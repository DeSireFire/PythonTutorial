function add(a,b){
    var c = a + b;
    return c;
    alert('here!');
}

console.log(add(1,2))

function f1(){
    console.log('1..')
    return;
    console.log('2..')
}
console.log(f1());

function getId(id){
    return document.getElementById(id)
}
window.onload = function() {
    alert('1...')
    getId("btn1").onclick = function () {
        alert('btn1...')
    }
}