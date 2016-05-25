var a = 2;
if(a==1){
    alert('语文');
}
else if(a==2){
    alert('数学');
}
else if(a==3){
    alert('英语');
}
else if(a==4){
    alert('美术');
}
else if(a==5){
    alert('舞蹈');
}
else{
    alert('不补习');
}

switch(a){
    case 1:
        alert('语文');
        break;
    case 2:
        alert('数学');
        break;
    case 3:
        alert('外语');
        break;
    default:
        alert('xx');
        break;
}
