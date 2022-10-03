
function getTeachers() {
    let dep = document.getElementById('ctDep').value ,
        sem = document.getElementById('ctSem').value ;

    if(dep != "" && sem != ""){
        loadingAnim(1) ;
        $.ajax({
            cache: false,
            type: "POST",
            url: "/teachers/classteacher",
            data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), swift: 1, dep: dep, sem: sem},
            success: function (result){
                loadingAnim(0) ;
                // console.log(result) ;
                try {
                    let data = JSON.parse(resJson(result))[0][0] ;
                    let classteacherId = "" ;
                    if(data.hasOwnProperty('ct')){
                        classteacherId = data.ct ;
                    }

                    document.getElementById('classteacher').innerHTML = "" ;
                    document.getElementById('classteacher').innerHTML = '<option></option>' ;

                    for(let i = 0; i < data.teachers.length; i++){
                        if (classteacherId == data.teachers[i].teacher_id){
                            document.getElementById('classteacher').innerHTML += `<option value="${data.teachers[i].teacher_id}" selected>${data.teachers[i].name}</option>` ;
                        } else
                            document.getElementById('classteacher').innerHTML += `<option value="${data.teachers[i].teacher_id}">${data.teachers[i].name}</option>` ;

                    }

                } catch (e) {
                    err() ;
                    console.log(e) ;
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


function saveClassTeacher() {
    let dep = document.getElementById('ctDep').value ,
        sem = document.getElementById('ctSem').value ,
        ct = document.getElementById('classteacher').value ;

    if(dep != "" && sem != "" && ct != ""){
        $.ajax({
            cache: false,
            type: "POST",
            url: "/teachers/classteacher",
            data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), swift: 2, dep: dep, sem: sem, ct: ct},
            success: function (result){
                loadingAnim(0) ;
                console.log(result) ;
                try {
                    let data = JSON.parse(resJson(result))[0] ;
                    if(data == "cs"){
                        showLineMsg("Class teacher changed", "po") ;
                    } else if(data == "cts"){
                        showLineMsg("Class teacher added", "po") ;
                    }
                    document.getElementById('ctDep').value = "" ;
                    sem = document.getElementById('ctSem').value = "" ;
                    ct = document.getElementById('classteacher').value = "";

                } catch (e) {
                    err() ;
                    console.log(e) ;
                }
            },
            error: function (jqXHR, exception, responseText) {
                loadingAnim(0) ;
                err() ;
                console.log(jqXHR, exception, responseText) ;
            }
        }) ;
    } else
        showLineMsg()
}


                for (var i = 0; i < document.getElementsByClassName('admin-nav-cont')[0].children.length; i++){
                    document.getElementsByClassName('admin-nav-cont')[0].children[i].children[0].classList.remove('selectedNav') ;
                }
                document.getElementsByClassName('admin-nav-cont')[0].children[6].children[0].classList.add('selectedNav') ;
