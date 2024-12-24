function redirectToSignUp() {
  // Send a fetch request to the signup endpoint
  fetch('/signup')
    .then(response => {
      // Handle the response, e.g., redirect to the signup page
      if (response.ok) {
        window.location.href = '/signup';
      } else {
        // Handle errors, e.g., display an error message
        console.error('Error fetching signup page');
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
}
