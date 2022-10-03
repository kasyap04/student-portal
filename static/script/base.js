'use-strict'

resJson = str => str.substring( str.indexOf('sta[')+3, str.indexOf(']end')+1 ) ;

function showLineMsg(msg, type){
    if(type == "po"){
        $(".lineMsg-cont").css({
            "color": "green",
            "border-color": "green"
        }) ;
    } else if(type == "ne") {
        $(".lineMsg-cont").css({
            "color": "red",
            "border-color": "red"
        }) ;
    } else {
        $(".lineMsg-cont").css({
            "color": "black",
            "border-color": "black"
        }) ;
    }

    $(".lineMsg-cont").animate({
        "bottom": "100px"
    }, 150) ;

    setTimeout(function() {
        $(".lineMsg-cont").animate({
        "bottom": "-50px"
    }, 150) ;
    }, 2000) ;

    $(".lineMsg-cont").html(msg) ;
}


var dla ;  // delay loading anim
loadingAnim = m => { // m =>   1 for open,   0 for close
    if(m == 1){
        dla = setTimeout(() => {
            $(".loading-outer").show() ;
        }, 500) ;
    } else if(m == 0){
        $(".loading-outer").hide() ;
        clearTimeout(dla) ;
    }
}


function openLogoutCont() {
    $(".logut-outer").show() ;
    $(".logout-cont").show() ;
}

function closeLogoutCont() {
    $(".logut-outer").hide() ;
    $(".logout-cont").hide() ;
}

function login() {
    location.href = 'login/login' ;
}

function logout() {
    console.log(0) ;
    $.ajax({
        cache: false,
        type: "POST",
        url: "/login/action",
        data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), swift: 2},
        success: function (result) {
            console.log(result) ;
            try {
                let data = JSON.parse(resJson(result))[0] ;
                if(data == "s"){
                    showLineMsg("Log out", "po") ;
                    location.reload() ;
                }
            }catch (e) {
                console.log(e) ;
                showLineMsg("Something wend wrong, Please refresh and try again", "ne") ;
            }
        },
        error: function (jqXHR, exception, responseText) {
            console.log(jqXHR, exception, responseText) ;
        }
    }) ;
}

err = () => showLineMsg("Something wend wrong, Please refresh and try again", "ne") ;



closeOPTCont = () => {
    $(".otp-cont").animate({
        "bottom": "-300px"
    }, 200, () => {
        document.getElementById('otp').value = "" ;
        $(".otp-cont").css("display", "none") ;
    }) ;
} ;

openOPTCont = (nmbr) => {
    $(".otp-cont").css("display", "grid") ;
    $(".otp-cont").animate({
        "bottom": "20px"
    }, 200, () => {
        document.getElementById('otp').focus() ;
        document.getElementById('numberForOTP').innerText = nmbr ;
    }) ;
} ;

// openOPTCont() ;

closeNumberVerify = () => {
    $(".otp-number-cont").animate({
        "bottom": "-300px"
    }, 200, () => {
        document.getElementById('mobileNumber').value = "" ;
        $(".otp-number-cont").css("display", "none") ;
    }) ;
} ;


openNumberVerify = () => {
    $(".opt-outer").show() ;
    $(".otp-number-cont").css("display", "grid") ;
    $(".otp-number-cont").animate({
        "bottom": "20px"
    }, 200, () => {
        document.getElementById('mobileNumber').focus() ;
    }) ;
} ;

// openNumberVerify() ;

openChangeForgotPassword = () => {
    $(".password-cont").show() ;
    $(".password-cont").animate({
        "bottom": "20px"
    }, 200, () => {
        document.getElementById('pass1').focus() ;
    }) ;
} ;

// openChangeForgotPassword() ;


function verifyMobileNumber() {
    $(".otp-number-cont label").hide() ;

    let nmbr = document.getElementById('mobileNumber').value.trim() ;
    if(isNaN(nmbr.substring(nmbr.length - 10))){
        $(".otp-number-cont label").html("Invalid phone number") ;
        $(".otp-number-cont label").show() ;
        return false ;
    }

    if(nmbr){
        loadingAnim(1) ;
        $.ajax({
            cache: false,
            type: "POST",
            url: "/login/changeforgotpassword",
            data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), s: 1, num: nmbr},
            success: function (result) {
                loadingAnim(0) ;
                console.log(result) ;
                try{
                    let data = JSON.parse(resJson(result))[0] ;
                    if(data == "s"){
                        showLineMsg("Number verified, Please verify OPT", "po") ;
                        closeNumberVerify() ;
                        setTimeout(() =>{ openOPTCont(nmbr) ; }, 1000) ;
                    } else if(data == "nnf"){
                        $(".otp-number-cont label").html("No accound found in this number") ;
                        $(".otp-number-cont label").show() ;
                    }
                } catch (e) {
                    console.log(e) ;
                    err() ;
                }
            },
            error: function (jqXHR, exception, responseText) {
                loadingAnim(0) ;
                err() ;
                console.log(jqXHR, exception, responseText) ;
            }
        }) ;
    } else {
        $(".otp-number-cont label").html("Please enter your registered mobile number") ;
        $(".otp-number-cont label").show() ;
    }
}


function verifyOTP() {
    $(".otp-cont label").hide() ;
    let otp = document.getElementById('otp').value.trim() ;
    if(otp){
        loadingAnim(1) ;
        $.ajax({
            cache: false,
            type: "POST",
            url: "/login/changeforgotpassword",
            data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), s: 2, otp: otp},
            success: function (result) {
                loadingAnim(0) ;
                console.log(result) ;
                try{
                    let data = JSON.parse(resJson(result))[0] ;
                    if(data == "s"){
                        showLineMsg("OTP verified", "po") ;
                        closeOPTCont() ;
                        openChangeForgotPassword() ;
                    } else if(data == "io"){
                        $(".otp-cont label").html("Incorrect OTP") ;
                        $(".otp-cont label").show() ;
                    }
                } catch (e) {
                    console.log(e) ;
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
}


function changeForgotPassword() {
    $(".password-cont label").hide() ;
    let pass1 = document.getElementById('pass1').value,
        pass2 = document.getElementById('pass2').value ;

    if(pass1 == ""){
        $(".forgotPassLabel1").html("Please enter a new password") ;
        $(".forgotPassLabel1").show() ;
        return false ;
    }

    if(pass1.length <= 6){
        $(".forgotPassLabel1").html("Password must contain more than 6 characters") ;
        $(".forgotPassLabel1").show() ;
        return false ;
    }

    if(pass1 === pass2){
        loadingAnim(1) ;
        $.ajax({
            cache: false,
            type: "POST",
            url: "/login/changeforgotpassword",
            data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), s: 3, p: pass2},
            success: function (result) {
                loadingAnim(0) ;
                console.log(result) ;
                try{
                    let data = JSON.parse(resJson(result))[0] ;
                    if(data == "s"){
                        $(".password-cont input").val("") ;
                        showLineMsg("Password changed", "po") ;
                        location.reload() ;
                    }
                } catch (e) {
                    console.log(e) ;
                    err() ;
                }
            },
            error: function (jqXHR, exception, responseText) {
                loadingAnim(0) ;
                err() ;
                console.log(jqXHR, exception, responseText) ;
            }
        }) ;
    } else {
        $(".forgotPassLabel2").html("Password not matching") ;
        $(".forgotPassLabel2").show() ;
    }
}