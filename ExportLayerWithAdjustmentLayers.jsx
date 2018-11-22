var myLayerGroup = app.activeDocument.layerSets;//.getByName()
var rootLayers = app.activeDocument.artLayers;

//alert(myLayerGroup.length);
//alert(rootLayers.length);

for(i=0;i<myLayerGroup.length;i++){
    var layerInGoup = myLayerGroup[i];
    //alert(layerInGoup.artLayers[0].name);
    //saveJpeg(layerInGoup.artLayers[0].name);
}
//for var in myLayerGroup  alert(myLayerGroup.name);
// function saveJpegBackup(folder, name){
//     var doc = app.activeDocument;
//     if (folder != ""){
//         alert(folder);
//         //var layerFolder = new Folder(doc.path +'/' + folder + '/');
//         //alert(layerFolder.path);
//         var newFolder = new Folder(doc.path +'/' + folder + '/');
//         if (!newFolder.exists){
//             newFolder.create();
//         }
//        // alert(newFolder)
//         var file = new File(newFolder + '/' + name + '.jpg');
//     }else{
//         var file = new File(doc.path + '/' + name + '.jpg');
//     }
//     var opts = new JPEGSaveOptions();
//     opts.quality = 10;
//     doc.saveAs(file, opts, true);
// }

function saveJpeg(folder, name){
    var doc = app.activeDocument;
    var newFolder;
    if (folder != ""){
        // alert(folder);
        //var layerFolder = new Folder(doc.path +'/' + folder + '/');
        //alert(layerFolder.path);
        newFolder = new Folder(folder);
        if (!newFolder.exists){
            newFolder.create();
        }
       // alert(newFolder)
        // var file = new File(newFolder + '/' + name + '.jpg');
    }else{
        newFolder = doc.path;
    }
    var file = new File(newFolder + '/' + name + '.jpg');
    var opts = new JPEGSaveOptions();
    opts.quality = 10;
    doc.saveAs(file, opts, true);
}

function hideAllLayers(){
    for (i=0; i<rootLayers.length; i++){
        if (rootLayers[i].allLocked != true){
            rootLayers[i].visible = false;
        }
    }
    for (i=0; i<myLayerGroup.length; i++){
        myLayerGroup[i].visible = false;
    }
}

function showAllLayers(){
    for (i=0; i<rootLayers.length; i++){
        if (rootLayers[i].allLocked != true){
            rootLayers[i].visible = true;
        }
    }
    for (i=0; i<myLayerGroup.length; i++){
        myLayerGroup[i].visible = true;
    }
}

function makeValidFileName(fileName)
{
	var validName = fileName.replace(/^\s+|\s+$/gm, '');	// trim spaces
	validName = validName.replace(/[\\\*\/\?:"\|<>]/g, ''); // remove characters not allowed in a file name
    validName = validName.replace(/[ ]/g, '_');	// replace spaces with chosen delimiter, since some programs still may have troubles with them
	return validName;
}

function diveAllLayers(groups,path){
    //alert(groups.length);
    //var curPath = path;
    //alert(path);
    for (i=0;i<groups.length;i++){
        alert('i='+i);
        var tempGroup = groups[i];
        alert('msg1 '+tempGroup.name);
        var newPath = path + '/' + makeValidFileName(tempGroup.name);
        // var newFolder = new Folder(newPath);
        // if (!newFolder.exists){
        //     newFolder.create();
        // }
        //alert(newPath);

        alert('msg2 '+tempGroup.artLayers.length);
        if(tempGroup.artLayers.length>0){
            for(j=0; j<tempGroup.artLayers.length; j++){
                //alert(tempGroup.artLayers[j].name);
                saveJpeg(newPath,makeValidFileName(tempGroup.artLayers[j].name));
                alert('saved');
                //var newFilename = makeValidFileName(tempGroup.artLayers[j].name);
            }
        }
        if(tempGroup.layerSets.length>0){
            diveAllLayers(tempGroup.layerSets,newPath);
        }
        alert('done='+i);
    } 
}

(function main(){
    var rootGroups = app.activeDocument.layerSets;
    diveAllLayers(rootGroups, app.activeDocument.path);
   // showAllLayers();
   return;
   alert("START");
   hideAllLayers();
   for (i=0; i<rootLayers.length; i++){
       if (rootLayers[i].allLocked != true){
           rootLayers[i].visible = true;
 //          saveJpeg("", rootLayers[i].name);
           rootLayers[i].visible = false;
        }
    }
    alert("ROOT LAYER DONE");
    
    for(i=0; i < myLayerGroup.length; i++){
        myLayerGroup[i].visible = true;
        for (j=0;j<myLayerGroup[i].artLayers.length;j++){
            // alert("1-5");
            myLayerGroup[i].artLayers[j].visible = true;
            //alert("1-6");
            var folder = myLayerGroup[i].name;
           // alert(folder);
            saveJpeg(myLayerGroup[i].name, myLayerGroup[i].artLayers[j].name);
            myLayerGroup[i].artLayers[j].visible = false;
        }
        myLayerGroup[i].visible = false;
    }
    
    alert("GROUP LAYER DONE");
    //alert(layerInGoup.artLayers[0].name);
        //saveJpeg(layerInGoup.artLayers[0].name);
    })();