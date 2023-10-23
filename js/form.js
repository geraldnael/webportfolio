$(function() {
  var form = $('#myForm');
  var formMessages = $('#form-messages');

  $('#submitBtn').click(function(e) {
    e.preventDefault();

    var name = $('#name').val();
    var email = $('#email').val();
    var message = $('#message').val();

    if (name.length < 3) {
      displayError('Name should be at least 3 characters long.');
    } else if (!isValidEmail(email)) {
      displayError('Please enter a valid email address.');
    } else if (message.length < 5) {
      displayError('Message should be at least 5 characters long.');
    } else {
      displaySuccess('Your message was successfully validated.');
    }
  });

  function isValidEmail(email) {
    var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    return emailPattern.test(email);
  }

  function displayError(message) {
    $(formMessages).removeClass('bg-success').addClass('bg-danger');
    $(formMessages).text(message);
  }

  function displaySuccess(message) {
    $(formMessages).removeClass('bg-danger').addClass('bg-success');
    $(formMessages).text(message);
  }
});
