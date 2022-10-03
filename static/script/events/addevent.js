for (var i = 0; i < document.getElementsByClassName('admin-nav-cont')[0].children.length; i++){
    document.getElementsByClassName('admin-nav-cont')[0].children[i].children[0].classList.remove('selectedNav') ;
}
document.getElementsByClassName('admin-nav-cont')[0].children[4].children[0].classList.add('selectedNav') ;


function addEvents() {

        const date = document.getElementById('addEventDate').value,
            event = document.getElementById('addEventBody').value.trim() ;

        if(date != "" && event != ""){
            loadingAnim(1) ;
            $.ajax({
                cache:false,
                type:"POST",
                url:"/events/uploadevents",
                data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
                date: date, event: event },
                success: function (result) {
                    loadingAnim(0) ;
                    // console.log(result) ;
                    try {
                        let data = JSON.parse(resJson(result))[0] ;
                        if (data == "s"){
                            document.getElementById('addEventBody').value = "" ;
                            document.getElementById('addEventDate').value = "" ;
                            showLineMsg("Event added", "po") ;
                        } else if(data == "l"){
                            login() ;
                        } else if(data == "pd"){
                            showLineMsg("Can't add past events", "ne") ;
                        }
                    } catch (e) {
                        console.log(e) ;
                        err() ;
                    }
                },
                error: function (jqXHR, exception, responseText) {
                    loadingAnim(0) ;
                    err() ;
                    console.log(jqXHR, exception, responseText)
                }
            }) ;
        }
    }