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
            Jimp.read(reader.result, function (err, test){
                if (err) throw err;
                test.resize(256, 256)
                    .quality(50)
                    .getBase64(Jimp.MIME_PNG, function (err, base64) {  // get base64
                        if (err) throw err;
                        document.getElementById('userpfp').src = base64;  // set src of new image
                        console.log(base64)
                        // var xmlHttp = new XMLHttpRequest();
                        // // https://stackoverflow.com/questions/247483/http-get-request-in-javascript
                        // xmlHttp.onreadystatechange = function() { 
                        //     if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
                        //         callback(xmlHttp.responseText);
                        // }
                        // xmlHttp.open('GET', '/setprofilepic', true, )
                        // xmlHttp.send('null')
                        fetch(
                            '/setprofilepic',
                            {
                                method:'GET',
                                headers:{
                                    'url':base64
                                }
                            }
                        )
                    });
            })
        }
        reader.readAsDataURL(fileList[0])
    }
