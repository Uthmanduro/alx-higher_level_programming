$(document).ready( () => {
    $.ajax({
        url: 'https://fourtonfish.com/hellosalut/?lang=fr',
        success: (response) => {
            $('DIV#hello').html(response.hello);
        }
    });
});
