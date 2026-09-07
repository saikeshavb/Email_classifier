const messageInput = document.getElementById("message");
const predictButton = document.getElementById("predictButton");
const result = document.getElementById("result");

// Get selected text from the current webpage
chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    if (!tabs || !tabs[0]) {
        return;
    }

    chrome.scripting.executeScript(
        {
            target: { tabId: tabs[0].id },
            func: () => window.getSelection().toString()
        },
        (results) => {
            if (chrome.runtime.lastError) {
                console.error(
                    "Could not get selected text:",
                    chrome.runtime.lastError.message
                );
                return;
            }

            if (
                results &&
                results[0] &&
                results[0].result &&
                results[0].result.trim() !== ""
            ) {
                messageInput.value = results[0].result.trim();
            }
        }
    );
});


// Predict button
predictButton.addEventListener("click", async () => {
    const message = messageInput.value.trim();

    if (message === "") {
        result.textContent = "Please enter a message.";
        result.className = "warning";
        return;
    }

    result.textContent = "Checking...";
    result.className = "checking";

    try {
        const response = await fetch(
            "http://127.0.0.1:8000/predict",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    message: message
                })
            }
        );

        if (!response.ok) {
            throw new Error(`API request failed: ${response.status}`);
        }

        const data = await response.json();

        if (data.prediction === "spam") {
            result.textContent = "🚨 This message is SPAM";
            result.className = "spam";
        } else {
            result.textContent = "✅ This message is HAM";
            result.className = "ham";
        }

    } catch (error) {
        console.error("Prediction error:", error);

        result.textContent = "❌ Could not connect to the server.";
        result.className = "warning";
    }
});