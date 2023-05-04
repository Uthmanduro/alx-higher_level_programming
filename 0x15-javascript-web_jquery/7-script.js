$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (res) {
        $('DIV#character').html(res.name);
    }
});
