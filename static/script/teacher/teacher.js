function getMyName() {
    loadingAnim(1) ;
    $.ajax({
        cache: false,
        type: "GET",
        url: '/student/myname',
        success: function (result) {
            loadingAnim(0) ;
            // console.log(result) ;
            try{
                let data = JSON.parse(resJson(result))[0] ;
                document.getElementById('myname').innerText = data.name ;
                document.getElementById('lastlogin').innerText = 'Last login ' + data.last_login ;
                document.getElementById('phone').innerText = data.phone ;
                document.getElementById('email').innerText = data.email ;
                if(data.hasOwnProperty('hod')){
                    $("#t_pos").append(`<section class="left-cont2">
                        <article style="text-transform: capitalize">${data.hod}</article>
                        <article>HOD</article>
                    </section>`) ;
                }

                if(data.hasOwnProperty('ct')){
                    $("#t_pos").append(`<section class="left-cont2">
                        <article >${data.ct}</article>
                        <article>Class teacher</article>
                    </section>`) ;

                }

                if( data.hasOwnProperty('sem')){
                    document.getElementById('addattendenceLink').setAttribute("href", `/attendence/add?dep=${data.dep_id}&sem=${data.sem}`) ;
                } else if(data.hasOwnProperty('nosem')){
                    document.getElementById('addattendenceLink').removeAttribute("href") ;
                    document.getElementById('addattendenceLink').setAttribute("onclick", "openSelectSem()") ;
                    $(".sel-sem-cout").attr("data-dep", data.dep_id) ;
                } else
                    $("#addattendenceLink").hide() ;


            } catch (e) {
                console.log(e) ;
                showLineMsg("Something wend wrong, Please refresh and try again", "ne") ;
            }
        },
        error: function (jqXHR, exception, responseText) {
            loadingAnim(0) ;
            console.log(jqXHR, exception, responseText) ;
        }
    }) ;
}

getMyName() ;


document.addEventListener("click", function (ev) {
    $(".menu-cont").hide() ;
})


function showMenuItems(subId, t, e) {
    e.stopPropagation() ;
    $(".menu-cont").show() ;
    $(".menu-cont").css({
        "top": $(t).offset().top  + "px",
        "left": ($(t).offset().left - 190) + "px"
    }) ;

    $("#notifLink").attr("href", '/notifications/add?sub=' + subId) ;
    $("#internalLink").attr("href", '/internals/add?sub=' + subId) ;
    $("#editInternalLink").attr("href", '/internals/edit?sub=' + subId) ;
}


function closeSelectSem() {
    $(".sel-sem-outer").hide() ;
}


function openSelectSem() {
     $(".sel-sem-outer").show() ;
}

function gotoAttendence(sem) {
    closeSelectSem() ;
    location.href = `/attendence/add?dep=${$(".sel-sem-cout").attr("data-dep")}&sem=${sem}` ;
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
        $(t).attr("data-show", "f");
        $(t).prev().attr("type", "password");
        $(t).html("show");
    }
}

document.getElementById('forgotPassBtn').addEventListener("click", function () {
    $(".change-pass-outer").hide() ;
    openNumberVerify() ;
}) ;



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

        $.ajax({
            cache: false,
            type: "POST",
            url: "/login/changepassword",
            data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), old: oldPassword, n: newPassword},
            success: function (result) {
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
                console.log(jqXHR, exception, responseText) ;
            }
        }) ;

    } else {
        $(".newPassCopy-arti").css("border-color", "red") ;
        $(".newPassCopy-label").show() ;
        $(".newPassCopy-label").html("Password not matching") ;
    }
}) ;