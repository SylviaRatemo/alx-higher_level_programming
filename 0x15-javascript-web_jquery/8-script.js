$.ajax({
      url: "https://swapi-api.alx-tools.com/api/films/?format=json",
      method: "GET",
      dataType: "json",
      success: function(data) {
        // Extract the movie title from the API response
        var movies = data.results;
        var movieList = '';

        $.each(movies, function(index, movie) {
          movieList += '<li>'+ movie.title +'</li>';
          });
        $("#list_movies").html(movieList);
      },
      error: function() {
        // Handle any errors that might occur during the API call
        $("#list_movies").text("Error fetching movie names.");
      }
    });
