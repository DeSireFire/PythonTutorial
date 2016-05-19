var  array1 = [1,'a',true,null,undefined,[1,2,3]]
console.log(array1)
console.log(array1.length)
console.log(array1[5][1])


var  array2 = new Array(1,'a',true,null,undefined,[1,2,3])
console.log(array2)

var  array3 = new Array(3,1)
console.log(array3)
console.log(array3[100])


var arr = new Array(3)
arr[0] = "George"
arr[1] = "John"
arr[2] = "Thomas"
arr[3] = "老王"

//document.write(arr.join())
console.log(arr.join())

window.onload = function(){
    divs = document.getElementsByTagName('div')
    console.log(divs)
}
