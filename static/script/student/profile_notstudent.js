
function togglePassword(t) {
    if($(t).attr("data-show") == "f"){
        $(t).attr("data-show", "t") ;
        $(t).prev().attr("type", "text") ;
        $(t).html("hide") ;
    } else {
        $(t).attr("data-show", "f") ;
        $(t).prev().attr("type", "password") ;
        $(t).html("show") ;
    }
}


function closeChangePassCount() {
    document.getElementById('newPassword').value = "" ;
    document.getElementById('newPassCopy').value  = "" ;
    $(".change-pass-outer").fadeOut() ;
}

function openChangePassCount() {
    $(".change-pass-outer").fadeIn() ;
    document.getElementById('newPassword').focus() ;
}


document.getElementById('changePassword').addEventListener("click", function() {
    $(".change-pass-cont label").hide() ;
    $(".change-pass-cont article").css("border-color", "black") ;
    let newPassword = document.getElementById('newPassword').value,
        copy = document.getElementById('newPassCopy').value ;


    if(!newPassword){
        $(".newPassword-arti").css("border-color", "red") ;
        $(".newPassword-label").show() ;
        $(".newPassword-label").html("New password can not be empty") ;
        return false ;
    }

    if(newPassword.length <= 6){
        $(".newPassword-arti").css("border-color", "red") ;
        $(".newPassword-label").show() ;
        $(".newPassword-label").html("Password must be greater than 6 charecters") ;
        return false ;
    }

    if(newPassword === copy){

        loadingAnim(1) ;
        $.ajax({
            cache: false,
            type: "POST",
            url: "/login/stupass",
            data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), n: newPassword, stu: document.getElementById('stu').value},
            success: function (result) {
                loadingAnim(0) ;
                // console.log(result) ;
                try {
                    let data =  JSON.parse(resJson(result))[0] ;
                    if(data == "s"){
                        closeChangePassCount() ;
                        showLineMsg("Password changes successfully", "po") ;
                    }else if(data == "l"){
                        location.href = '/login/login' ;
                    } else if(data == "uau"){
                        showLineMsg("Unauthorised user", "ne") ;
                    }
                } catch (e) {
                    console.log(e) ;
                    showLineMsg("Something went wrong, Please try again later", "ne") ;
                }
            },
            error: function (jqXHR, exception, responseText) {
                loadingAnim(0) ;
                console.log(jqXHR, exception, responseText) ;
            }
        }) ;

    } else {
        $(".newPassCopy-arti").css("border-color", "red") ;
        $(".newPassCopy-label").show() ;
        $(".newPassCopy-label").html("Password not matching") ;
    }
}) ;


function openSemCountProfile(e, dep, dur) {
    e.stopPropagation() ;
    let stu = parseInt(document.getElementById('stu').value) ;
    let totSem = parseInt(dur)*2 ;
    document.getElementById('semCont').innerHTML = "" ;
    for(let i = 1; i <= totSem; i++){
        document.getElementById('semCont').innerHTML += `<a href="/fees/studentpaid?dep=${dep}&sem=${i}&stu=${stu}"> <article>${i}</article> </a>` ;
    }
    $(".sel-sem-outer").show() ;
}

        for (var i = 0; i < document.getElementsByClassName('admin-nav-cont')[0].children.length; i++){
            document.getElementsByClassName('admin-nav-cont')[0].children[i].children[0].classList.remove('selectedNav') ;
        }
