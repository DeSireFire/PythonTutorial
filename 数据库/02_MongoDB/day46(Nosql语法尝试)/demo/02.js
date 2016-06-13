show collections

db.t8.insert({name:'laowang',age:1})

db.t8.getIndexes()

for(i=0;i<10000;i++){
    
    db.t9.insert({'name':'laowang'+i,num:i})
}

db.t9.find({name:'laowang8888'})

db.t9.find({name:'laowang8888'}).explain('allPlansExecution')
db.t9.find({name:'laowang8888'}).explain('executionStats')
db.t9.find({_id:'234234'}).explain('executionStats')
db.t9.ensureIndex({'name':1,num:-1})

db.t9.find({name:'laowang555',num:555}).explain('executionStats')


db.t9.getIndexes()


db.t9.dropIndex({'name':1,num:-1})