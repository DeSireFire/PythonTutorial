db.t2.find({})
db.t1.find({})
db.t1.find({age:20})
db.t1.find({age:{$gte:20}})
db.t1.findOne({age:{$gt:20}})
db.t2.find({}).pretty()
db.t1.find({
     age:{$gte:20},
     sex:1
});
db.t1.find({
     $or:[{age:{$gte:20}},{sex:1}]
});
select * from t1 where (age>=20 or sex=1) and name='a'
db.t1.find({
     $or:[{age:{$gte:20}},{sex:1}],
     name:'a'
});

select * from t1 where age in(20,30,40)
db.t1.find({
   age:{$in:[20,30,40]}     
})

db.t1.insert({name:'abc'})


db.t1.find({
     name:/^a/
})
db.t1.find({
     name:/.*b.*/
})
db.t1.find({
     age:{$gt:20}
})
db.t1.find({
     $where:function(){return this.age>20}
})

db.t1.find({
     $where:function(){return this.name.indexOf('b')!=-1}
})

for(i=0;i<10;i++){
     db.t1.insert({'name':'name'+i,sex:0,age:i})
}

db.t1.find({})
db.t1.find({}).limit(3).skip(2)

db.t1.find({},{_id:1,name:1})
db.t1.find({},{age:0,sex:0})

db.t1.find({}).sort({age:-1})
db.t1.find({},{sex:0}).sort({age:-1})

db.t1.find({sex:1}).count()
db.t1.count({sex:1})

db.t1.find({age:{$gt:5}})
db.t1.distinct('sex')
db.t1.distinct('sex',{age:{$gt:5}})

