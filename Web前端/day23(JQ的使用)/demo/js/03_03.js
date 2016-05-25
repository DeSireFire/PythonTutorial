function Person(name,age,job){
    this.name = name;
    this.age = age;
    this.job = job;
    this.showname = function(){
        alert('我的名字叫'+this.name);
    };
    this.showage = function(){
        alert('我今年'+this.age+'岁');
    };
    this.showjob = function(){
        alert('我的工作是'+this.job);
    };
}

laowang = new Person('老王',18,'隔壁')
laowang.showname()
console.log(Person)

Person.num = 100
console.log(Person.num)
console.log(laowang.num)

laowang.a = 'a'
console.log(laowang.a)