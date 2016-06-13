db.student.insert({name:'a',sex:1,age:20})
db.student.insert({name:'b',sex:0,age:21})
db.student.insert({name:'c',sex:1,age:22})
db.student.insert({name:'d',sex:0,age:23})
db.student.insert({name:'e',sex:1,age:24})
db.student.insert({name:'f',sex:1,age:25})

db.student.find()

db.student.aggregate([
    {
        $group:{
             _id:'$sex',
             num:{$sum:1}
        }
    }
])






    
db.student.aggregate([
    {$group:{_id:'$sex',num:{$sum:1},avgage:{$avg:'$age'}}}
])
db.student.aggregate([
    {$group:{_id:null,num:{$sum:1},avgage:{$avg:'$age'}}}
])

db.student.aggregate([
    {$group:{_id:'$sex',num:{$sum:1},names:{$push:'$name'}}}
])    
    
db.student.aggregate([
    {$group:{_id:'$sex',num:{$sum:1},names:{$push:'$$ROOT'}}}
])   



db.student.find({age:{$gt:20}})

db.student.aggregate([
    {$match:{age:{$gt:20}}},
    {$group:{_id:'$sex',num:{$sum:1}}}
]) 


db.student.find({age:{$gt:20}},{_id:0,name:1,age:1})


db.student.aggregate([
    {$match:{age:{$gt:20}}},
    {$group:{_id:'$sex',num:{$sum:1}}},
    {$project:{_id:0}}
])


db.student.find().sort({age:-1})



db.student.aggregate([
    {$match:{age:{$gt:20}}},
    {$group:{_id:'$sex',num:{$sum:1}}},
    {$project:{_id:0}},
    {$sort:{num:1}}
])


db.student.find().skip(2).limit(1)
    
db.student.aggregate([
    {$match:{age:{$gt:20}}},
    {$group:{_id:'$sex',num:{$sum:1}}},
    {$project:{_id:0}},
    {$sort:{num:1}},
    {$skip:1},
    {$limit:10}
])
    
    
db.t4.insert([
{ "_id" : 1, "item" : "a", "size": [ "S", "M", "L"] },
{ "_id" : 2, "item" : "b", "size" : [ ] },
{ "_id" : 3, "item" : "c", "size": "M" },
{ "_id" : 4, "item" : "d" },
{ "_id" : 5, "item" : "e", "size" : null }
])

db.t4.find()
    
db.t3.insert({"item" : "a", "size": [ "S", "M", "L"] })

db.t3.find()


db.t3.aggregate([
    {$unwind:'$size'}
])
db.t4.aggregate([
    {$unwind:'$size'}
])
db.t4.aggregate([
    {$unwind:{path:'$size',preserveNullAndEmptyArrays:true}}
])

