function Person(name,age,job){
    var o = new Object();
    o.name = name;
    o.age = age;
    o.job = job;
    o.showname = function(){
        alert('我的名字叫'+this.name);
    };
    o.showage = function(){
        alert('我今年'+this.age+'岁');
    };
    o.showjob = function(){
        alert('我的工作是'+this.job);
    };
    return o;
}

laowang = Person('老王',18,'隔壁')
laowang.showname()