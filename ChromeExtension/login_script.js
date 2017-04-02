$.ajax({
type: "POST",
url: "http://127.0.0.1:5000",
success: function(result) {
    if (result == "True") {
        // do an autofill
        var username = 'hnguyen0428@yahoo.com';
        var password = '';

        var loginField = document.getElementById('email');
        var passwordField = document.getElementById('pass');

        // fills in username and password
        loginField.value = username;
        passwordField.value = password;

        // submits the form
        var loginForm = document.getElementById ('signIn');
        loginForm.submit()

    } else {
        alert("Unsuccessful login")
    }
}
});