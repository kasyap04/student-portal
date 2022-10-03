for (var i = 0; i < document.getElementsByClassName('student-nav-cont')[0].children.length; i++){
    document.getElementsByClassName('student-nav-cont')[0].children[i].children[0].classList.remove('selectedNav') ;
}


function clearEntry(){
    document.getElementById('internalDate').value = null ;
    document.getElementById('internalTotalMark').value = null ;
    document.getElementById('examName').value = null ;
    $(".studentMark").val("") ;
}


function submitInternals() {
    const elm = document.getElementsByClassName('studentMark') ;

    let internal = {
        'sub': document.getElementById('internalSubId').value,
        'date': document.getElementById('internalDate').value,
        'total_mark': document.getElementById('internalTotalMark').value,
        'exam_name': document.getElementById('examName').value,
        'marks': []
    } ;

     if(internal.exam_name == ""){
        showLineMsg("Please select exam name", "ne") ;
        document.getElementById('examName').focus() ;
        return false ;
    }

    if(internal.total_mark == ""){
        showLineMsg("Please set total mark to exam", "ne") ;
        document.getElementById('internalTotalMark').focus() ;
        return false ;
    }

    if(internal.date == ""){
        showLineMsg("Please select date of exam conducted", "ne") ;
        document.getElementById('internalDate').focus() ;
        return false ;
    }


    for(let i = 0; i < elm.length; i ++){
        if(elm[i].value == ""){
            showLineMsg("Please fill all fields", "ne") ;
            elm[i].focus() ;
            return false ;
        } else
            internal.marks.push( {'stu_id': parseInt(elm[i].getAttribute("data-id")), 'mark': parseInt(elm[i].value)} ) ;
    }

    loadingAnim(1) ;
    $.ajax({
        cache: false,
        type: "POST",
        url: "/internals/add",
        data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 'i': JSON.stringify(internal)},
        success:function(result){
            loadingAnim(0) ;
            // console.log(result) ;
            try {
                let data = JSON.parse(resJson(result))[0] ;
                if(data == "s"){
                    clearEntry() ;
                    showLineMsg("Internals uploaded", "po") ;
                }
            } catch (e) {
                console.log(e) ;
                showLineMsg("Somethign wend wrong, Please refresh and try again", "ne") ;
            }
        },
        error:function(jqXHR, exception, responseText){
            loadingAnim(0) ;
            console.log(jqXHR) ;
            console.log(exception) ;
            console.log(responseText) ;
        }
    }) ;
}



checkNumber = t => isNaN(t.value) ? t.value = "" : t.value ;