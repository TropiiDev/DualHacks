var pfpselector = document.getElementById('pfpfileselector');
// var Jimp = require('jimp')


pfpselector.onchange = function(event){
        // https://stackoverflow.com/questions/38691318/resize-an-image-in-node-js-using-jimp-and-get-the-path-the-new-image
        //  https://web.dev/read-files/#read-content 
        // https://stackoverflow.com/questions/3814231/loading-an-image-to-a-img-from-input-file

        const reader = new FileReader();
        var fileList = event.target.files;
        console.log('test')
        reader.onload = function (event) {
            // Jimp.read(reader.result, function (err, test){
            //     if (err) throw err;
            //     test.resize(256, 256)
            //         .quality(50)                 
            //         .write("userpfp.png"); 
            // })
            
            document.getElementById('userpfp').src = event.target.result
            // console.log(document.getElementById('userpfp'))
            // console.log('pain')
        }
        reader.readAsDataURL(fileList[0])
    }
