$(document).ready(function() {
    $('#submitBtn').click(function(e) {
        // Stop form from submitting normally
        e.preventDefault();

        $.ajax({
            url: window.location.href,
            type: 'POST',
            data: {
                username: $('#inputUsername').val(),
                password: $('#inputPassword').val()
            },
            success: function(data) {
                if (data.code == '200') {
                    // TODO
                    // 注册成功后的处理逻辑
                } else {
                    alert(data['msg']);
                }
            },
            error: function(data) {
                alert('internal error');
            },
            dataType: 'json',
        });
    });
});