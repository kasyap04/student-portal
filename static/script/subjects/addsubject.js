document.getElementById('addSubYear').innerHTML = '<option value=""></option>' ;
for (let i = 2013; i <= new Date().getFullYear(); i++){
    document.getElementById('addSubYear').innerHTML += `<option value="${i}">${i}</option>` ;
}


function addNewSubjects() {
        $(".add-sub label").hide() ;
        let department = {
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
            dep: document.getElementById('adSubDep').value,
            sem: document.getElementById('adSubSem').value,
            sub: document.getElementById('addSubName').value.trim(),
            code: document.getElementById('addSubCode').value.trim(),
            type: document.getElementById('addSubType').value.trim(),
            teacher: document.getElementById('addSubTeacher').value,
            year: document.getElementById('addSubYear').value
        } ;


        let canUpload = true ;

        for(let i = 0; i < Object.keys(department).length; i++){
            if(department[Object.keys(department)[i]] == ""){
                $(`#addSubErr${i}`).html("Please fill this field") ;
                $(`#addSubErr${i}`).show() ;
                canUpload = false ;
                break ;
            }
        }
        if(canUpload){
            loadingAnim(1) ;
            $.ajax({
                cache: false,
                type: "POST",
                url: "",
                data: department,
                success: function (result) {
                    loadingAnim(0) ;
                    console.log(result) ;
                    try {
                        let data = JSON.parse(resJson(result))[0] ;
                        if(data == "s"){
                            $(".add-sub input").val("") ;
                            document.getElementById('addSubTeacher').value = "" ;
                            document.getElementById('addSubYear').value = "" ;
                            showLineMsg("New subject is added", "po") ;
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
            showLineMsg("Please fill all fields", "ne") ;
        }
    }