function getId(id){
    return document.getElementById(id)
}
function getTagId(tag){
    return document.getElementsByTagName(tag)
}
function getByClass(className){
    return document.getElementsByClassName(className)
}
window.onload = function(){
    getId("checkAll").onclick = function(obj){
        var checked = obj.target.checked
        lis = getByClass('c1')
        for(var i in lis){
            lis[i].checked = checked
        }
    }
}