'use-strict'

    $.ajax({
        cache: false,
        type: "POST",
        url: "/login/action",
        data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), swift: 1},
        success: function (result) {
            console.log(result) ;
            try {
                let data = JSON.parse(resJson(result))[0] ;
                if(data == "stu"){
                    location.href = '/temp/student/' ;
                } else if(data == "tea"){
                    location.href = '/temp/teacher/' ;
                }else if(data == "adm"){
                    location.href = '/temp/admin/' ;
                } else if(data == "pri"){
                    location.href = '/temp/principal/' ;
                }
            }catch (e) {
                console.log(e) ;
            }
        },
        error: function (jqXHR, exception, responseText) {
            console.log(jqXHR, exception, responseText) ;
        }
    }) ;


$("#loginForm").on("submit", function (e) {
    e.preventDefault() ;

    loadingAnim(1) ;
    $.ajax({
        cache: false,
        type: "POST",
        url: "/login/login",
        data: new FormData(this),
        contentType:false,
        processData:false,
        success: function (result) {
            loadingAnim(0) ;
            console.log(result) ;
            try {
                let data = JSON.parse(resJson(result))[0] ;
                if(data == "stu"){
                    location.href = '/temp/student/' ;
                } else if(data == "tea"){
                    location.href = '/temp/teacher/' ;
                } else if(data == "adm"){
                    location.href = '/temp/admin/' ;
                } else if(data == "pri"){
                    location.href = '/temp/principal/' ;
                }else if(data == "e"){
                    showLineMsg("Incorrect user id or password", "ne") ;
                }
            }catch (e) {
                loadingAnim(0) ;
                showLineMsg("Something wend wrong, Refesh and try again", "ne") ;
            }
        },
        error: function (jqXHR, exception, responseText) {
            loadingAnim(0) ;
            console.log(jqXHR, exception, responseText) ;
        }
    }) ;
}) ;


function togglePassword(t) {
    if (t.getAttribute("data-show") == "false"){
        t.setAttribute("data-show", "true") ;
        $(t).prev().attr("type", "input") ;
        $(t).prev().focus() ;
        t.innerHTML = "hide" ;
    } else{
        t.setAttribute("data-show", "false") ;
        $(t).prev().attr("type", "password") ;
        $(t).prev().focus() ;
        t.innerHTML = "show" ;
    }
}