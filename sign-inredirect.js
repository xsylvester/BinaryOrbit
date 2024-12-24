function redirectToSignIn() {
  // Send a fetch request to the signup endpoint
  fetch('/signin')
    .then(response => {
      // Handle the response, e.g., redirect to the signup page
      if (response.ok) {
        window.location.href = '/signin';
      } else {
        // Handle errors, e.g., display an error message
        console.error('Error fetching login page');
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
}
