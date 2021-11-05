function scrollUp() {
    const vheight = $('.test').height();
    $('html, body').animate({
        //윈도우 높이만큼 스크롤업, -1의 값을 준 이유 : 아래에서 위로 이동하기 때문
        scrollTop: ((Math.floor($(window).scrollTop() / vheight)-1) * vheight)
    }, 500);
}
function scrollDown() {
    const vheight = $('.test').height();
    $('html, body').animate({
        scrollTop: ((Math.floor($(window).scrollTop() / vheight)+1) * vheight)
    }, 500);
}

$(function(){
    //next_btn을 눌렀을때, 스크롤 다운
    $('.next_btn').click(function(e){
        e.preventDefault();
        scrollDown();
    });
    //prev_btn을 눌렀을때, 스크롤 업
    $('.prev_btn').click(function(e){
        e.preventDefault();
        scrollUp();
    });
});