function loadImage(e) {
    $("#img").show() ;
    $(".student-img").hide() ;
    $("#image").hide() ;
    $(".img-rem-cont").css({
        "display": "flex"
    });

    let output = document.getElementById('img') ;
    output.src = URL.createObjectURL(event.target.files[0]) ;
    output.onload = function () {
        URL.revokeObjectURL(output.src) ;
    }
}

function removeImage() {
    $("#img").attr('src', '') ;
    $("#img").hide() ;
    $("#image").val("") ;
    $("#image").show() ;
    $(".img-rem-cont").hide() ;
    $(".student-img").show() ;
}

function canRegister() {

    let nmbr = document.getElementById('selfMobile').value.trim() ;
    if(nmbr.length !== 10 || isNaN(nmbr)){
        $(".student-number label").html("Invalid phone number") ;
        $(".student-number label").show() ;
        return false ;
    }

    let email = document.getElementById('email').value.trim() ;
    if(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)){
        return true ;
    } else{
        $(".student-email label").html("Invalid email id") ;
        $(".student-email label").show() ;
        return false
    }

}


$("#stuRegForm").on("submit", function (e) {
    e.preventDefault() ;

    $(".student-field-cont label").hide() ;

    let image = document.getElementById('image').value ;
    if(image == ""){
        showLineMsg("Please select student profile image", "ne") ;
        return false ;
    }

    if(canRegister()){
        loadingAnim(1) ;
        $.ajax({
            cache: false,
            type: "POST",
            url: "/student/uploadstudent",
            data: new FormData(this),
            contentType:false,
            processData:false,
            xhr: function () {
                var xhr = new window.XMLHttpRequest();
                xhr.upload.addEventListener("progress", (evt) => {
                    if (evt.lengthComputable) {
                    var percentComplete = Math.round((evt.loaded / evt.total) * 100) ;
                     console.log(percentComplete)
                }
            }, false);
                return xhr;
            },
            success: function (result) {
                loadingAnim(0) ;
                console.log(result) ;
                try {
                    let data = JSON.parse(resJson(result))[0] ;
                    if(data == "s"){
                        showLineMsg("Student registered", "po") ;
                        removeImage() ;
                        document.getElementById('stuRegForm').reset() ;
                    } else if(data == "uau"){
                        showLineMsg("Unauthorised user, You can't register student", "ne") ;
                    } else if(data == "se"){
                        $(".student-admNo label").html("Student with this admission number already exist") ;
                        $(".student-admNo label").show();
                    } else if(data == "l"){
                        showLineMsg("Please login to continue", "ne") ;
                        login() ;
                    }
                } catch (e) {
                    console.log(e);
                    err() ;
                }
            },
            error: function (jqXHR, exception, responseText) {
                loadingAnim(0) ;
                console.log(jqXHR, exception, responseText) ;
            }
        }) ;
    }
}) ;


$("#stuEditForm").on("submit", function (e) {
    e.preventDefault() ;
    if(canRegister()){
        loadingAnim(1) ;
        $.ajax({
            cache: false,
            type: "POST",
            url: "",
            data: new FormData(this),
            contentType:false,
            processData:false,
            xhr: function () {
                var xhr = new window.XMLHttpRequest();
                xhr.upload.addEventListener("progress", (evt) => {
                    if (evt.lengthComputable) {
                    var percentComplete = Math.round((evt.loaded / evt.total) * 100) ;
                     console.log(percentComplete)
                }
            }, false);
                return xhr;
            },
            success: function (result) {
                loadingAnim(0) ;
                console.log(result) ;
                try {
                    let data = JSON.parse(resJson(result))[0] ;
                    if(data == "s"){
                        showLineMsg("Changes are saved", "po") ;
                    }
                }catch (e) {
                    console.log(e) ;
                    err() ;
                }
            },
            error: function (jqXHR, exception, responseText) {
                console.log(jqXHR, exception, responseText) ;
            }
        }) ;
    }
}) ;


function deleteImage(id) {
    loadingAnim(1) ;
        $.ajax({
            cache: false,
            type: "POST",
            url: "/student/deleteimage",
            data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), stu: id},
            success: function (result) {
                loadingAnim(0) ;
                console.log(result) ;
                try {
                    let data = JSON.parse(resJson(result))[0] ;
                    if(data == "s"){
                        showLineMsg("Profile image removed", "po") ;
                        removeImage() ;
                    } else if(data == "uau"){
                        showLineMsg("Unauthorised user, You can't register student", "ne") ;
                    } else if(data == "l"){
                        showLineMsg("Please login to continue", "ne") ;
                        login() ;
                    }
                } catch (e) {
                    console.log(e);
                    err() ;
                }
            },
            error: function (jqXHR, exception, responseText) {
                loadingAnim(0) ;
                err() ;
                console.log(jqXHR, exception, responseText) ;
            }
        }) ;
}