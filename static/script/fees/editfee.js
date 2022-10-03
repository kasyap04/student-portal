for (var i = 0; i < document.getElementsByClassName('admin-nav-cont')[0].children.length; i++){
    document.getElementsByClassName('admin-nav-cont')[0].children[i].children[0].classList.remove('selectedNav') ;
}



function saveChanges(feeId) {
        const fee = document.getElementById(`ediFeeAmount${ feeId }`).value ,
            due = document.getElementById(`editFeeDue${ feeId }`).value ;

        // console.log(feeId, fee, due) ;

        loadingAnim(1) ;
        $.ajax({
            cache: false,
            type: "POST",
            url: "",
            data:{csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
                feeId: feeId, fee: fee, due: due
            },
            success: function (result) {
                loadingAnim(0) ;
                console.log(result) ;
                try {
                    let data = JSON.parse(resJson(result))[0] ;
                    if(data == "s"){
                        showLineMsg("Fee edited", "po") ;
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
    }

    function deleteFee() {
        let feeId = $(".deleteFee-outer").attr('data-fee') ;
        loadingAnim(1) ;
        $.ajax({
            cache: false,
            type: "POST",
            url: "deletefee",
            data:{csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
                feeId: feeId
            },
            success: function (result) {
                loadingAnim(0) ;
                console.log(result) ;
                try {
                    let data = JSON.parse(resJson(result))[0] ;
                    if(data == "s"){
                        document.getElementById(`feeCont${ feeId }`).remove() ;
                        showLineMsg("Fee deleted", "po")
                        closeDeleteFee() ;
                    } else if(data == "uau"){
                        showLineMsg("You are not permitted to do this action", "ne") ;
                    } else if(data == "l"){
                        login() ;
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
    }


function closeDeleteFee() {
    $(".deleteFee-outer").hide() ;
}

function openDeleteFeeCont(id) {
    $(".deleteFee-outer").show() ;
    $(".deleteFee-outer").attr('data-fee', id) ;
}