document.addEventListener('DOMContentLoaded', function() {
$('#btn_translate').click(function() {
    // Get the language code entered by the user
    var languageCode = $('#language_code').val();

    // Make the API request to fetch the translation
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode,
      dataType: 'json',
      success: function(data) {
        // Check if the API response contains the translation
        if (data.hello) {
          // Display the translation in the HTML element with ID "hello"
          $('#hello').text(data.hello);
        } else {
          // Handle the case when the translation is not available
          $('#hello').text('Translation not found.');
        }
      },
      error: function() {
        // Handle any errors that might occur during the API call
        $('#hello').text('Error fetching translation.');
      }
    });
  });
});
