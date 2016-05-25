function getId(id){
    return document.getElementById(id)
}

function changImg(){
    getId("myImg").src="./images/东北F4.jpg"
};

function changImg2(obj){
    console.log(obj)
    console.log(obj.value)

};
/*
事件：
    1、绑定功能
    2、触发事件，执行功能
*/

window.onload = function(){
    alert('1...')
    getId("btn1").onclick = function(){
        alert('btn1...')
    }
    getId("btn2").onclick = function(obj){
        console.log(obj)
        console.log(obj.target.value)
        console.log(obj.target.localName)
    }
}

function myalert(a){
    alert(a);
}
myalert('2...');


