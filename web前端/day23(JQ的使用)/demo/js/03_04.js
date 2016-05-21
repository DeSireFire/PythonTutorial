function Person(name,age,job){
    this.name = name;
    this.age = age;
    this.job = job;
}
Person.prototype.showname = function(){
    alert('我的名字叫'+this.name);
};
Person.prototype.showage = function(){
    alert('我今年'+this.age+'岁');
};
Person.prototype.showjob = function(){
    alert('我的工作是'+this.job);
};


laowang = new Person('老王',18,'隔壁')
laowang.showname()
console.log(Person)

Person.prototype.num = 100;
console.log(Person.prototype.num)
console.log(laowang.num)

laowang.a = 'a'
console.log(laowang.a)



String.prototype.capitalize = function(){
    console.log('this:'+this)
    return this[0].toUpperCase()+this.slice(1,this.length);
}

var name = 'laowang';
alert(name.capitalize())
/*
prototype可以为类创建实例属性
*/
