$(".goback").click(function () {
    window.history.back() ;
}) ;


    function getFileType(f) {
        let ext = f.substring(f.lastIndexOf("."), f.length) ;
        if( ext == '.docx' ){
            return "WordDocument" ;
        } else if(ext == '.pptx'){
            return "PowerPoint" ;
        } else if(ext == '.pdf') {
            return "PDF" ;
        }else if ( ['.png', '.jpg', '.jpeg', '.img'].some(function (value) {
            return value == ext ;
        }) ) {
            return "IMAGE" ;
        } else if( ['.mp4', '.mov', '.avi', '.mkv', '.webm'].some(function (value) {
            return value == ext ;
        }) ) {
            return "VIDEO" ;
        } else if( ['.m4a', '.mp3', '.wav', '.aac'].some(function (value) {
            return value == ext ;
        }) ){
            return "AUDIO" ;
        } else
        return "FILE" ;
    }


            // function switchToHome(){
            //     $(".classwork-home-cont").hide() ;
            //     $(".classroom-home-cont").show() ;
            //
            //     document.getElementsByClassName('classroom-nav')[1].classList.remove('selected-classroom-nav') ;
            //     document.getElementsByClassName('classroom-nav')[0].classList.add('selected-classroom-nav') ;
            // }
            //
            // function switchToClasswork(){
            //     $(".classroom-home-cont").hide() ;
            //     $(".classwork-home-cont").css("display", "flex") ;
            //
            //     document.getElementsByClassName('classroom-nav')[0].classList.remove('selected-classroom-nav') ;
            //     document.getElementsByClassName('classroom-nav')[1].classList.add('selected-classroom-nav') ;
            // }

            function classroomSwitch(i){
                let elem = document.getElementsByClassName('classroom-nav') ;
                $(".classroom-nav").removeClass("selected-classroom-nav") ;
                elem[i].classList.add('selected-classroom-nav') ;
                $(".forswitch").hide() ;

                if(i == 0){
                    $(".classroom-work-body").show() ;
                } else if(i == 1){
                    $(".classwork-works-cont").show() ;
                } else if(i == 2){
                    $(".classroom-student-cont").show() ;
                }
            }

            // classroomSwitch(1) ;

            document.addEventListener("click", () => {
                $(".menu-cont").hide() ;
            }) ;

            function openSendNotifCount(t, e, id){
                e.stopPropagation() ;
                $(".menu-cont").show() ;
                $(".menu-cont").css({
                    "top": $(t).offset().top - 20 + "px",
                    "left": $(t).offset().left - $(".menu-cont").width() + "px"
                }) ;
                $(".menu-cont a").attr("href", `/notifications/add?stu=${id}`) ;
            }


            document.getElementsByClassName('userShare-defult')[0].addEventListener("click", () => {
                $(".userShare-defult").hide() ;
                $(".userShare-cont").show() ;
                document.getElementById('userShareBody').focus() ;
            }) ;

  //document.getElementsByClassName('userShare-defult')[0].click() ;

            function closeuserShare() {
                $(".userShare-cont").hide() ;
                $(".userShare-defult").show() ;

                document.getElementById('userShareBody').innerHTML = "" ;
                document.getElementById('linkAttachments').innerHTML = "" ;
                document.getElementById('mediaAttachments').innerHTML = "" ;
            }

            document.getElementById('btnCancelUserShare').addEventListener("click", closeuserShare) ;

            function openAddLink() {
                $(".addLink-outter").show() ;
                $(".addLink-cont").show() ;
                document.getElementById('inpAddLink').focus() ;
            }

            document.getElementById('btnCloseAddLink').addEventListener("click", () => {
                $(".addLink-outter").hide() ;
                $(".addLink-cont").hide() ;
                document.getElementById('inpAddLink').value = "" ;
            }) ;


            document.getElementById('btnAddLink').addEventListener("click", function () {
                let link = document.getElementById('inpAddLink').value.trim() ;
                document.getElementById('linkAttachments').innerHTML += `<a href="${link}" target="_blank"><div class="media-items">
                                        <section class="media-image-cont">
                                                <img src='http://www.google.com/s2/favicons?domain=${link}' />
                                        </section>
                                        <section class="media-body-cont">
                                            <article>${link}</article>
                                            <article>Website</article>
                                        </section>
                                        <section  class="media-remove-cont"> <i class="fas fa-times" onclick="removeItem(this, event, '')"></i> </section>
                                    </div></a>` ;
                document.getElementById('btnCloseAddLink').click() ;
            }) ;




    function closeUploadFileUserShare() {
        $(".addAttachmentsCont").hide() ;
    }

    let fileInputNums = 0 ;
    function openUploadFileUserShare() {
        for(let i = 0; i < document.getElementById('addAttachments').children.length ; i++){
            document.getElementById('addAttachments').children[i].style.display = "none" ;
        }

        $("#addAttachments").append(`<article class="chooseFile-btn-cont"> <article>BROWSE</article><input type="file" id="userShareFile${fileInputNums}" name="userShare${fileInputNums}" onchange="fileSelected(event, ${fileInputNums})"></article>`) ;
        fileInputNums++ ;
        $(".addAttachmentsCont").show() ;
    }

    function fileSelected(e, id) {
        let fileName = e.target.files[0].name ;
        let fileType = getFileType(fileName) ;

        document.getElementById('mediaAttachments').innerHTML += `<div class="media-items">
                                        <section class="media-image-cont">
                                                <i class="fas fa-file-alt"></i>
                                        </section>
                                        <section class="media-body-cont">
                                            <article>${fileName}</article>
                                            <article>${fileType}</article>
                                        </section>
                                        <section  class="media-remove-cont"> <i class="fas fa-times" onclick="removeItem(this, event, ${id})"></i> </section>
                                    </div>` ;

        closeUploadFileUserShare()
    }


            function openClassroomMediaItems(t){
                if( $(t).attr("data-mediaOpen") == "false" ){
                    $(t).parent().next().next().css({
                        "height":"fit-content"
                    }) ;
                    $(t).css({
                        "transform":"rotate(180deg)"
                    }) ;
                    $(t).attr("data-mediaOpen", "true") ;
                } else {
                    $(t).parent().next().next().css({
                        "height":"0px"
                    }) ;
                    $(t).css({
                        "transform":"rotate(0deg)"
                    }) ;
                    $(t).attr("data-mediaOpen", "false") ;
                }
            }


            function removeItem(t, e, id) {
                e.preventDefault() ;
                $(t).parent().parent().remove() ;
                if(id != ""){
                    document.getElementById(`userShareFile${id}`).remove() ;
                }
            }


            $("#userShareForm").on("submit", function (e) {
                e.preventDefault() ;

                console.log(document.getElementById('userShareBody').innerHTML) ;

                document.getElementById('userShareBodyCopy').value = document.getElementById('userShareBody').innerHTML ;

                let links = [] ;

                if(document.getElementById('linkAttachments').children.length > 0){
                    for(let i = 0; i < document.getElementById('linkAttachments').children.length; i++){
                        links.push(document.getElementById('linkAttachments').children[i].getAttribute('href')) ;
                    }
                    document.getElementById('userShareBodyCopy').value += "stali" + JSON.stringify(links) + "endli" ;
                }


                function  closeUploadingCont() {
                    $(".classroom-loading-cont").animate({
                        "padding": "0 20px",
                        "height": "0px",
                    }, 200, function () {
                        $(".classroom-loading-cont").hide() ;
                    }) ;
                }

                function openUploadingCont(){

                    document.getElementById('loadinPercentage').innerText = '0%' ;

                    $(".classroom-loading-before").show() ;
                    $(".classroom-loading-after").hide() ;

                    $(".classroom-loading-bar").css({
                        "width": "0%"
                    }) ;

                    $(".classroom-loading-cont").show() ;
                    $(".classroom-loading-cont").css({
                        "height": "fit-content",
                        "padding":"20px 20px"
                    }) ;
                }




                if(document.getElementById('userShareBodyCopy').value.trim() != ""){
                    openUploadingCont() ;
                    $.ajax({
                        cache: false,
                        type: "POST",
                        url: "/classroom/usershare",
                        data: new FormData(this),
                        contentType:false,
                        processData:false,
                        xhr: function () {
                            var xhr = new window.XMLHttpRequest();
                            xhr.upload.addEventListener("progress", (evt) => {
                                if (evt.lengthComputable) {
                                var percentComplete = Math.round((evt.loaded / evt.total) * 100) ;
                                document.getElementById('loadinPercentage').innerText = percentComplete + '%' ;
                                $(".classroom-loading-bar").css({
                                    "width": percentComplete + "%"
                                }) ;
                                 console.log(percentComplete)
                            }
                        }, false);
                            return xhr;
                        },
                        success: function (result) {
                            console.log(result) ;
                            try{
                                let data = JSON.parse(resJson(result))[0] ;
                                if(data == "s"){
                                    $(".classroom-loading-before").hide() ;
                                    $(".classroom-loading-after").show() ;
                                    setTimeout(function () {
                                        closeUploadingCont() ;
                                        closeuserShare() ;
                                        showLineMsg("Your post have been uploaded", "po") ;
                                    }, 500) ;
                                }
                            } catch (e) {
                                console.log(e) ;
                                showLineMsg("Something wend wrong, Please try again later", "ne") ;
                                closeUploadingCont() ;
                            }
                        },
                        error: function (jqXHR, exception, responseText) {
                            closeUploadingCont() ;
                            console.log(jqXHR, exception, responseText) ;
                        }
                    }) ;
                }
            }) ;
