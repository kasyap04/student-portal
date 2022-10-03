function submitClasswork() {

        let work = {
            title: document.getElementById('workTitle').value.trim(),
            body: document.getElementById('workBody').value.trim() ,
            time:  document.getElementById('workTime').value,
            date:  document.getElementById('workDate').value,
            dep: document.getElementById('dep').value,
            sem: document.getElementById('sem').value,
            sub: document.getElementById('sub').value
        } ;

        const setErr = ['Title', 'Body', 'Due time', 'Due date'] ;

        // console.log(work) ;

        let canUpload = true ;

        for(let i = 0; i <= 6; i++){
            if(work[Object.keys(work)[i]] == ""){
                canUpload = false ;
                if(i <= 3){
                    showLineMsg(setErr[i]+' of classwork not found', "ne") ;
                }
                break ;
            }
        }

        if(canUpload){
            $.ajax({
                cache: false,
                type: "POST",
                url: "/classroom/addclasswork",
                data:{csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), d: JSON.stringify(work)},
                success: function (result) {
                    console.log(result) ;
                    try {
                      let data = JSON.parse(resJson(result))[0] ;
                        if(data == "s"){
                           showLineMsg("Classwork added", "po") ;
                           setTimeout(function () {
                               location.reload() ;
                           }, 1000) ;
                        } else if(data == "e"){
                            showLineMsg("Classwork couldn't add at this moment, Please try again later", "ne") ;
                        } else if(data == "l"){
                            showLineMsg("Please login to continue", "ne") ;
                            setTimeout(function () {
                                location.href = '/login/login' ;
                            }, 1000) ;
                        }
                    } catch (e) {
                        console.log(e) ;
                        showLineMsg("Something wend wrong, Please refresh and try again", "ne") ;
                    }
                },
                error: function (jqXHR, exception, responseText) {
                    console.log(jqXHR, exception, responseText) ;
                }
            }) ;
        }

    }

    function closeAddClasswork() {
        $(".addClasswork-cont").hide() ;
        $(".addClasswork-defult").css("display", "flex") ;
    }

    function openAddClasswork()  {
        $(".addClasswork-defult").hide() ;
        $(".addClasswork-cont").show() ;
    }