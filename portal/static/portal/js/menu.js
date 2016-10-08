'use strict';

$(function () {
    highlightMenuOption();
});

// Highlight the main menu option that corresponds to the current URI.
function highlightMenuOption() {
    var path = window.location.pathname;
    path = path.replace(/\/$/, "");
    path = decodeURIComponent(path) + '/';  // django adds the '/' to href

    $("#mainmenu a").each(function () {
        var href = $(this).attr('href');
        var uri = path.substring(0, href.length);
        if (uri === href) {
            $(this).closest('li').addClass('care-menu-selected');
            $(this).addClass('care-menu-selected-text');
        }
    });
}

// Update the display of the user's name in the user's menu.
function updateUserMenu(user) {
    $('a#usermenu').text(user.first_name + ' ' + user.last_name);
}
