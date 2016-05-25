$(function(){
    var ret = $("#btn1").click(function(){
        $("#div1").fadeToggle()
    });
    console.log(ret)
    console.log($("#btn1"))

    $("#div1").mouseenter(function(){
        $(this).toggleClass("c1")
    }).mouseout(function(){
        $(this).toggleClass("c1")
    });

    $("#btn2").click(function(){
        //console.log($("#div1").css("color","red").siblings())
        $("#div1").css("color","red").siblings().find("input").val('xx')
    });
})
