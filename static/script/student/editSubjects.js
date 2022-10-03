

 function editSubject(id) {
    $(`#delBtn${id}`).show() ;
    $(`#saveBtn${id}`).show() ;
    $(`#cancelBtn${id}`).show() ;
    $(`#editBtn${id}`).hide() ;
    teacherSelectedId.show = true ;
    for(let i = 0; i <= 2; i++){
        document.getElementById(`subList${id}`).children[i].setAttribute("contenteditable", "true") ;
    }
}

    function cancelUpdate(id) {
    $(`#delBtn${id}`).hide() ;
    $(`#saveBtn${id}`).hide() ;
    $(`#cancelBtn${id}`).hide() ;
    $(`#editBtn${id}`).show() ;
    teacherSelectedId.show = false ;
        for(let i = 0; i <= 2; i++){
            document.getElementById(`subList${id}`).children[i].setAttribute("contenteditable", "false") ;
        }
    }

    function saveSubject(id ) {
        const selected = document.getElementById(`subList${id}`) ;
        let sub = {
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
            name: document.getElementById(`name${id}`).innerText,
            code: document.getElementById(`code${id}`).innerText,
            type: document.getElementById(`type${id}`).innerText,
            teacher: document.getElementById(`teacher${id}`).getAttribute("data-teacherId"),
            subId: id,
            swift: 1
        } ;


        let canSaveChanges = true ;
        for(let i = 0; i < Object.keys(sub).length; i++){
            if(sub[Object.keys(sub)[i]] == ""){
                canSaveChanges = false ;
                break ;
            }
        }
        if(canSaveChanges){
            loadingAnim(1) ;
            $.ajax({
                cache:false,
                type:"POST",
                url:"",
                data:sub,
                success:function(result){
                    loadingAnim(0) ;
                    console.log(result) ;
                    console.log("res = ", result) ;
                    let data = JSON.parse(resJson(result))[0] ;
                    if(data == "s"){
                        showLineMsg("Subject edited", "po") ;
                        cancelUpdate(id) ;
                    }
                },
                error:function(jqXHR, exception, responseText){
                    console.log(jqXHR) ;
                    console.log(exception) ;
                    console.log(responseText) ;
                }
            }) ;
        } else
            console.log("please fill all field") ;
    }

    function deleteSubject() {
    let id = $(".delete-conf-outer").attr('data-id') ;
        let sub = {
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
            subId: id,
            swift: 2
        } ;

        loadingAnim(1) ;
        $.ajax({
            cache:false,
            type:"POST",
            url:"",
            data:sub,
            success:function(result){
                loadingAnim(0) ;
                // console.log(result) ;
                try {
                    let data = JSON.parse(resJson(result))[0] ;
                    if(data == "s"){
                        showLineMsg("Subject deleted", "po") ;
                        document.getElementById(`subList${id}`).remove() ;
                        closeDeleteCont() ;
                    }
                } catch (e) {
                    console.log(e) ;
                    err() ;
                }
            },
            error:function(jqXHR, exception, responseText){
                loadingAnim(0) ;
                err() ;
                console.log(jqXHR) ;
                console.log(exception) ;
                console.log(responseText) ;
            }
        }) ;
    }

    const teacherSelectedId = {
        id: 0,
        show: false
    } ;

    // $("#selTeacher").hide() ;

    function closeSelectTeacher() {
         $(".teacher-sel-outer").hide() ;
    }

    function selectTeacher() {
        const selected = document.getElementById('selTeacher').value ;
        let id = selected.substring(0, selected.indexOf('==')).trim() ,
            name = selected.substring(selected.indexOf('==')+2).trim() ;
        document.getElementById(`teacher${teacherSelectedId.id}`).setAttribute("data-teacherId", id)
        document.getElementById(`teacher${teacherSelectedId.id}`).innerText = name ;
        closeSelectTeacher();
        $("#selTeacher").val("") ;
    }

    function changeTeacher(id) {
        if(teacherSelectedId.show){
            $(".teacher-sel-outer").show() ;
            teacherSelectedId.id = id ;
        }
    }


    function closeDeleteCont() {
        $(".delete-conf-outer").hide() ;
    }

    function openDeleteCont(id) {
        $(".delete-conf-outer").show() ;
        $(".delete-conf-outer").attr('data-id', id) ;
    }