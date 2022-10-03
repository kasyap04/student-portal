

function dateChange(t) {
    console.log(t.value) ;
    location.href = '/attendence/students?dep=1&sem=1&date=' + t.value ;
}