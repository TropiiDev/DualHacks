var pfpselector = document.getElementById('pfpfileselector');

pfpselector.onchange = function(event){
        //  https://web.dev/read-files/#read-content 
        // https://stackoverflow.com/questions/3814231/loading-an-image-to-a-img-from-input-file

        const reader = new FileReader();
        var fileList = event.target.files;
        reader.onload = function () {
            document.getElementById('userpfp').src = event.target.result;
        }
        reader.readAsDataURL(fileList[0]);
    }

console.log('test')