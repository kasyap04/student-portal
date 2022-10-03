
canRegister = () => {
    let nmbr = document.getElementById('num').value.trim() ;
    if(nmbr.length !== 10 || isNaN(nmbr)){
        $(".teacher-number label").html("Invalid phone number") ;
        $(".teacher-number label").show() ;
        return false ;
    }

    let exp = document.getElementById('exp').value ;
    if(isNaN(exp)){
        $(".teacher-exp label").html("Invalid experiance") ;
        $(".teacher-exp label").show() ;
        return false ;
    }

    let email = document.getElementById('email').value.trim() ;
    if(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)){
        return true ;
    } else{
        $(".teacher-email label").html("Invalid email id") ;
        $(".teacher-email label").show() ;
        return false
    }
} ;

$("#teacherRegForm").on("submit", function (e) {
    e.preventDefault() ;
    $(".student-fields label").hide() ;
    if(canRegister()){
        loadingAnim(1) ;
        $.ajax({
            cache: false,
            type: "POST",
            url: "",
            data: new FormData(this),
            contentType:false,
            processData:false,
            success: function (result) {
                loadingAnim(0) ;
                console.log(result) ;
                try {
                    let data = JSON.parse(resJson(result))[0] ;
                    if(data == "s"){
                        document.getElementById('teacherRegForm').reset() ;
                        showLineMsg("Teacher registered", "po")
                    } else if(data == "te"){
                        showLineMsg("Number already exist", "ne") ;
                        $(".teacher-number label").html("Teacher with this number already exist") ;
                        $(".teacher-number label").show() ;
                    }
                } catch (e) {
                    console.log(e) ;
                    loadingAnim(0) ;
                    err() ;
                }
            },
            error: function (jqXHR, exception, responseText) {
                loadingAnim(0) ;
                console.log(jqXHR, exception, responseText) ;
            }
        }) ;
    }
}) ;




$("#teacherEditForm").on("submit", function (e) {
    e.preventDefault() ;
    $(".student-fields label").hide() ;
    if(canRegister()){
        loadingAnim(1) ;
        $.ajax({
            cache: false,
            type: "POST",
            url: "",
            data: new FormData(this),
            contentType:false,
            processData:false,
            success: function (result) {
                loadingAnim(0) ;
                console.log(result) ;
                try {
                    let data = JSON.parse(resJson(result))[0] ;
                    if(data == "s"){
                        showLineMsg("Changes are saved", "po")
                    } else if(data == "te"){
                        showLineMsg("Number already exist", "ne") ;
                        $(".teacher-number label").html("Teacher with this number already existe") ;
                        $(".teacher-number label").show() ;
                    }
                } catch (e) {
                    console.log(e) ;
                    loadingAnim(0) ;
                    err() ;
                }
            },
            error: function (jqXHR, exception, responseText) {
                loadingAnim(0) ;
                console.log(jqXHR, exception, responseText) ;
            }
        }) ;
    }
}) ;



function deleteTeacher(id) {
        console.log(id) ;
        loadingAnim(1) ;
        $.ajax({
            cache: false,
            type: "POST",
            url: "/teachers/deleteteacher",
            data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
            teacher_id: id},
            success: function (result) {
                loadingAnim(0);
                console.log(result) ;
                let data = JSON.parse(resJson(result))[0] ;
                if(data == "s"){
                    showLineMsg("Teacher is deleted", "po") ;
                    closeDeleteTeachCont() ;
                } else if(data == "auu"){
                    showLineMsg("You are not permitted to do this action", "ne") ;
                    closeDeleteTeachCont() ;
                } else if(data == "l"){
                    showLineMsg("Please login to continue", "ne") ;
                    login() ;
                }
            },
            error: function (jqXHR, exception, responseText) {
                loadingAnim(0) ;
                err() ;
                console.log(jqXHR, exception, responseText) ;
            }
        }) ;
}

function closeDeleteTeachCont() {
    $(".delete-teacher-outer").hide() ;
}

function showDeleteTeachCont() {
    $(".delete-teacher-outer").show() ;
}

