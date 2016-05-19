var names = ['小沈阳','赵四','刘能','宋小宝'];
for(var temp in names){
    console.info(names[temp]);
}
for(var i=0;i<names.length;i++){
    console.info(names[i]);
}
i=0
while(i<names.length){
    console.info(names[i]);
    i++;
}

var aList = [1,2,3,4,4,3,2,1,2,3,4,5,6,5,5,3,3,4,2,1];

var aList2 = [];

for(var i=0;i<aList.length;i++) {
    if(aList.indexOf(aList[i])==i) {
        aList2.push(aList[i]);
    }
}

alert(aList2);
