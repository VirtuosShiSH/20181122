//alert("hello worm");

var myLayerGroup = app.activeDocument.layerSets;//.getByName()
var rootLayers = app.activeDocument.artLayers;

//alert(myLayerGroup.length);
//alert(rootLayers.length);

//saveJpeg("whwhwh");
for(i=0;i<myLayerGroup.length;i++){
    var layerInGoup = myLayerGroup[i];
    //alert(layerInGoup.artLayers[0].name);
    //saveJpeg(layerInGoup.artLayers[0].name);
}
//for var in myLayerGroup  alert(myLayerGroup.name);

function saveJpeg(folder, name){
    var doc = app.activeDocument;
    if (folder != ""){
        alert(folder);
        //var layerFolder = new Folder(doc.path +'/' + folder + '/');
        //alert(layerFolder.path);
        var newFolder = new Folder(doc.path +'/' + folder + '/');
        if (!newFolder.exists){
            newFolder.create();
        }
       // alert(newFolder)
        var file = new File(newFolder + '/' + name + '.jpg');
    }else{
        var file = new File(doc.path + '/' + name + '.jpg');
    }
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



(function main(){
   // showAllLayers();
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