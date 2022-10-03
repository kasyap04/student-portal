function postNotification() {
    $("#notif + span").hide() ;
    $("#notif").css("border-color", "black") ;

    // const dep = document.getElementById('notifDepId'),
    //     s = document.getElementById('notifSemId'),
    //     sub = document.getElementById('notifSubId'),
    //     stu = document.getElementById('notifStu') ;
    //
    // const dep_id = dep == undefined ? null : dep.value ,
    //     sem = s == undefined ? null : s.value,
    //     sub_id = sub == undefined ? null : sub.value,
    //     stu_id = stu == undefined ? null : stu.value ;
    const body = document.getElementById('notif').value.trim() ;
    // console.log(dep_id, sem, sub_id, stu_id) ;

    if(body == ""){
        $("#notif + span").show() ;
        $("#notif + span").html("Please fill this field") ;
        $("#notif").css("border-color", "red") ;
        return false ;
    }

    const contId = document.getElementById('contId').value ;
    const cont = document.getElementById('contId').getAttribute('data-con') ;
    let sem_id = document.getElementById('conSem').value.trim() ;

    let toSend ;
    if(sem_id != ""){
        toSend = {
            'cont': cont,
            'cont_id': contId,
            'sem': sem_id,
            'body': body
        } ;
    } else {
        toSend = {
            'cont': cont,
            'cont_id': contId,
            'body': body
        } ;
    }

    if(cont != ""){
        $.ajax({
            cache: false,
            type: "POST",
            url: "/notifications/addNotifications",
            // data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), dep: dep_id, sem: sem, sub: sub_id, stu: stu_id, body: body},
            data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), cont: JSON.stringify(toSend) },
            success: function (result) {
                console.log(result)
                try{
                    let data = JSON.parse(resJson(result))[0] ;
                    if(data == "s"){
                        document.getElementById('notif').value = "" ;
                        showLineMsg("Notification send", "po") ;
                    }
                } catch (e) {
                    console.log(e) ;
                    showLineMsg("Something wend wrong, Please refresh and try again", "ne") ;
                }
            },
            error: function (jqXHR, exception, responseText) {
                console.log(jqXHR, exception, responseText) ;}}) ;
    } else{
        showLineMsg("Something wend wrong, Please refresh and try again", "ne") ;
    }
}

if(document.getElementsByClassName('student-nav-cont')[0] != undefined){
    for (var i = 0; i < document.getElementsByClassName('student-nav-cont')[0].children.length; i++){
        document.getElementsByClassName('student-nav-cont')[0].children[i].children[0].classList.remove('selectedNav') ;
    }
}

