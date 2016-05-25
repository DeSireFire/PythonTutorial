var num = 10/3;
console.log(num);
console.log(parseInt(3.56))

var a = 10;
a++;  // a=a+1
console.log(a);


var b = 1
c = b++
console.log(b);
console.log(c);


var b = 1
c = ++b
console.log(b);
console.log(c);


console.log(undefined==false)
console.log(null==false)
console.log(''==false)
console.log(0==false)
console.log('5'==5)
console.log('5'===5)

if (0){
    console.log('if...')
}else{
    console.log('else...')
}


if (!true){
    console.log('if...')
}else{
    console.log('else...')
}
var year = 2008
if ((year%400==0)||(year%4==0 && year%100!=0)){
    console.log('if...')
}else{
    console.log('else...')
}