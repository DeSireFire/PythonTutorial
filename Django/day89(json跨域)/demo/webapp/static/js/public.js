/**
 * Created by yong on 17-9-29.
 */
function myajax(url,func,method='GET',params=null) {
    //获取XMLHttpRequest对象

    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest()
    } else {
        xmlhttp = new ActiveXObject()
    }
    //onreadystatechange 事件
    xmlhttp.onreadystatechange = func;
    //open
    xmlhttp.open(method, url, true);
    //send
    xmlhttp.send(params);
};


String.prototype.trim = function() {
    return this.replace(/(^\s*)|(\s*$)/g,'')
}

Array.bubble = function(){
    //作业
}