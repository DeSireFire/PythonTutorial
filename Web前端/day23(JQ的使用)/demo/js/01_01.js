/*
Window 对象
所有浏览器都支持 window 对象。它表示浏览器窗口。
所有 JavaScript 全局对象、函数以及变量均自动成为 window 对象的成员。
全局变量是 window 对象的属性。
全局函数是 window 对象的方法。
*/


function  f1() {
    var w = window.innerWidth
        || document.documentElement.clientWidth
        || document.body.clientWidth;

    var h = window.innerHeight
        || document.documentElement.clientHeight
        || document.body.clientHeight;

    x = document.getElementById("demo");
    x.innerHTML = "浏览器的内部窗口宽度：" + w + "，高度：" + h + "。"
}

window.onload = function(){
    console.log(window)
    f1()
}

function open_win() {
    /*window.open("http://www.w3school.com.cn")*/
    window.open("http://www.w3school.com.cn","_blank","toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=no, resizable=no, copyhistory=yes, width=400, height=400")
}
function closeWin() {
    window.close()
}
function CloseWebPage(){
    if (navigator.userAgent.indexOf("MSIE") > 0) {
        if (navigator.userAgent.indexOf("MSIE 6.0") > 0) {
            window.opener = null;
            window.close();
        } else {
            window.open('', '_top');
            window.top.close();
        }
    }
    else if (navigator.userAgent.indexOf("Firefox") > 0) {
        window.location.href = 'about:blank ';
    } else {
        window.opener = null;
        window.open('', '_self', '');
        window.close();
    }
}
function btn1(){
   /* window.location.href = "http://www.baidu.com";*/
    /*alert(location.search)*/
    alert(navigator.userAgent)
}