function fclass(name,age){
    this.name = name;
    this.age = age;
}
fclass.prototype.showname = function(){
    alert(this.name);
}
fclass.prototype.showage = function(){
    alert(this.age);
}


zclass.prototype = new fclass();

function zclass(name,age,job){
    fclass.call(this,name,age)
    this.job = job;
}

laowang = new zclass('老王',18,'隔壁')
console.log(laowang.name)
console.log(laowang.age)
console.log(laowang.job)
laowang.showname()