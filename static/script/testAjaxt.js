
document.body.onclick = () => {
    $(".err-msg").hide() ;
}

createErrMsg = (element, msg) => {
    $(".err-msg span").text(msg) ;
    $(".err-msg").show() ;
    $(".err-msg").css({
        "top":$(`#${element}`).offset().top - 45 + "px" ,
        "left":($(`#${element}`).offset().left + ($(`#n`).width()/2) - ($(".err-msg").width()/2)) + 'px'
    }) ;
}


document.getElementById('loginBtn').addEventListener("click", (event) => {
    event.stopPropagation() ;

    let login = {
        'user':document.getElementById('user').value ,
        'username':document.getElementById('n').value,
        'password':document.getElementById('pass').value,
        csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val()
    } ;
    

    if(login.user == ""){
        createErrMsg("user", "Please select a user") ;
        $(".err-msg").css({
            "left":($(`#user`).offset().left + ($(`#n`).width()/2) - ($(".err-msg").width()/2) - 125 ) + "px"
        }) ;
        return false
    }

    if(login.username == ""){
        createErrMsg("n", "Please enter your username or admission number") ;
        return false ;
    }

    if(login.password == ""){
        createErrMsg("pass", "Please enter your password") ;
        return false ;
    }
    $.ajax({
        cache:false,
        type:"POST",
        url:"/login",
        data:login,
        success:function(result){
            console.log(result) ;
            location.href = `/student/?name=${result}`
        },
        error:function(jqXHR, exception, responseText){
            console.log(jqXHR) ;
            console.log(exception) ;
            console.log(responseText) ; 
        }
    }) ;
}) ;
