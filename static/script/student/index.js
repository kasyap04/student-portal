
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
                document.getElementById('myadmno').innerText = data.adm_no ;
                document.getElementById('myimage').setAttribute('src', '/static/'+data.image) ;
                document.getElementById('lastlogin').innerText = 'Last login ' + data.last_login ;
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



function openNotification(t) {
    if($(t).attr("data-open") == "f"){
        $(t).parent().next().css({
            "text-overflow": "unset",
            "white-space": "unset",
            "overflow": "unset"
        }) ;

        $(t).parent().parent().css({
            "background-color": "rgba(138, 191, 230, 0.09)"
        }) ;

        $(t).css({
            "transform": "rotate(180deg)"
        }) ;
        $(t).attr("data-open", "t")
    } else {
        $(t).parent().next().css({
            "text-overflow": "ellipsis",
            "white-space": "nowrap",
            "overflow": "hidden"
        }) ;
        $(t).parent().parent().css({
            "background": "none"
        }) ;

        $(t).css({
            "transform": "rotate(0deg)"
        }) ;
        $(t).attr("data-open", "f")
    }


}