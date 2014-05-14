$("document").ready(function(){
    console.log("taco");
    $('body').each(function(){$(this).css("background",Math.floor(Math.random()*16777215).toString(16))})
    $('#p1').val($(".char-1").val())
    $('#p2').val($(".char-2").val())

    $(".char-1").click(function(){
        $('#p1').val($(this).val())
        console.log($(this).val())
    });
    $(".char-2").click(function(){
        $('#p2').val($(this).val())
    });
});
