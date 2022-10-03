function getMyName() {
    loadingAnim(1) ;
    $.ajax({
        cache: false,
        type: "GET",
        url: '/student/myname',
        success: function (result) {
            loadingAnim(0) ;
            // console.log(result) ;
            try{
                let data = JSON.parse(resJson(result))[0] ;
                // console.log(data) ;
                document.getElementById('myName').innerText = data.name ;
                document.getElementById('lastlogin').innerText = 'Last login ' + data.last_login ;
            } catch (e) {
                console.log(e) ;
                showLineMsg("Something wend wrong, Please refresh and try again", "ne") ;
            }
        },
        error: function (jqXHR, exception, responseText) {
            loadingAnim(0) ;
            console.log(jqXHR, exception, responseText) ;
        }
    }) ;
}

getMyName() ;

function searchStudents(t) {
    let search = t.value ;
    if(search){
        t.value = t.value.toUpperCase() ;
        $.ajax({
            cache: false,
            type: "POST",
            url: "/student/searchstudent",
            data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), search: search},
            success: function (result) {
                // console.log(result) ;
                try {
                    let data = JSON.parse(result) ;
                    document.getElementById('searchResult').innerHTML = "" ;
                    if(data.length > 0){
                        $(".search-result-cont").show() ;
                        for(let i = 0; i < data.length; i++){
                            document.getElementById('searchResult').innerHTML += `<a href="/student/profile?stu=${data[i][2]}"><section class="search-result-list">
                                <article>${data[i][1]}</article>
                                <article>${data[i][0]}</article>
                            </section></a>` ;
                        }
                    }else
                        $(".search-result-cont").hide() ;
                } catch (e) {
                    console.log(e) ;
                    showLineMsg("Something went wrong, Please refresh and try again", "ne") ;
                }
            },
            error: function (jqXHR, exception, responseText) {
                console.log(jqXHR, exception, responseText) ;
            }
        }) ;
    } else
        $(".search-result-cont").hide() ;
}

document.addEventListener("click", () => {
    $(".menu-cont").hide() ;
    closeSelectSem() ;
}) ;



function closeSelectSem() {
    $(".sel-sem-outer").hide() ;
}


function openSemCount(t, e) {
    e.stopPropagation() ;
    let sem = parseInt(t.getAttribute('data-dur'))*2 ;
    let dep = t.getAttribute('data-depId') ;
    document.getElementById('semCont').innerHTML = "" ;
    for(let i = 1; i <=sem; i++ ){
        document.getElementById('semCont').innerHTML += `<a href="/subject/view?dep=${dep}&sem=${i}"> <article>${i}</article> </a>` ;
    }
    $(".sel-sem-outer").show() ;
}


function openEditSubMenu(t, e) {
    e.stopPropagation() ;
    $(".menu-subject").show() ;
    $(".menu-subject").css({
        "top": $(t).offset().top + "px",
        "left": $(t).offset().left - $(".menu-subject").width() + "px"
    }) ;

    let dep = document.getElementById('showSubDepId').value,
        sem = document.getElementById('showSubSem').value ;
    $(".menu-subject a:nth-child(1)").attr('href', `/notifications/add?dep=${dep}&sem=${sem}`)  ;
    $(".menu-subject a:nth-child(2)").attr('href', `/fees/view?dep=${dep}&sem=${sem}`)  ;
    $(".menu-subject a:nth-child(3)").attr('href', `/attendence/students?dep=${dep}&sem=${sem}`)  ;
    $(".menu-subject a:nth-child(4)").attr('href', `/internals/studentinternal?dep=${dep}&sem=${sem}&exam=1`)  ;
}


function openSendNofiCount(t, e) {
    e.stopPropagation() ;
    $(".menu-notif a:nth-child(1)").attr('href', '/notifications/add?dep=' + t.getAttribute('data-depId') )
    $(".menu-notif").show() ;
    $(".menu-notif").css({
        "top": $(t).offset().top + "px",
        "left": $(t).offset().left - $(".menu-notif").width() + "px"
    }) ;

    // $(".upgradeSem-outer").attr('data-depId', t.getAttribute('data-depId')) ;
    // $(".upgradeSem-outer").attr('data-depName', t.getAttribute('data-depName')) ;
}