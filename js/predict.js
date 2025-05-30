document.getElementById("form").addEventListener("submit", async function (e) {
  e.preventDefault();
  const resultadoDiv = document.getElementById("resultado");
  resultadoDiv.className = "";
  resultadoDiv.textContent = "Processing...";

  const formData = new FormData(e.target);
  const jsonData = {};
  formData.forEach((value, key) => (jsonData[key] = value));

  try {
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(jsonData),
    });

    const data = await response.json();

    if (!response.ok) {
      resultadoDiv.className = "error";
      let errorMsg = `Error: ${data.erro || "Unknown error"}`;
      if (data.valid_values) {
        errorMsg += `<br>Accepted values: ${data.valid_values.join(", ")}`;
      }
      resultadoDiv.innerHTML = errorMsg;
    } else {
      resultadoDiv.className = "success";
      resultadoDiv.innerHTML = `
        Predicted severity: ${data.severidade_predita}<br>
        Confidence: ${data.probabilidade}
      `;
    }
  } catch (error) {
    resultadoDiv.className = "error";
    resultadoDiv.textContent = `Connection error: ${error.message}`;
  }
});
