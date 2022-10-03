    $(".goback").click(function () {
        window.history.back() ;
    }) ;

    function openUploadFile(){
        $(".classwork-work-form").show() ;
    }

     function closeUploadFile() {
        $(".classwork-work-form").hide() ;
    }


let fileIds = 0 ;
    function createAttchmentButton() {
        for (let i = 0; i < document.getElementById('attachmentCont').children.length; i++){
            document.getElementById('attachmentCont').children[i].style.display = "none" ;
        }

        fileIds ++ ;
        $("#attachmentCont").append(`<article class="chooseFile-btn-cont"> <article>BROWSE</article><input type="file" id="submitFile${fileIds}" name="submitFile${fileIds}" onchange="fileSelected(event)"></article>`) ;

        openUploadFile() ;
    }


    // document.getElementById('adddFileBtn').addEventListener("click", createAttchmentButton) ;

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
    
    function feildIsEmpty() {
        if (document.getElementById('displaySelectedFile').children.length > 0){
            $(".classwork-work-labels").hide() ;
            document.getElementById('classworkSubmitBtn').removeAttribute('disabled') ;
            document.getElementById('classworkSubmitBtn').classList.remove('disbled')
        } else{
            document.getElementById('classworkSubmitBtn').setAttribute('disabled', 'disabled') ;
            document.getElementById('classworkSubmitBtn').classList.add('disbled')
            $(".classwork-work-labels").show() ;
        }
    }

    function fileSelected(e){
        let fileName = e.target.files[0].name ;
        let fileType = getFileType(fileName) ;

        document.getElementById('displaySelectedFile').innerHTML += `<section class="select-file">
                                    <article class="select-file-icon"><i class="fas fa-file-alt"></i></article>
                                    <article class="select-file-name">
                                        <span>${fileName}</span>
                                        <span>${ fileType }</span>
                                    </article>
                                    <article class="select-file-remove"> <i class="fas fa-times" onclick="removeSelectedFile(${fileIds}, this)"></i> </article>
                                </section>` ;

        closeUploadFile() ;
        feildIsEmpty() ;
    }

    function removeSelectedFile(id, t){
        $(t).parent().parent().remove()
        document.getElementById(`submitFile${id}`).remove() ;
        feildIsEmpty() ;
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


    $("#submitWorkForm").on("submit", function (e) {
        e.preventDefault() ;

        let canSubmit = true ;
        const fileElem = document.getElementById('attachmentCont') ;
        for(let i = 0; i < fileElem.children.length - 1; i++){
            if(fileElem.children[i].value == ""){
                canSubmit = false ;
                break ;
            }
        }

        let workid = document.getElementById('workid').value ;

      //  fileElem.children[fileElem.children.length-1].remove() ;



        if(canSubmit){
            openUploadingCont() ;
            $.ajax({
                cache: false,
                type: "POST",
                url: "",
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
                                showLineMsg("Handed in successfully", "po") ;
                                document.getElementById('classWorkBtnCont').innerHTML = '<button onclick="openUnsubmitCount('+ workid +', this); return false;" class="work-handin-btn">Unsubmit</button>' ;
                                }, 500) ;

                        } else if(data == "mnf"){
                            closeUploadingCont() ;
                            showLineMsg("File is missing, Please select file to upload", "ne") ;
                        }
                    } catch (e) {
                        console.log(e) ;
                        closeUploadingCont() ;
                        showLineMsg("Something wend wrong, Please refresh and try again", "ne") ;
                    }
                },
                error: function (jqXHR, exception, responseText) {
                    closeUploadingCont() ;
                    console.log(jqXHR, exception, responseText) ;
                }
            }) ;
        }
    }) ;


    function closeUnsubmitCont() {
        $(".unsubmit-outer").hide() ;
    }

    function openUnsubmitCount(id) {
        document.getElementById('unsubmitBtnYes').setAttribute('data-workid', id) ;
        $(".unsubmit-outer").show() ;
    }


    function unsubmitWork(t) {
        let id = t.getAttribute('data-workid') ;
        if(id != ""){
            $.ajax({
                cache: false,
                type: "POST",
                url: "undoclasswork",
                data: {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), workid: id },
                success: function (result) {
                    console.log(result) ;
                    try {
                        let data = JSON.parse(resJson(result))[0] ;
                        if(data == "s"){
                            showLineMsg("Work unsubmited successfully", "po") ;
                            setTimeout(function () {
                                location.reload() ;
                            }, 1000) ;
                        }
                    }catch (e) {
                        console.log(e) ;
                        showLineMsg("Something wend wrong, Please refresh and try again", "ne") ;
                    }
                },
                error: function (jqXHR, exception, responseText) {
                    console.log(jqXHR, exception, responseText) ;
                }
            }) ;
        } else
            showLineMsg("Something wend wrong, Please refresh and try again", "ne") ;
    }