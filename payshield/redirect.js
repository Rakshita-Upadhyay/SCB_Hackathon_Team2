document.getElementById('myForm').addEventListener('submit', function(event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Redirect to the specified webpage
    window.location.href = 'customers.html'; // Replace '/newpage' with the URL of the page you want to redirect to
});
