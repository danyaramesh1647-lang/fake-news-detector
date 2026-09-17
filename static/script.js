const textArea = document.getElementById("article-text");
const wordCountEl = document.getElementById("word-count");
const analyzeBtn = document.getElementById("analyze-btn");
const errorMsg = document.getElementById("error-msg");
const verdictSection = document.getElementById("verdict-section");
const stamp = document.getElementById("stamp");
const stampLabel = document.getElementById("stamp-label");
const confidenceFill = document.getElementById("confidence-fill");
const confidenceText = document.getElementById("confidence-text");

function countWords(text) {
  const trimmed = text.trim();
  return trimmed === "" ? 0 : trimmed.split(/\s+/).length;
}

textArea.addEventListener("input", () => {
  const count = countWords(textArea.value);
  wordCountEl.textContent = `${count} word${count === 1 ? "" : "s"}`;
});

async function analyze() {
  const text = textArea.value.trim();
  errorMsg.textContent = "";

  if (countWords(text) < 3) {
    errorMsg.textContent = "Please enter a longer piece of text (at least a few words).";
    return;
  }

  analyzeBtn.disabled = true;
  analyzeBtn.textContent = "Analyzing…";

  try {
    const response = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });

    const data = await response.json();

    if (!response.ok) {
      errorMsg.textContent = data.error || "Something went wrong. Please try again.";
      return;
    }

    renderVerdict(data.prediction, data.confidence);
  } catch (err) {
    errorMsg.textContent = "Could not reach the server. Please try again.";
  } finally {
    analyzeBtn.disabled = false;
    analyzeBtn.textContent = "Analyze text";
  }
}

function renderVerdict(prediction, confidence) {
  verdictSection.hidden = false;
  stamp.classList.remove("is-real", "is-fake");
  stamp.classList.add(prediction === "REAL" ? "is-real" : "is-fake");
  stampLabel.textContent = prediction === "REAL" ? "REAL" : "FAKE";
  confidenceFill.style.width = `${confidence}%`;
  confidenceText.textContent = `${confidence}%`;
}

analyzeBtn.addEventListener("click", analyze);
textArea.addEventListener("keydown", (e) => {
  if ((e.metaKey || e.ctrlKey) && e.key === "Enter") analyze();
});