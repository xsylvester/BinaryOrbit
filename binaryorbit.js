// script.js
document.getElementById('signup-button').addEventListener('click', function() {
    // Send a request to your FastAPI server
    fetch('/signup')
      .then(response => {
        // Handle the response from the server, e.g., redirect to the signup page
        if (response.ok) {
          window.location.href = '/signup-page'; // Replace with your actual signup page URL
        } else {
          // Handle errors, e.g., display an error message
          console.error('Error fetching signup page');
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
});

