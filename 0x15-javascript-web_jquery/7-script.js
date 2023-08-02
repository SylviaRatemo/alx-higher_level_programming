$.ajax({
      url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
      method: "GET",
      dataType: "json",
      success: function(data) {
        // Extract the character name from the API response
        var characterName = data.name;

        // Display the character name in the HTML tag with ID "character"
        $("#character").text(characterName);
      },
      error: function() {
        // Handle any errors that might occur during the API call
        $("#character").text("Error fetching character name.");
      }
    });
