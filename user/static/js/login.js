  var cr = 0;
  var br = document.getElementsByClassName("brr");
document.getElementById("firstName").addEventListener('input', function () {
 var fn = document.getElementById("firstName");
 if (fn.value == "") {
  var form = document.getElementById("myForm");
  form.action = "create_account/";
  }
 else { 
  form.action = "login/";
 }
 });
  document.getElementById('username').addEventListener('input', function() {
    const username = this.value.trim();
    if (username === '') {
      return;
    }
    // Make AJAX request to check username uniqueness
    fetch("{% url 'check_username_unique' %}", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': '{{ csrf_token }}'
      },
      body: JSON.stringify({ username: username }),
    })
      .then(response => response.json())
      .then(data => {
        if (!data.unique) {
          document.getElementById('usernameError').textContent = 'Username is not unique.';
        } else {
          document.getElementById('usernameError').textContent = '';
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
  });

  function handleCreate() {
    if (cr == 0) {
      var fname = document.getElementsByClassName("fname");
      for (var i = 0; i < fname.length; i++) {
        fname[i].style.display = "block";
      }
      
      var lname = document.getElementsByClassName("lname");
      for (var i = 0; i < lname.length; i++) {
        lname[i].style.display = "block";
      }
      
      var email = document.getElementsByClassName("em");
      for (var i = 0; i < email.length; i++) {
        email[i].style.display = "block";
      }
      
      for (var i = 0; i < br.length; i++) {
        br[i].style.display = "block";
      }
      
      var btnn=document.getElementById('secbtn');
      btnn.innerHTML = "I have account already";
      var btnnn = document.getElementById('firstbtn');
      btnnn.innerHTML = "Signup";
      var form = document.getElementById("myForm");
      form.action = "create_account/";
      cr = 1;
    } else {
      var fname = document.getElementsByClassName("fname");
      for (var i = 0; i < fname.length; i++) {
        fname[i].style.display = "none";
      }
      
      var lname = document.getElementsByClassName("lname");
      for (var i = 0; i < lname.length; i++) {
        lname[i].style.display = "none";
      }
      
      var email = document.getElementsByClassName("em");
      for (var i = 0; i < email.length; i++) {
        email[i].style.display = "none";
      }
      
      for (var i = 0; i < br.length; i++) {
        br[i].style.display = "none";
      }
      
      var btnn=document.getElementById('secbtn');
      btnn.innerHTML = "Create New Account";
      var btnnn = document.getElementById('firstbtn');
      btnnn.innerHTML = "Login"
      var form = document.getElementById("myForm");
      form.action = "login/";
      cr = 0;
    }
  }