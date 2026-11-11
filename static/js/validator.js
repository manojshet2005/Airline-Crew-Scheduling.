(() => {
  const form = document.querySelector("#validator-form");
  const result = document.querySelector("#result");
  const submitButton = document.querySelector("#submit");
  const fieldNames = ["daily", "weekly", "rest"];

  function clearFieldErrors() {
    for (const name of fieldNames) {
      const input = document.querySelector(`#${name}`);
      input.removeAttribute("aria-invalid");
      document.querySelector(`#${name}-error`).textContent = "";
    }
  }

  function showResult(kind, title, message) {
    result.className = `result-panel result-${kind}`;
    result.querySelector(".result-symbol").textContent =
      kind === "valid" ? "✓" : kind === "invalid" ? "×" : "!";
    result.querySelector(".result-title").textContent = title;
    result.querySelector(".result-message").textContent = message;
    result.hidden = false;
  }

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    clearFieldErrors();

    const invalidFields = fieldNames.filter((name) => {
      const input = document.querySelector(`#${name}`);
      if (!input.value.trim() || !input.validity.valid) {
        input.setAttribute("aria-invalid", "true");
        document.querySelector(`#${name}-error`).textContent =
          input.value.trim() ? "Enter a valid non-negative number." : "This field is required.";
        return true;
      }
      return false;
    });

    if (invalidFields.length) {
      showResult("error", "Check the highlighted fields", "Enter a finite, non-negative number in each field.");
      document.querySelector(`#${invalidFields[0]}`).focus();
      return;
    }

    submitButton.disabled = true;
    submitButton.textContent = "Checking…";
    try {
      const values = Object.fromEntries(
        fieldNames.map((name) => [name, Number(document.querySelector(`#${name}`).value)])
      );
      const response = await fetch("/api/validate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(values),
      });
      const data = await response.json();

      if (!response.ok) {
        showResult("error", "Input could not be checked", data.message || "Correct the input and try again.");
      } else if (data.valid) {
        showResult("valid", "Schedule is within sample limits", data.message);
      } else {
        showResult("invalid", "Schedule does not meet the sample limits", data.message);
      }
    } catch {
      showResult("error", "Validation service unavailable", "The check could not reach the application. Please try again.");
    } finally {
      submitButton.disabled = false;
      submitButton.innerHTML = '<span aria-hidden="true">✓</span> Validate schedule';
    }
  });

  form.addEventListener("reset", () => {
    clearFieldErrors();
    result.hidden = true;
    result.className = "result-panel result-empty";
    result.querySelector(".result-title").textContent = "";
    result.querySelector(".result-message").textContent = "";
  });
})();
