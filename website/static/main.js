document.getElementById("submit-btn").addEventListener("click", () => {
    const input_value = document.getElementById("input_field").value;
    window.location.href = `http://localhost:5000/message/to=${input_value}`;
});