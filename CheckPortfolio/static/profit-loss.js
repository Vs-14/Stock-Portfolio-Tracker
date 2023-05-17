// Get all the table rows
const rows = document.querySelectorAll("tbody tr");

// Loop through each row
rows.forEach(row => {
  // Get the cell containing the change percentage
  const changeCell = row.querySelector("td:nth-child(8)");

  // Get the cell containing the current total value
  const currentTotalCell = row.querySelector("td:nth-child(7)");

  // Get the value of the change percentage
  const change = parseFloat(changeCell.textContent);

  // Set the text color of the change percentage and current total value cells
  if (change < 0) {
    changeCell.style.color = "red";
    currentTotalCell.style.color = "red";
  } else if (change > 0) {
    changeCell.style.color = "green";
    currentTotalCell.style.color = "green";
  }
});
