$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: (response) => {
        $.each(response.results, (index, titles) => {
            $('UL#list_movies').append('<li>' + titles.title + '</li>');
        });
    }
});
