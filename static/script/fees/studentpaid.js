function checkFeild(t) {
    if(isNaN(t.value)){
        t.value = "" ;
    }
}


function addFee(id) {
    $(".stu-addFee-cont label").hide() ;
        const amount = document.getElementById(`fee${id}`).value ,
            stuId = document.getElementById('stu').value ;
        let date = document.getElementById(`date${id}`).value ;
        if(amount != "" && date != ""){
            loadingAnim(1) ;
            $.ajax({
                cache: false,
                type: "POST",
                url: "",
                data:{csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
                feeId: id, amount: amount, stu: stuId, date: date, swift: 1 },
                success: function (result) {
                    loadingAnim(0) ;
                    // console.log(result) ;
                    try {
                        let data = JSON.parse(resJson(result))[0] ;
                        if(data == "s"){
                           showLineMsg("Fee paid by student updated", "po") ;
                           document.getElementById(`fee${id}`).value = "" ;
                        }
                    }catch (e) {
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
            if(amount == ""){
                $(`.errMsgFee${id}`).html("Please enter valid fee") ;
                $(`.errMsgFee${id}`).show() ;
            }

            if(date == ""){
                $(`.errMsgDate${id}`).html("Please enter date format") ;
                $(`.errMsgDate${id}`).show() ;
            }
            }
    }


    function updateFee(paidId, feeId) {
    $(".stu-addFee-cont label").hide() ;
        const amount = document.getElementById(`fee${feeId}`).value ;
        let date = document.getElementById(`date${feeId}`).value ;


        if(amount != "" && date){
            loadingAnim(1) ;
            $.ajax({
                cache: false,
                type: "POST",
                url: "",
                data:{csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
                paidId: paidId, amount: amount, date: date, swift: 2 },
                success: function (result) {
                    loadingAnim(0) ;
                    // console.log(result) ;
                    try {
                        let data = JSON.parse(resJson(result))[0] ;
                        console.log(data) ;
                        if(data == "s"){
                            showLineMsg("Fee paid by student updated", "po") ;
                            document.getElementById(`fee${feeId}`).value = "" ;
                        }
                    }catch (e) {
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
            if(amount == ""){
                $(`.errMsgFee${feeId}`).html("Please enter valid fee") ;
                $(`.errMsgFee${feeId}`).show() ;
            }

                if(date == ""){
                $(`.errMsgDate${feeId}`).html("Please enter date format") ;
                $(`.errMsgDate${feeId}`).show() ;
            }
        }
    }

    for (var i = 0; i < document.getElementsByClassName('admin-nav-cont')[0].children.length; i++){
        document.getElementsByClassName('admin-nav-cont')[0].children[i].children[0].classList.remove('selectedNav') ;
    }
