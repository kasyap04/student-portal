document.getElementById('addDepDur').addEventListener("input", (ev) => {
    if(isNaN(ev.target.value)){
        ev.target.value = "" ;
    }
}) ;

function clearAddDepartment() {
    $(".addDepartment input").val("") ;
    $(".addDepartment label").hide() ;
    $(".addDepartment input").css({
        "border-color": "#80808065"
    }) ;
}

function saveAddDepartment() {
    $(".addDepartment label").hide() ;
    $(".addDepartment input").css({
        "border-color": "#80808065"
    }) ;
    const addDep = {
        'name': document.getElementById('addDepName').value.trim(),
        'short': document.getElementById('addDepShortName').value.trim(),
        'dur': document.getElementById('addDepDur').value
    } ;

    if(addDep.name == ""){
        $(".addDep-name-cont label").html("Please enter department name") ;
        $(".addDep-name-cont label").show() ;
        $(".addDep-name-cont input").css({
            "border-color": "red"
        }) ;
        return false ;
    }

    if(addDep.short == "") {
        $(".addDep-shortname-cont label").html("Please enter department name");
        $(".addDep-shortname-cont label").show();
        $(".addDep-shortname-cont input").css({
            "border-color": "red"
        });
        return false;
    }

    if(addDep.dur == ""){
        $(".addDep-duration-cont label").html("Please enter department name");
        $(".addDep-duration-cont label").show();
        $(".addDep-duration-cont input").css({
            "border-color": "red"
        });
        return false;
    }

    loadingAnim(1) ;
    $.ajax({
        cache: false,
        type: "POST",
        url: "/department/add",
        data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), dep: JSON.stringify(addDep)},
        success: function (result) {
            loadingAnim(0) ;
            // console.log(result) ;
            try {
                let data = JSON.parse(resJson(result))[0] ;
                if(data == "s"){
                    showLineMsg("New department added", "po") ;
                    clearAddDepartment() ;
                } else if(data == "l"){
                    showLineMsg("Please login to continue", "ne") ;
                    login() ;
                }
            } catch (e) {
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