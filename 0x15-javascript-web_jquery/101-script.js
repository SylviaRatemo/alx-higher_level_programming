document.addEventListener('DOMContentLoaded', function() {
      $('DIV#add_item').click(function() {
        // Create a new <li> element with the text "Item"
        var newItem = $('<li>Item</li>');
        // Append the new <li> element to the UL with class "my_list"
        $('ul.my_list').append(newItem);
      });

      $('DIV#remove_item').click(function() {
        // Remove the last <li> element from the UL with class "my_list"
        $('ul.my_list li:last-child').remove();
      });

      $('DIV#clear_list').click(function() {
        // Remove all <li> elements from the UL with class "my_list"
        $('ul.my_list').empty();
      });
    });
