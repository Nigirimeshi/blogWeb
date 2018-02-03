/**
 * 1.0 导航栏切换效果
 * 2.0 表格加样式
 * 3.0 动态设定页面最小高度
 * 4.0 回到顶部按钮
 * 5.0 目录可视区浮动
 *
 **/

$(function () {

    /**
     * 1.0 导航栏切换效果
     **/
    $('.navbar-nav li a').click(function () {
        $(this).addClass('navbar-active-a')
            .parents('li').siblings('li').children('a').removeClass('navbar-active-a');
    });


    /**
     * 2.0 表格加样式
     **/
    $('table').addClass('table table-hover');


    /**
     * 3.0 动态设定页面最小高度
     **/
    var win_height = $(window).height();
    var content_height = win_height - 72 - 165;
    $('.min-height').css({'min-height': content_height});


    /**
     * 4.0 回到顶部按钮
     **/
    var $back_top_btn = $('#back-to-top');

    $back_top_btn.click(function () {
        $('html,body').animate({scrollTop: 0}, 500);
    });

    $(window).scroll(function () {
        if ($(window).scrollTop() >= win_height) {
            $back_top_btn.fadeIn();
        }
        else {
            $back_top_btn.fadeOut();
        }
    });


    /**
     * 5.0 目录可视区浮动
     **/
    // var $toc = $('#toc');
    //
    // $(window).scroll(function () {
    //     if ($(window).scrollTo() >= win_height) {
    //         $toc.css({''})
    //     }
    //
    // })

});