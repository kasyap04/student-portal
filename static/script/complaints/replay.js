function sendReply() {
    $(".reply-err").hide() ;
    let reply = document.getElementById('complaintreply').value ,
        id = document.getElementById('repId').value ;
    if(reply){
        loadingAnim(1) ;
        $.ajax({
            cache: false,
            type: "POST",
            url: "/complaints/view",
            data:{csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), r: reply, i: id},
            success: function (result) {
                loadingAnim(0) ;
                // console.log(result) ;
                try {
                    let data = JSON.parse(resJson(result))[0] ;
                    if(data == "s"){
                        showLineMsg("Reply send", "po") ;
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
        $(".reply-err").html("Please type your reply") ;
        $(".reply-err").show() ;
    }
}