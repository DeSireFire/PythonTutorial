/*
$(this)是jquery对象
this是js对象

js对象   转    jquery对象     $(js对象)
jquery对象   转    js对象     jquery对象.get(0)    jquery对象[0]
*/

$(function(){
    $("#btn1").click(function(){
        var width = $("#div1").css('width');
        width = parseInt(width)+50;
        //$("#div1").css('width',width);
        $("#div1").css({"width":width,"backgroundColor":"red"});
    });
    $("#btn2").click(function(){
        var width = $("#div1").css('width');
        width = parseInt(width)-50;
        $("#div1").css('width',width);
    });
   /* $("#div1").mousemove(function(){
        $(this).css({"border":"solid 1px red"});
    }).mouseout(function(){
        $(this).css({"border":"none"});
    });*/
/*    $("#div1").mousemove(function(){
        $(this).addClass("c1")
    }).mouseout(function(){
        $(this).removeClass("c1")
    });*/
    $("#div1").mouseenter(function(){
        $(this).toggleClass("c1")
    }).mouseout(function(){
        $(this).toggleClass("c1")
    });
})