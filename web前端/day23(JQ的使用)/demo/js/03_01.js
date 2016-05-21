var tom = {
    name : 'tom',
    age : 18,
    showname : function(){
        alert('我的名字叫'+this.name);
    },
    showage : function(){
        alert('我今年'+this.age+'岁');
    }
}
//console.log(tom['name'])
console.log(tom.name)
tom.showage()
tom.showname()

