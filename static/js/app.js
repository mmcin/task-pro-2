// Bootstrap Tooltips
const themeToolTip = document.getElementById("theme-tooltip");
const tooltip = new bootstrap.Tooltip(themeToolTip);

// ----- Script For Changing The Theme -----

// Local storgage to save visitor preferences, button to change theme & Icon
let darkMode = localStorage.getItem("darkMode");
const themeChangeButton = document.querySelector("#theme-tooltip");
const themeChangeIcon = document.querySelector(".theme-toggle");

// Function to enable darkmode.
const enableDarkMode = () => {
  //  Add darkmode display to the body
  document.body.classList.add("darkmode");
  //   Animation Spin & change.
  themeChangeIcon.classList.add("rotate-icon");
  themeChangeIcon.classList.add("fa-moon");
  themeChangeIcon.classList.remove("fa-sun");
  //   Local storage update
  localStorage.setItem("darkMode", "enabled");
};

// Function to disable darkmode
const disableDarkMode = () => {
  //  Add darkmode display to the body
  document.body.classList.remove("darkmode");
  //   Animation Spin & change.
  themeChangeIcon.classList.add("rotate-icon");
  themeChangeIcon.classList.remove("fa-moon");
  themeChangeIcon.classList.add("fa-sun");
  setTimeout(() => {
    themeChangeIcon.classList.remove("rotate-icon");
  }, 0);
  //   Local storage update
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
