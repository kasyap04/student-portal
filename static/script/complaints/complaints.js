for (var i = 0; i < document.getElementsByClassName('student-nav-cont')[0].children.length; i++){
    document.getElementsByClassName('student-nav-cont')[0].children[i].children[0].classList.remove('selectedNav') ;
}

document.getElementsByClassName('student-nav-cont')[0].children[5].children[0].classList.add('selectedNav') ;

 function postComplaint() {
     $(".complaint-err").hide() ;
        const to = document.querySelector(`input[name=complaintTo]:checked`)  ,
            body = document.getElementById('complaintbody').value.trim() ;

        if(to != null && body != ""){
            // console.log(to.value, body) ;

            loadingAnim(1) ;
            $.ajax({
                cache: false,
                type: "POST",
                url: "/complaints/add",
                data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
                to: to.value, body: body},
                success: function (result) {
                    loadingAnim(0) ;
                    console.log(result) ;
                    try{
                        let data = JSON.parse(resJson(result))[0] ;
                        if(data == "s"){
                            showLineMsg("Complaint filed successfully", "po") ;
                            document.getElementById('complaintFrom').reset() ;
                            document.getElementById('complaintbody').value = "" ;
                        }
                    } catch (e) {
                        showLineMsg("Unable to file the complaint, Please try again later", "ne") ;
                    }
                },
                error: function (jqXHR, exception, responseText) {
                    loadingAnim(0) ;
                    err() ;
                    console.log(jqXHR, exception, responseText) ;
                }
            }) ;
        } else {
            if(to == null){
                $(".fileto").html("Please fill this field") ;
                $(".fileto").show();
            }
            if(body == ""){
                $(".create").html("Please fill this field") ;
                $(".create").show();
            }
        }
    }

    document.addEventListener("click", function () {
         $(".complaint-box-cont").css({
            "height":"fit-content"
        }) ;
        $(".complaint-body").css({
            "height":"55px"
        }) ;
        $(".complaint-reply-cont").hide() ;
    }) ;

    function expandComplaint(t, e) {
        e.stopPropagation() ;
        $(".complaint-box-cont").css({
            "height":"fit-content"
        }) ;
        $(".complaint-body").css({
            "height":"55px"
        }) ;

        $(t.children[0].children[0].children[1]).css({
            "height":"fit-content"
        }) ;

        if($(t.children[0].children[1]) != undefined){
            $(t.children[0].children[1]).show() ;
        }

    }

    document.getElementById('complaintbody').addEventListener("input", function (e) {
        document.getElementById('complantCharCount').innerText = e.target.value.length + "/200" ;
    })  ;

 function openCreateComplaint() {
    $(".complaint-history-cont").css({
        "display":"none"
    }) ;
    $(".complaint-new-cont").show() ;
    $(".createComplaintBtn-cont").hide() ;
 }

 function closeCreateComplaintCont() {
     $(".complaint-history-cont").css({
        "display":"grid"
    }) ;
    $(".complaint-new-cont").hide() ;
    $(".createComplaintBtn-cont").show() ;
 }