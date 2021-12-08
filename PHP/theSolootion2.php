<?php
   ob_start();
   session_start();

  $user = 'root';
  $password = '';
  $db = 'Solution';
  $host = 'localhost';
  $port = 8080;
  $tablename = 'AccountInfo';
  

  $success = new mysqli(
      $host,
      $user,
      $password,
      $db
  ); 

  if(!$success) {
    die('Could not connect: ' . mysqli_error($success));
  }
?>

<!DOCTYPE html>
<html>
    <head>
        <title>Login Page</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <style>
            body {
                background-color: darkgrey;
            }

            .switch {
            position: relative;
            display: inline-block;
            width: 60px;
            height: 34px;
            }

            .switch input { 
            opacity: 0;
            width: 0;
            height: 0;
            }

            .slider {
            position: absolute;
            cursor: pointer;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: #ccc;
            -webkit-transition: .4s;
            transition: .4s;
            }

            .slider:before {
            position: absolute;
            content: "";
            height: 26px;
            width: 26px;
            left: 4px;
            bottom: 4px;
            background-color: white;
            -webkit-transition: .4s;
            transition: .4s;
            }

            input:checked + .slider {
            background-color: #2196F3;
            }

            input:focus + .slider {
            box-shadow: 0 0 1px #2196F3;
            }

            input:checked + .slider:before {
            -webkit-transform: translateX(26px);
            -ms-transform: translateX(26px);
            transform: translateX(26px);
            }

            /* Rounded sliders */
            .slider.round {
            border-radius: 34px;
            }

            .slider.round:before {
            border-radius: 50%;
            }
            body {font-family: Arial, Helvetica, sans-serif;}
            * {box-sizing: border-box;}
            
            /* Full-width input fields */
            input[type=text], input[type=password], input[type=number], input[type=email] {
              width: 100%;
              padding: 15px;
              margin: 5px 0 22px 0;
              display: inline-block;
              border: none;
              background: #f1f1f1;
            }
            
            /* Add a background color when the inputs get focus */
            input[type=text]:focus, input[type=password]:focus, input[type=number]:focus, input[type=email]:focus {
              background-color: #ddd;
              outline: none;
            }
            
            /* Set a style for all buttons */
            button {
              
            }

            .registerbtn, .submitbtn {
              background-color: #4CAF50;
              color: white;
              padding: 14px 20px;
              margin: 8px 0;
              border: none;
              cursor: pointer;
              width: 100%;
              opacity: 0.9;
            }
            
            button:hover {
              opacity:1;
            }

            #signinRegister {
              background-color: #4CAF50;
              color: white;
              padding: 14px 20px;
              margin: 8px 0;
              border: none;
              cursor: pointer;
              width: 100%;
              opacity: 0.9;
            }
            
            /* Extra styles for the cancel button */
            .cancelbtn {
              padding: 14px 20px;
              
              background-color: #4CAF50;
              color: white;
              padding: 14px 20px;
              margin: 8px 0;
              border: none;
              cursor: pointer;
              width: 10%;
              opacity: 0.9;
            }
            
            /* Float cancel and signup buttons and add an equal width */

            .cancelbtn {
                width: auto;
                padding: 10px 18px;
                background-color: #f44336;
                }
            
            /* Add padding to container elements */
            .container {
              padding: 16px;
            }
            
            /* The Modal (background) */
            .modal {
              display: none; /* Hidden by default */
              position: fixed; /* Stay in place */
              z-index: 1; /* Sit on top */
              left: 0;
              top: 0;
              width: 100%; /* Full width */
              height: 100%; /* Full height */
              overflow: auto; /* Enable scroll if needed */
              background-color: #474e5d;
              padding-top: 50px;
            }
            
            /* Modal Content/Box */
            .modal-content {
              background-color: #fefefe;
              margin: 5% auto 15% auto; /* 5% from the top, 15% from the bottom and centered */
              border: 1px solid #888;
              width: 40%; /* Could be more or less, depending on screen size */
            }
            
            /* Style the horizontal ruler */
            hr {
              border: 1px solid #f1f1f1;
              margin-bottom: 25px;
            }
             
            /* The Close Button (x) */
            .close {
              position: absolute;
              right: 35px;
              top: 15px;
              font-size: 40px;
              font-weight: bold;
              color: #f1f1f1;
            }
            
            .close:hover,
            .close:focus {
              color: #f44336;
              cursor: pointer;
            }
            
            /* Clear floats */
            .clearfix::after {
              content: "";
              clear: both;
              display: table;
            }

            #RegisterForm {
                display: none;
            }

            footer {
                padding: 3px;
                text-align: center;
                position: fixed;
                height: 40px;
                background-color: black;
                bottom: 0px;
                left: 0px;
                right: 0px;
                margin-bottom: 0px;
                color: white;
            }

            footer a {
              color: white;
            }

            ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

