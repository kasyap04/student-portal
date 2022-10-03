
    function cancelUpdate(count) {
        let selDep = document.getElementsByClassName('department-list-cont')[count] ;
        for(let i = 0; i < 3; i++){
            selDep.children[i].setAttribute("contenteditable", 'false') ;
        }
        $(`.save${count}, .cancel${count}`).hide() ;
        $(`.edit${count}`).show() ;
    }

    function updateDepartment(depId, count) {
        let selDep = document.getElementsByClassName('department-list-cont')[count] ;

        let shotname = selDep.children[0].innerText ,
            name = selDep.children[1].innerText,
            duration = selDep.children[2].children[0].innerText ,
            hod = selDep.children[3].children[0].value ;

        loadingAnim(1) ;
        $.ajax({
            cache: false,
            type: "POST",
            url: "/department/changedepartment",
            data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
                shotname: shotname, name: name, dur: duration, hod: hod, depId: depId },
            success: function (result) {
                loadingAnim(0) ;
                console.log(result) ;
                try {
                    let data = JSON.parse(resJson(result))[0] ;
                    if(data == "s"){
                        showLineMsg("Saved changes", "po") ;
                    }
                }catch (e) {
                    console.log(e) ;
                    err() ;
                }
            },
            error: function (jqXHR, exception, responseText) {
                loadingAnim(0) ;
                console.log(jqXHR, exception, responseText) ;
            }
        }) ;
    }

    function editDepartment(depId, count) {
        // console.log(depId) ;
       let selDep = document.getElementsByClassName('department-list-cont')[count] ;
        for(let i = 0; i < 2; i++){
            selDep.children[i].setAttribute("contenteditable", 'true') ;
        }
        selDep.children[2].children[0].setAttribute("contenteditable", 'true')
        $(`.save${count}, .cancel${count}`).show() ;
        $(`.edit${count}`).hide() ;
    }

