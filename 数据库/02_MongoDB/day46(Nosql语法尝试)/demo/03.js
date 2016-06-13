use admin

db.createUser({
    user:'laowang',
    pwd:'123456',
    roles:[{role:'root',db:'admin'}]
})
sudo /usr/local/mongodb/bin/mongo -u laowang -p 123456 --authenticationDatabase admin


use d1
db.createUser({
    user:'d1',
    pwd:'123456',
    roles:[{role:'read',db:'d1'}]
});
use d2
db.createUser({
    user:'d2',
    pwd:'123456',
    roles:[{role:'readWrite',db:'d2'}]
});
sudo /usr/local/mongodb/bin/mongo -u d1 -p 123456 --authenticationDatabase d1
sudo /usr/local/mongodb/bin/mongo -u d1 -p 123456 --authenticationDatabase d1


db.system.users.find()
db.system.users.remove({user:'d1'})
db.system.users.remove({user:'d2'})