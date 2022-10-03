
for (var i = 0; i < document.getElementsByClassName('student-nav-cont')[0].children.length; i++){
    document.getElementsByClassName('student-nav-cont')[0].children[i].children[0].classList.remove('selectedNav') ;
}

document.getElementsByClassName('student-nav-cont')[0].children[2].children[0].classList.add('selectedNav') ;


    function getInternals() {
    console.log(0) ;
        const sem = document.getElementById('sem').value ;
        if(sem){
            $.ajax({
                cache:false,
                type:"POST",
                url:"/internals/getinternalsforstudents",
                data:{csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
                    sem: sem
                },
                success:function(result){
                    console.log(result) ;
                    let data = JSON.parse(result) ;
                    document.getElementById('internals').innerHTML = "";
                    if(data.length > 0) {

                        console.log(data);
                        for (let i = 0; i < data.length; i++) {
                            document.getElementById('internals').innerHTML += `<header class="internal-name">${data[i].exam_name}</header>
                            <header class="internal-table-head">
                                <article>Subject code</article>
                                <article>Subject </article>
                                <article>Your mark</article>
                                <article>Total mark</article>
                                <article>Date</article>
                            </header>
                            <div class="internalMarkList" id="internalMarkList${i}"></div>`;
                        }

                        for (let i = 0; i < data.length; i++) {
                            for (let sub = 0; sub < data[i]['sub'].length; sub++) {
                                document.getElementById(`internalMarkList${i}`).innerHTML += `<section class="internal-mark-list">
                                    <article>${data[i]['sub'][sub]['code']}</article>
                                    <article>${data[i]['sub'][sub]['name']}</article>
                                    <article>${data[i]['sub'][sub]['mark']}</article>
                                    <article>${data[i]['sub'][sub]['total']}</article>
                                    <article>${data[i]['sub'][sub]['date']}</article>
                                </section>`;
                            }
                        }
                    }
                },
                error:function(jqXHR, exception, responseText){
                    console.log(jqXHR) ;
                    console.log(exception) ;
                    console.log(responseText) ;
                }
            }) ;
        }
    }
