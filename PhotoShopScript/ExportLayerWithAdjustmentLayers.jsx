var rootLayers = app.activeDocument.artLayers;
var rootGroups = app.activeDocument.layerSets;

function saveJpeg(folder, name)
{
    var doc = app.activeDocument;
    var newFolder;
    if (folder != ""){
        newFolder = new Folder(folder);
        if (!newFolder.exists){
            newFolder.create();
        }
    }else{
        newFolder = doc.path;
    }
    var file = new File(newFolder + '/' + name + '.jpg');
    var opts = new JPEGSaveOptions();
    opts.quality = 10;
    doc.saveAs(file, opts, true);
}

function showHideAllLayers(groups,operation)
{
    var condition = false;
    if (operation=='show'){
        condition = true;
    }
    var artLayers = groups.artLayers;
    var layerSets = groups.layerSets;
    if (artLayers.length>0){
        for (var i=0; i<artLayers.length; i++){
            if (artLayers[i].allLocked != true){
                artLayers[i].visible = condition;
            }
        }
    }
    if (layerSets.length>0){
        for (var j=0; j<layerSets.length; j++){
            if (layerSets[j].allLocked != true){
                layerSets[j].visible = condition;
                showHideAllLayers(layerSets[j],operation);
            }
        }
    }
}

function makeValidFileName(fileName)
{
	var validName = fileName.replace(/^\s+|\s+$/gm, '');	// trim spaces
	validName = validName.replace(/[\\\*\/\?:"\|<>]/g, ''); // remove characters not allowed in a file name
    validName = validName.replace(/[ ]/g, '_');	// replace spaces with chosen delimiter, since some programs still may have troubles with them
	return validName;
}

function diveAllLayers(groups,path)
{
    for (var i=0;i<groups.length;i++)
    {
        var tempGroup = groups[i];
        tempGroup.visible = true;
        var newPath = path + '/' + makeValidFileName(tempGroup.name);
        if (tempGroup.artLayers.length>0)
        {
            for(var j=0; j<tempGroup.artLayers.length; j++)
            {
                tempGroup.artLayers[j].visible = true;
                saveJpeg(newPath,makeValidFileName(tempGroup.artLayers[j].name));
                tempGroup.artLayers[j].visible = false;
            }
        }
        if(tempGroup.layerSets.length>0)
        {
            diveAllLayers(tempGroup.layerSets,newPath);
        }
        tempGroup.visible = false;
    } 
}

(function main(){
    showHideAllLayers(app.activeDocument, 'show');
    showHideAllLayers(app.activeDocument, 'hide');
    diveAllLayers(rootGroups, app.activeDocument.path);
})();