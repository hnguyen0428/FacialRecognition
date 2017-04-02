url = 'http://127.0.0.1:5000'
var getJSON = function(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'json';
    xhr.onload = function() {
      var status = xhr.status;
      if (status == 200) {
        callback(null, xhr.response);
      } else {
        callback(status);
      }
    };
    xhr.send();
};

getJSON(url, function(err, data) {
  if (err != null) {
      alert('Something went wrong: ' + err);
  } else {
      console.log(data['match']);
      if(data['match'] == true) {
          var myUsername = '';
          var myPassword = '';

          //finds the fields in your login form
          var loginField = document.getElementById('email');
          var passwordField = document.getElementById('pass');

          //fills in your username and password
          loginField.value = myUsername;
          passwordField.value = myPassword;

          //automatically submits the login form
          var loginButton = document.getElementById('loginbutton');

          loginButton.click();
      } else {
          alert('Does not match')
      }
  }
});