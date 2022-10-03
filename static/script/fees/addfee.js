for (var i = 0; i < document.getElementsByClassName('admin-nav-cont')[0].children.length; i++){
    document.getElementsByClassName('admin-nav-cont')[0].children[i].children[0].classList.remove('selectedNav') ;
}
document.getElementsByClassName('admin-nav-cont')[0].children[3].children[0].classList.add('selectedNav') ;


function postFees() {
    $('.add-fee-sections label').hide() ;
    let feeDet = {
        'dep': document.getElementById('addFeeDep').value,
        'sem': document.getElementById('addFeeSem').value,
        'amount': document.getElementById('addFeeamount').value.trim(),
        'name': document.getElementById('addFeeName').value.trim(),
        'due': document.getElementById('addFeeDue').value
    } ;

    for (let i = 0; i <=3; i++ ){
        if(feeDet[Object.keys(feeDet)[i]] == ""){
            $(`#affFeeErr${i}`).show() ;
            $(`#affFeeErr${i}`).html("Please fill this field") ;
            showLineMsg("Please fill all fields", "ne") ;
            return false ;
        }
    }

    if(isNaN(feeDet.amount)){
        $(`#affFeeErr2`).show() ;
        $(`#affFeeErr2`).html("Please enter valid fee format") ;
        return false ;
    }

    loadingAnim(1) ;
    $.ajax({
            cache: false,
            type: "POST",
            url: "/fees/postfee",
            data:{csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), det: JSON.stringify(feeDet)},
            success: function (result) {
                loadingAnim(0) ;
                console.log(result) ;
                try {
                    let data = JSON.parse(resJson(result))[0] ;
                    if(data == "s"){
                        showLineMsg("Academic fee added", "po") ;
                        clearFields() ;
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


function clearFields() {
    $(".add-fee-sections input, select").val("") ;
}