const form = document.getElementById("uploadForm");
const loader = document.getElementById("loader");
const resultDiv = document.getElementById("result");

const topPrediction = document.getElementById("topPrediction");
const score = document.getElementById("score");
const top3List = document.getElementById("top3");
const loadingText = document.getElementById("loadingText");

const messages = [
    "Thinking 🤔...",
    "Analyzing resume 📄...",
    "Checking skills 🧠...",
    "Matching job roles 💼...",
    "Almost done ⏳..."
];

let msgIndex = 0;

setInterval(() => {
    if (!loader.classList.contains("hidden")) {
        loadingText.textContent = messages[msgIndex % messages.length];
        msgIndex++;
    }
}, 1500);

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const fileInput = document.getElementById("fileInput");
    const file = fileInput.files[0];

    if (!file) return alert("Please upload a PDF");

    loader.classList.remove("hidden");
    resultDiv.classList.add("hidden");

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("/predict_pdf", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    loader.classList.add("hidden");
    resultDiv.classList.remove("hidden");

    topPrediction.textContent = data.top_prediction;
    score.textContent = data.suitability_score;

    top3List.innerHTML = "";
    data.top_3_matches.forEach(item => {
        const li = document.createElement("li");
        li.textContent = `${item.category} - ${item.probability}`;
        top3List.appendChild(li);
    });
});