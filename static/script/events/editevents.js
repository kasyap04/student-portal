for (var i = 0; i < document.getElementsByClassName('admin-nav-cont')[0].children.length; i++){
    document.getElementsByClassName('admin-nav-cont')[0].children[i].children[0].classList.remove('selectedNav') ;
}
document.getElementsByClassName('admin-nav-cont')[0].children[5].children[0].classList.add('selectedNav') ;


function updateEvent(eventId) {
        const event = document.getElementById(eventId)
        let date = event.children[1].children[0].value,
            eventName = event.children[2].children[0].value ;
        //console.log(eventName)
        loadingAnim(1) ;
        $.ajax({
            cache:false,
            type:"POST",
            url:"'events/updateevents",
            data:{csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
                date: date, event: eventName, id: eventId},
            success: function (result) {
                loadingAnim(0) ;
                try {
                    let data = JSON.parse(resJson(result))[0] ;
                    if(data == "s"){
                        showLineMsg("Changes saved", "po") ;
                        location.reload() ;
                    } else if(data == "uau"){
                        showLineMsg("You are not permitted to do this action", "ne") ;
                    } else if(data == "l"){
                        login() ;
                    }
                } catch (e) {
                    console.log(e);
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

    function cancelUpadte(eventId) {
        const event = document.getElementById(eventId)
        $(event.children[0]).show() ;
        $(event.children[1]).hide() ;
        event.children[2].children[0].setAttribute('readonly', 'readonly') ;
        event.children[2].children[0].classList.remove('editInput') ;
        event.children[3].innerHTML = `<button class="edit-btn" onclick="editEvent(${eventId})">Edit</button>` ;
    }

    function editEvent(eventId){
        const event = document.getElementById(eventId)
        $(event.children[0]).hide() ;
        $(event.children[1]).show() ;
        event.children[2].children[0].removeAttribute('readonly') ;
        event.children[2].children[0].focus() ;
        event.children[2].children[0].classList.add('editInput') ;
        event.children[3].innerHTML = `<button class="cancel-btn" onclick='cancelUpadte(${eventId})'>cancel</button> <button class="save-btn" onclick='updateEvent(${eventId})'>Update</button>` ;
    }

    // months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Decembe'] ;
    //
    // function  getEvents() {
    //     const fromDate = document.getElementById('fromDate').value,
    //         toDate = document.getElementById('toDate').value ;
    //
    //     if(fromDate != "" && toDate != ""){
    //         var date = new Date(fromDate)
    //         $.ajax({
    //             cache:false,
    //             type:"POST",
    //             url:"",
    //             data:{csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
    //             fromDate: fromDate, toDate: toDate},
    //             success: function (result) {
    //                 console.log(result)
    //             },
    //             error: function (jqXHR, exception, responseText) {
    //                 console.log(jqXHR, exception, responseText)
    //             }
    //         }) ;
    //     }
    // }