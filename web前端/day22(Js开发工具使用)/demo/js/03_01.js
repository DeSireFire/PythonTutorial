function  showTime(){
    now = new Date()
    //alert(now)
    console.log(now)
    console.log(now.getYear()+1900)
    console.log(now.getFullYear())
    document.getElementById("time").innerHTML = now
}