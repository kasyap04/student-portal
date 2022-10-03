
function setProgress(){
    let elm = document.getElementById('progress').getAttribute('data-progress') ;
    // let elm = '[10, 7, 2]' ;
    try{
        let workProgress = JSON.parse(elm) ;
        // console.log(workProgress) ;
        let works = workProgress[0] ,
            submited = workProgress[1] ;
        let workPercentage = (submited/works)*100  ;
        //console.log(workPercentage) ;
        let angle = (workPercentage/100)*360 ;
      //  console.log( angle) ;

        $(".circle2").html(Math.round(workPercentage) + '%') ;

        if(angle <= 180){
            $(".circle .left .progress").css({
                "transform": "rotate("+ angle +"deg)"
            }) ;
        } else {
            angle -= 180 ;
            $(".circle .left .progress").css({
                "transform": "rotate(180deg)"
            }) ;
            $(".circle .right .progress").css({
                "transform": "rotate("+angle+"deg)"
            }) ;
        }

    } catch (e) {
        console.log(e) ;
        showLineMsg("Something went wrong about classwork progress bar", "ne") ;
    }
}

setProgress() ;

document.addEventListener("click", function (ev) {
    $(".changePass-btn-cont").hide() ;
})


function showChangePassBtn(t, e) {
    e.stopPropagation() ;
    $(".changePass-btn-cont").show() ;
    $(".changePass-btn-cont").css({
        "top": $(t).offset().top - 8 + "px",
        "left": $(t).offset().left - $(".changePass-btn-cont").width() - 30 + "px"
    }) ;
}

function closeChangePassCount() {
    document.getElementById('oldPassword').value  = "" ;
    document.getElementById('newPassword').value = "" ;
    document.getElementById('newPassCopy').value  = "" ;
    $(".change-pass-outer").fadeOut() ;
}

function openChangePassCount() {
    $(".change-pass-outer").fadeIn() ;
    document.getElementById('oldPassword').focus() ;
}

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


document.getElementById('changePassword').addEventListener("click", function() {
    $(".change-pass-cont label").hide() ;
    $(".change-pass-cont article").css("border-color", "black") ;
    let oldPassword = document.getElementById('oldPassword').value ,
        newPassword = document.getElementById('newPassword').value,
        copy = document.getElementById('newPassCopy').value ;


    if(!oldPassword){
        $(".oldPassword-arti").css("border-color", "red") ;
        $(".oldPassword-label").show() ;
        $(".oldPassword-label").html("Old password can not be empty") ;
        return false ;
    }

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
            url: "/login/changepassword",
            data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), old: oldPassword, n: newPassword},
            success: function (result) {
                loadingAnim(0) ;
                // console.log(result) ;
                try {
                    let data =  JSON.parse(resJson(result))[0] ;
                    if(data == "s"){
                        closeChangePassCount() ;
                        showLineMsg("Password changes successfully", "po") ;
                    } else if(data == "wp"){
                        $(".oldPassword-arti").css("border-color", "red") ;
                        $(".oldPassword-label").show() ;
                        $(".oldPassword-label").html("Password is incorrect") ;
                    } else if(data == "l"){
                        location.href = '/login/login' ;
                    }
                } catch (e) {
                    console.log(e) ;
                    showLineMsg("Something wend wrong, Please try again later", "ne") ;
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

document.getElementById('forgotPassBtn').addEventListener("click", function () {
    showLineMsg("Please contact the Admin", "nu") ;
}) ;


$(".personalDetails-btn-cont button").click(function (ev) {
    let btn = ev.target ;
    if(btn.getAttribute("data-show") === "f"){
        $(".profile-personalDetails").css("height", "fit-content") ;
        btn.setAttribute("data-show", "t") ;
        btn.innerHTML = "Show less" ;
    } else {
        $(".profile-personalDetails").css("height", "200px") ;
        btn.setAttribute("data-show", "f") ;
        btn.innerHTML = "Show more" ;
    }
}) ;