$(document).ready(function() {
    $('#uploadBtn').click(function(e) {
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
                    window.location.reload();
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