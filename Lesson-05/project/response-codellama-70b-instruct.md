# Response

* Create a file called chat.html.
* Add the following HTML code to it:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <input type="text" id="message" placeholder="Type your message...">
        <button id="generate">Send</button>
        <script src="chat.js"></script>
    </body>
</html>
```

* Create a file called chat.js.
* Add the following JavaScript code to it:

```javascript
document.getElementById("generate").addEventListener("click", sendMessage);

function sendMessage() {
    const message = document.getElementById("message").value;
    const url = "https://example.com/api/message";
    const data = { message: message };
    const options = {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-Type": "application/json"
        }
    };

    fetch(url, options)
        .then(response => {
            if (response.ok) {
                console.log("Message sent successfully!");
            } else {
                console.error("There was an error sending the message!");
            }
        })
        .catch(error => {
            console.error(error);
        });
}
```

* Now, when you open chat.html on your browser and type a message in the input field, you can click the "Send" button to send the message to the provided API URL. Note that you need to replace the API URL with your own.
