for (var i = 0; i < document.getElementsByClassName('student-nav-cont')[0].children.length; i++){
    document.getElementsByClassName('student-nav-cont')[0].children[i].children[0].classList.remove('selectedNav') ;
}



checkNumber = t => isNaN(t.value) ? t.value = "" : t.value ;

function saveEditedInternals(id, t) {
    const mark = document.getElementById(`mark${id}`).value ;

    if(mark > t.getAttribute("data-tot")){
        showLineMsg("Student's mark cannot be greater then total mark", "ne") ;
        document.getElementById(`mark${id}`).focus() ;
        return false ;
    }

    if(mark){
        loadingAnim(1) ;
        $.ajax({
            cache: false,
            type:"POST",
            url: "/internals/edit",
            data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), id: id, mark: mark },
            success: function (result){
                loadingAnim(0) ;
                // console.log(result) ;
                try {
                    let data = JSON.parse(resJson(result))[0] ;
                    if (data == "s"){
                        showLineMsg("Student's mark changed", "po") ;
                    }
                } catch (e) {
                    console.log(e) ;
                    showLineMsg("Something wend wrong, Please refresh and try again", "ne") ;
                }
            },
            error: function (jqXHR, exception, responseText){
                loadingAnim(0);
                console.log(jqXHR, exception, responseText) ;
            }
        }) ;
    } else {
        document.getElementById(`mark${id}`).focus() ;
        showLineMsg("Student's mark cannot be empty", "ne") ;
    }

}