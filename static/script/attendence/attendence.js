'use-strict'
for (var i = 0; i < document.getElementsByClassName('student-nav-cont')[0].children.length; i++){
    document.getElementsByClassName('student-nav-cont')[0].children[i].children[0].classList.remove('selectedNav') ;
}

document.getElementsByClassName('student-nav-cont')[0].children[1].children[0].classList.add('selectedNav') ;


function clearEntry() {
    document.getElementById('attendForm').reset() ;
    document.getElementById('attDate').value = "" ;
}


function uploadAttendence() {
    const elm = document.getElementsByClassName('attendence-student-list') ;

    if(document.getElementById('attDate').value == ""){
        showLineMsg("Please select date", "ne") ;
        document.getElementById('attDate').focus() ;
        return false ;
    }

    res = {
           "dep": document.getElementById('attDep').value,
           "sem": document.getElementById('attSem').value,
            "date": document.getElementById('attDate').value,
            att:{}
        } ;

    for(let i =0; i < elm.length; i++){
        let stu = elm[i].getAttribute("data-stu") ;
        let attend = document.querySelector(`input[name=att${stu}]:checked`).value ;
        res.att[stu.toString()] = attend
    }

        loadingAnim(1) ;
        $.ajax({
            cache:false,
            type:"POST",
            url:"/attendence/uploadattendence",
            data:{csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
                a:JSON.stringify(res)
            },
            success:function(result){
                loadingAnim(0) ;
                console.log(result) ;
                try {
                    let data = JSON.parse(resJson(result))[0] ;
                    if(data == "s"){
                        showLineMsg("Attendence uploaded", "po") ;
                    } else if(data == "e"){
                        showLineMsg("Currenlty unable to upload attendentce", "ne") ;
                    }
                } catch (e) {
                    console.log(e) ;
                    showLineMsg("Something went wrong, Please try again later", "ne") ;
                }
            },
            error:function(jqXHR, exception, responseText){
                loadingAnim(0) ;
                console.log(jqXHR, exception, responseText) ;
            }
        }) ;
}

document.addEventListener("click", () => {
    $(".editAttendence-count").hide() ;
}) ;

function openEditAttend(t, e) {
    e.stopPropagation() ;
    $(".editAttendence-count").show() ;
    $(".editAttendence-count").css({
        "top": $(t).offset().top - 10 + 'px',
        "left": ( Math.round($(t).offset().left) - 145 ) + 'px'
    }) ;
}



function closeDateCont() {
    $(".editAttend-date-cont").hide() ;
}

function openDateCount() {
    $(".editAttend-date-cont").show() ;
}

function gotoEditAttend(t) {
    closeDateCont() ;
    location.href = `/attendence/edit?sem=${document.getElementById('attSem').value}&date=${t.value}` ;
}



function editAttendence(t) {

        console.log(t.getAttribute("data-attendId"), t.value) ;

        loadingAnim(1) ;
        $.ajax({
            cache: false,
            type: "POST",
            url: "",
            data:{csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), id: t.getAttribute("data-attendId"), attend: t.value},
            success: function (result) {
                loadingAnim(0) ;
                console.log(result) ;
                try {
                    let data = JSON.parse(resJson(result))[0] ;
                    if(data == "s"){
                        showLineMsg("Attendence edited", "po") ;
                    }
                } catch (e) {
                    console.log(e) ;
                    showLineMsg("Something went wrong, Please refresh and try again", "ne") ;
                }
            },
            error: function (jqXHR, exception, responseText) {
                loadingAnim(0) ;
                console.log(jqXHR, exception, responseText) ;
            }
        }) ;
    }



    function changeAttendenceMonth(t) {
        location.href = "/attendence/myattendence?date=" + t.value ;
    }