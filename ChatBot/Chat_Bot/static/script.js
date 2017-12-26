$(document).ready(function() {
  $('button').click(function() {
    var message = $("#inputMessage").val();
    console.log(message);
    $('.Chat').append("<div class='userMessage'>" + message + "</div>");
    $('#inputMessage').val("");
    $.ajax({
        type: "POST",
        url: "post/",  // or just url: "/my-url/path/"
        data: {
            userMessage: message,
            'csrfmiddlewaretoken': '{{ csrf_token }}',
        },
        success: function(data) {
            $('.Chat').append("<div class='botMessage'>fuckyou</div>");
        },
        error: function(xhr, textStatus, errorThrown) {
            alert("Please report this error: "+errorThrown+xhr.status+xhr.responseText);
        }
    });
  });
});
