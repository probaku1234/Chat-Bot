$(document).ready(function() {
    var selection;
    $(".Input").hide();

    writeMessage("Hello, I'm fucking chatbot! Please select the type of information you want!",0);

    $(".selectBox").click(function () {
       $('.Input').show();
       $('.selectBox').hide();
        console.log($(this).text());

        selection = $(this).text();

        $.ajax({
            type: "GET",
            url: "select/",
            data: {
                userSelection : selection
            },
            success: function (response) {
                writeMessage("You choose " + selection + ".",0);
                writeMessage(response,0)
            },
            error: function (xhr, textStatus, errorThrown) {
                alert("Please report this error: "+errorThrown+xhr.status+xhr.responseText);
            }
        })


    });

    $('#sendButton').click(function() {
        var message = $("#inputMessage").val();
        console.log(message);
        writeMessage(message, 1);

        $('#inputMessage').val("");
        $.ajax({
            type: "GET",
            url: "post/",  // or just url: "/my-url/path/"
            data: {
                userMessage: message,
                'csrfmiddlewaretoken': '{{ csrf_token }}',
            },
            success: function(response) {
                var response = response;
                writeMessage(response, 0)
            },
            error: function(xhr, textStatus, errorThrown) {
                alert("Please report this error: "+errorThrown+xhr.status+xhr.responseText);
            }
        });
    });
    
    function writeMessage(message, target) {
        var name;
        if (target == 0) {
            name = "botMessage";
        } else {
            name = "userMessage";
        }
        $('.Chat').append("<div class="+ name + ">" + message + "</div>");
        var div = document.getElementsByClassName('Chat');
        div[0].scrollTop = div[0].scrollHeight;
    }
});
