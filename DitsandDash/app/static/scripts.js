async function convertToMorse() {
    const text = document.getElementById("textInput").value;
    const response = await fetch("http://127.0.0.1:5000/encode", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    });
    const data = await response.json();
    document.getElementById("morseOutput").innerText = data.morse;
}

async function convertToText() {
    const morse = document.getElementById("morseInput").value;
    const response = await fetch("http://127.0.0.1:5000/decode", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ morse })
    });
    const data = await response.json();
    document.getElementById("textOutput").innerText = data.text;
}
