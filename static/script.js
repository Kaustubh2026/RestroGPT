document.getElementById("send-btn").addEventListener("click", function () {
    let userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") return;

    // Append user message to chat
    let chatBox = document.getElementById("chat-box");
    let userMessage = document.createElement("div");
    userMessage.className = "message user";
    userMessage.innerText = userInput;
    chatBox.appendChild(userMessage);

    // Send message to Flask backend
    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        let botMessage = document.createElement("div");
        botMessage.className = "message bot";
        botMessage.innerText = data.response;
        chatBox.appendChild(botMessage);
    })
    .catch(error => console.error("Error:", error));

    // Clear input field
    document.getElementById("user-input").value = "";
});
