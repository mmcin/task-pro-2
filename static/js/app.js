// Bootstrap Tooltips
const themeToolTip = document.getElementById("theme-tooltip");
const tooltip = new bootstrap.Tooltip(themeToolTip);

// ----- Script For Changing The Theme -----

// Local storgage to save visitor preferences & Button to chnage theme
let darkMode = localStorage.getItem("darkMode");
const themeChangeButton = document.querySelector("#theme-tooltip");

// Function to enable darkmode.
const enableDarkMode = () => {
  document.body.classList.add("darkmode");
  localStorage.setItem("darkMode", "enabled");
};

// Function to disable darkmode
const disableDarkMode = () => {
  document.body.classList.remove("darkmode");
  localStorage.setItem("darkMode", null);
};

// Check for user preference on page load
if (darkMode === "enabled") {
  enableDarkMode();
}

// Event listener for theme change
themeChangeButton.addEventListener("click", () => {
  darkMode = localStorage.getItem("darkMode");
  if (darkMode !== "enabled") {
    enableDarkMode();
  } else {
    disableDarkMode();
  }
});
