document.addEventListener('DOMContentLoaded', () => {
      $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
        $('DIV#hello').text(data.hello);
      });
    });