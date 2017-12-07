$(document).ready(function () {
    $('.user_change').change(function () {
        current_select = $(this);
        $.ajax({
            type: "POST",
            url: '/admin_request',
            data: {
                type: 'user_change',
                user: $(this).attr('data-email'),
                usergroup: this.value
            }
        }).done(function () {
            current_select.next('.notify-user-update').fadeIn(350).fadeOut(1500);
        }).fail(function (data) {
            data = JSON.parse(data.responseText);
            alert(data.error);
        })
    });
    $('.request_change').change(function () {
        current_select = $(this);
        $.ajax({
            type: "POST",
            url: '/admin_request',
            data: {
                type: 'request_change',
                user: $(this).attr('data-email'),
                status: this.value,
                date: $(this).attr('data-date')
            }
        }).done(function () {
            current_select.next('.notify-request-update').fadeIn(350).fadeOut(1500);
        }).fail(function (data) {
            data = JSON.parse(data.responseText);
            alert(data.error);
        })
    });
});