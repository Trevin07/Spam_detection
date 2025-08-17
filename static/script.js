const subjectInput = document.getElementById("subjectText");
const bodyInput = document.getElementById("bodyText");
const checkBtn = document.getElementById("checkBtn");
const clearBtn = document.getElementById("clearBtn");
const resultDiv = document.getElementById("result");
const labelBadge = document.getElementById("labelBadge");
const percentage = document.getElementById("percentage");
const barFill = document.getElementById("barFill");
const explain = document.getElementById("explain");

checkBtn.addEventListener("click", async () => {
  const text = `Subject: ${subjectInput.value} Body: ${bodyInput.value}`;
  if (!text.trim()) return;

  try {
    const res = await fetch("/predict", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({text})
    });
    const data = await res.json();

    const label = data.prediction === "spam" ? "Spam" : "Not Spam";
    // confidence calculation
    const conf = label === "Spam"
      ? (data.probability * 100).toFixed(1)
      : ((1 - data.probability) * 100).toFixed(1);

    labelBadge.textContent = label;
    percentage.textContent = conf + "%";
    barFill.style.width = conf + "%";
    barFill.style.background = label === "Spam" ? "var(--danger)" : "var(--accent)";
    explain.textContent = `This email is classified as "${label}" with ${conf}% confidence.`;
    resultDiv.classList.remove("hide");

  } catch (err) {
    console.error(err);
  }
});

clearBtn.addEventListener("click", () => {
  subjectInput.value = "";
  bodyInput.value = "";
  resultDiv.classList.add("hide");
});

// Fill example emails
function fillExample(type){
  if(type==="spam"){
    subjectInput.value = "You won $1,000,000!";
    bodyInput.value = "Claim your prize by paying a $50 processing fee: [scam.link],send us your bank account number to recieve the payment.";
  } else {
    subjectInput.value = "Meeting Tomorrow at 10 AM";
    bodyInput.value = "Hi team, just a reminder we have our regular meeting tomorrow at 10 AM.";
  }
  checkBtn.click();
}