#Login {
  background-color: #008CBA;
  color: black;
}

#Videos {
  background-color: #cb5a14;
  color: black;
}

#Donate {
  background-color: #4CAF50;
  color: black;
}

#Contact {
  background-color: #fff42c;
  color: black;
}

.dropdown {
  float: left;
  overflow: hidden;
}

.dropdown .dropbtn {
  font-size: 16px;  
  border: none;
  outline: none;
  color: white;
  padding: 14px 16px;
  background-color: inherit;
  font-family: inherit;
  margin: 0;
}

.navbar a:hover, .dropdown:hover .dropbtn {
  background-color: red;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  float: none;
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-content {
  display: block;
}

            
            /* Change styles for cancel button and signup button on extra small screens */
            @media screen and (max-width: 600px) {
              .cancelbtn, .signupbtn {
                 width: 100%;
              }

              #signinForm, #RegisterForm {
                width: 100%;
              }
          }
            </style>
            <script>
                function myFunction() {
                    $("#RegisterForm").hide();
                    var x = document.getElementById("toggle");
                    if (x.innerHTML === "Sign In") {
                        x.innerHTML = "Register";
                        $("#signinForm").hide();
                        $("#RegisterForm").show();
                    } else {
                        x.innerHTML = "Sign In";
                        $("#signinForm").show();
                        $("#RegisterForm").hide();
                    }
                }
            </script>
    </head>
    <body>
        <div>
        <nav>
                <ul id='nav'>
                    <li><a href="index.php" id='Login'>Home</a></li>
                    <li><a href="<?php $uri ?>theSolootionSearch.php" id='Videos'>Videos</a></li>
                    <li><a href="theSolootionDonate.php" id='Donate'>Donate</a></li>
                    <li><a href="theSolootionContact.php" id='Contact'>Contact</a></li>
                    <li><div class="dropdown">
                    <button class="dropbtn">More 
                    <i class="fa fa-caret-down"></i>
                    </button>
                    <div class="dropdown-content">
                        <a href="theSolootionAboutUs.php" id='aboutUs'>About Us</a>
                        <a href="Testomony.php" id='Testimonies'>Testimonies</a>
                        <a href="#" id='help'>Help</a>
                    </div>
                </div></li>
                </ul>
            </nav> 

            <center><h2 id='toggle'>Sign In</h2></center>

            <center>
              <label class="switch">
              <input type="checkbox" onclick="myFunction()">
              <span class="slider round"></span>
              </label>
            </center>

            <form id='signinForm' class="modal-content" method="POST">       
                <div class="container">
                  <h1>Log In</h1>
                  <p>Please fill out credientals to login account</p>
                  <hr>

                  <label for="usname"><b>Username</b></label>
                  <input type="text" placeholder="Enter Username" name="usernameLogin" required>
              
                  <label for="psw"><b>Password</b></label>
                  <input type="password" placeholder="Enter Password" name="passwordLogin" required>
                      
                  <input type="submit" name="submit" class="submitbtn" value="Login">

                  <input type="checkbox" checked="checked" name="remember"> Remember me
          
                </div>
              
                <div class="container" style="background-color:#f1f1f1">
                  <button type="button" class="cancelbtn">Cancel</button>
                  <span class="psw">Forgot <a href="#">password?</a></span>
                </div>
            </form>


            <form id='RegisterForm' class="modal-content" action='' method="POST">
                <div class="container">
                  <h1>Register</h1>
                  <p>Please fill in this form to create an account.</p>
                  <hr>
              
                  <label for="fname"><b>First Name</b></label>
                  <input type="text" placeholder="Ricky" name="fname" id="fname" required>

                  <label for="lname"><b>Last Name</b></label>
                  <input type="text" placeholder="Spanish" name="lname" id="lname" required>

                  <label for="uname"><b>Username</b></label>
                  <input type="text" placeholder="RateThem2020" name="uname" id="uname" required>

                  <label for="email"><b>Email</b></label>
                  <input type="email" placeholder="rate@test.com" name="email" id="email" required>

                  <label for="phone"><b>Mobile Number</b></label>
                  <input type="number" placeholder="555-555-5555" name="phone" id="phone" required>
              
                  <label for="pswd"><b>Password</b></label>
                  <input type="password" placeholder="Enter Password" name="pswd" id="pswd" required>
              
                  <label for="pswd-repeat"><b>Repeat Password</b></label>
                  <input type="password" placeholder="Repeat Password" name="pswd-repeat" id="pswd-repeat" required>
                  <hr>
                  <p>By creating an account you agree to our <a href="#">Terms & Privacy</a>.</p>
              
                  <input type="submit" name='register' class="registerbtn" value="Register">
                </div>
                
                <div class="container signin">
                  <p>Already have an account? <button onclick=myFunction() id='signinRegister'>Sign in</button>.</p>
                </div>
              </form>

              <footer>
                © Khallid Konnections 2020 | <a href="https://www.instagram.com/codingwithkhallid/"><img src="ig1.png" style="width:25px;height:25px;"></a>
              </footer>
        </div>

              <?php //LOGIN
                if(isset($_POST["submit"])){  
                  if(!empty($_POST['usernameLogin']) && !empty($_POST['passwordLogin'])) {  //forms
                      $user=$_POST['usernameLogin'];  //form
                      $pass=$_POST['passwordLogin'];  //form
                      
                      $sql = "SELECT Username, Password FROM $tablename WHERE Username='$user' AND Password='$pass'";
                      $count = "SELECT count(*) FROM $tablename WHERE Username='$user' AND Password='$pass'";

                      $sqlGO = mysqli_query($success,$sql);
                      $countGO = mysqli_query($success,$count);

                      if($countGO!=0) { 
                        while($row = mysqli_fetch_array($sqlGO)) {
                          $dbusername=$row["Username"];  
                          $dbpassword=$row["Password"]; 
                        }  
                        if($user == $dbusername && $pass == $dbpassword) {
                          $_SESSION['sess_user']=$user;  
                          /*echo "Username = ". $dbusername . "<br>";
                          echo "Password = ". $dbpassword ."<br>";
                          echo "Form username = ". $user . "<br>";
                          echo "Form password = ". $pass . "<br>";*/  
                          /* Redirect browser */  
                          header("Location: theSolootionMainMenu.php");
                          exit(); 
                        }
                        else {  
                          echo "<script>alert('Invalid username or password!')</script>"; 
                        }    
                      }
                      else {  
                        echo "<script>alert('Not in the database')</script>";
                      }    
                    } 
                    else {  
                      echo "<script>alert('All fields are required!')</script>"; 
                    }  
                  }
              ?>  

            <?php
            //REGISTER Username
            date_default_timezone_set("America/Chicago");
            $date = date("m/d/Y h:i:sa");
            if(isset($_POST["register"])) { 
              $registerPassword = $_POST["pswd"];
              $registerPasswordConfirm = $_POST["pswd-repeat"];
              if($registerPassword == $registerPasswordConfirm) {
                if(!empty($_POST['uname']) || !empty($_POST['ename'])) { 
                  $uname_= $_POST["uname"]; //declare username from form
                  $ename_= $_POST["email"];

                  $username = "SELECT count(Username) u FROM $tablename WHERE Username = '$uname_'";
                  $email = "SELECT count(Email) e FROM $tablename WHERE Email = '$ename_'";
                  
                  $usernamecount = mysqli_query($success,$username) or die(mysqli_error($success)); //run count query
                  $emailcount = mysqli_query($success,$email) or die(mysqli_error($success));

                  $userrow=mysqli_fetch_array($usernamecount);
                  $emailrow=mysqli_fetch_array($emailcount);
                  if($userrow['u']==0) { //if  zero, then it matches name in the database
                    if($emailrow['e']==0) { //if  zero, then it matches name in the database
                      $fname_= $_POST["fname"];
                      $lname_= $_POST["lname"];
                      $pname_= $_POST["phone"];
                      $pword_= $_POST["pswd"];
                      $accountImage = "defaultPic.png";
                  
                      $stmt = "INSERT INTO `AccountInfo`(`First_Name`, `Last_Name`, `Username`, `Email`, `Phone_Number`, `Password`, `Account_Photo`, `Date`) VALUES ('$fname_','$lname_','$uname_','$ename_','$pname_','$pword_','$accountImage', '$date')";
                      
                      if (mysqli_query($success, $stmt)) {
                        echo "<script>alert('Thanks for register with the shield! Your username is $uname_ Your password is $pword_')</script>";
                    } else {
                        echo "Error: " . $stmt . "<br>" . mysqli_error($success);
                    }
                      //mysqli_close($success);
                  } else {
                    echo "<script>alert('Email already exist!')</script>";  
                  }
                } 
                  else {
                    echo "<script>alert('Username already exist!')</script>";  
                  }
                }
                else {
                  echo "<script>alert('Something broke')</script>";  
                }
              }
            else {
              echo "<script>alert('Passwords Mixmatch')</script>";  
            }
          }
          ?>
    </body>
</html>