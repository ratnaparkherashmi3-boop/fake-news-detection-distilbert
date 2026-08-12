async function checkNews() {

    const title = document.getElementById("title").value.trim();
    const text = document.getElementById("text").value.trim();

    if (!title || !text) {
        alert("Please enter both headline and article.");
        return;
    }

    const predictionElement =
        document.getElementById("prediction");

    const confidenceElement =
        document.getElementById("confidence");

    predictionElement.innerText = "Checking...";
    confidenceElement.innerText = "Please wait...";

    try {

        const response = await fetch(
            "https://cosigner-stunned-sputter.ngrok-free.dev/predict",
            {
                method: "POST",

                mode: "cors",

                headers: {
                    "Content-Type": "application/json",
                    "ngrok-skip-browser-warning": "1"
                },

                body: JSON.stringify({
                    title: title,
                    text: text
                })
            }
        );

        console.log("HTTP Status:", response.status);

        if (!response.ok) {
            throw new Error(
                "Server returned status " + response.status
            );
        }

        const data = await response.json();

        console.log("API Response:", data);

        predictionElement.innerText =
            data.prediction;

        confidenceElement.innerText =
            "Confidence: " + data.confidence + "%";

    }

    catch (error) {

        console.error("API Error:", error);

        predictionElement.innerText =
            "Error";

        confidenceElement.innerText =
            "Unable to connect to prediction server.";

    }
}