$(function(){
    $("#go").click(function(){
        $("#block1").animate({
            width: "90%",
            height: "100%",
            fontSize: "10em",
            borderWidth: 10,
            opacity: 'toggle'
        }, 3000 );
    })
    $("#left").click(function(){
        $("#block2").animate({left: '-=50px'}, "slow");
    });
    $("#right").click(function(){
        $("#block2").animate({left: '+=50px'}, "slow");
    });
    $("#stop").click(function(){
        //停止所有动画
        $("#block2").stop(true);
        //停止当前这一次没有完成的动画，如果队列里还有动画，会进行下一次动画
        //$("#block2").stop();
    });
})
