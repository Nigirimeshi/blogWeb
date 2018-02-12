/**
 * 1.0 input 表单切换效果
 * 2.0 倒计时返回首页 - password_reset_done.html
 *
 *
**/


$(function () {
    /**
     * 1.0 input 表单切换效果
    **/
    var $input = $('.form-group input');

    $input.addClass('form-control');

    $input.focus(function () {
        $(this).addClass('active').parent('div').siblings('div').children('input').removeClass('active');
    });


    /**
     * 2.0 倒计时返回首页 - password_reset_done.html
    **/

});