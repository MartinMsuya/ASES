document.addEventListener('DOMContentLoaded', function() {
    // Retrieve the checkbox and input fields
    var rememberCheckbox = document.getElementById('remember');
    var usernameInput = document.getElementById('Username');
    var passwordInput = document.getElementById('password');
    var loginButton = document.querySelector('.login_button');
  
    // Check if there are stored username and password values
    var storedUsername = localStorage.getItem('rememberedUsername');
    var storedPassword = localStorage.getItem('rememberedPassword');
    if (storedUsername) {
      usernameInput.value = storedUsername;
    }
    if (storedPassword) {
      passwordInput.value = storedPassword;
    }
  
    // Save username and password values when the button is clicked
    loginButton.addEventListener('click', function() {
      localStorage.setItem('rememberedUsername', usernameInput.value);
      localStorage.setItem('rememberedPassword', passwordInput.value);
    });
  });
  