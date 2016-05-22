    function check_userName(){
        var flag = true;
        var firstname = document.getElementById("firstname").value;
        console.log("firstname:"+firstname)
        if (firstname.length==0){
            document.getElementById("firstname_erro").innerHTML= "用户名必填";
            flag = false;
        }else if(firstname.length<6){
            document.getElementById("firstname_erro").innerHTML= "用户名长度至少是6";
            flag = false;
        }else{
            document.getElementById("firstname_erro").innerHTML="";
        }
        return flag;
    }
/*function check_userPwd(){

 }*/

window.onload = function(){
        document.getElementById("signupForm").onsubmit = function(){
            /*if(!(check_userName() && function check_userPwd() &&xx())){
             return false
             }*/
            if(!(check_userName())){
                return false;
            }
        }
    }
