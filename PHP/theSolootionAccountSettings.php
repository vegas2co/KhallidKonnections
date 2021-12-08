<?php   
session_start();  
if(!isset($_SESSION["sess_user"])){  
    header("location:theSolootion2.php");  
} else {  
?> 

<!DOCTYPE html>
<html>
    <head>
        <title>Account Settings</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <style>
            body {
                background-color: darkgrey;
            }

            .navbar {
  overflow: hidden;
  background-color: #333;
}

.navbar a {
  float: left;
  font-size: 16px;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
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

            #mainMenuButton {
              background-color: #4CAF50;
              color: white;
              padding: 14px 20px;
              margin: 8px 0;
              border: none;
              cursor: pointer;
              width: 10%;
              opacity: 0.9;
            }

            footer {
                padding: 3px;
                text-align: center;
                position: fixed;
                height: 30px;
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

            #passwordLabel, #phonenumberLabel, #usernameLabel,  #submit, #submitForm { /* Labels */
                display:none;
            }

            #username, #password, #phonenumber { /* Text Box */
                display: none;
            }

            #personalInfo {
                text-align: center;
                font-size: 28px;
            }

            @media screen and (max-width: 892px) {


                img {
                    width: 100px;
                    height: 100px;
                }
 
            }

                #div1 h1 center {
                    position: absolute;
                    top: 45%;
                    right: 15%;
                }

                #div2 {
                    position: absolute;
                    top: 50%;
                    left: 0%;
                }

                #form {
                    position: absolute;
                    top: 80%;
                    left: 0%;
                }
            }
        </style>
        <script>
            $(document).ready(function(){
                $("#clickUsername").click(function(){
                    $("#username").show();
                    $("#usernameLabel").show();
                    $("#submitForm").show();
                });
            });

            $(document).ready(function(){
                $("#clickPassword").click(function(){
                    $("#password").show();
                    $("#passwordLabel").show();
                    //$("#submitForm").show();
                });
            });

            $(document).ready(function(){
                $("#clickPhoneNumber").click(function(){
                    $("#phonenumber").show();
                    $("#phonenumberLabel").show();
                    //$("#submitForm").show();
                });
            });

        </script>
    </head>
    <body>
            <?php
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
                $user = $_SESSION["sess_user"];
                $userInfo = mysqli_query($success,"SELECT First_Name, Last_Name, Email, Account_Photo FROM $tablename where Username = '$user'") or die(mysqli_error($success));

                $row = mysqli_fetch_array($userInfo);
                
                $firstName = ucfirst($row['First_Name']);
                $lastName = ucfirst($row['Last_Name']);
                $email = $row['Email'];
                $image = $row['Account_Photo'];
            ?>
        <nav>
        <div class="navbar">
            <a href="theSolootionMainMenu.php">Home</a>
            <div class="dropdown">
                <button class="dropbtn">More 
                <i class="fa fa-caret-down"></i>
                </button>
                <div class="dropdown-content">
                    <a href="theSolootionChangePassword.php">Change Password</a>
                    <a href="theSolootionUpdateUsername.php">Update User name</a>
                    <a href="theSolootionChangePhoneNumber.php">Update Phone Number</a>
                    <a href="#">Update Account Photo</a>
                </div>
            </div>
        </div> 
            <h1><center><?php echo ucfirst($user).'`s' ?> Account</center></h1>
        </nav>

        <div id='personalInfo'>
            Profile Picture: <?php echo "<img src='$image'width='200px' height='200px'"?> <br><br> <!-- Add image source -->
            First Name: <?php echo $firstName?><br>
            Last Name: <?php echo $lastName?><br>
            Email: <?php echo $email?>
        </div>

        <div id='div2'>
            <form enctype="multipart/form-data" method="POST">
                <p><center>Upload Profile Picture <input type='file' id='clickProfilePic' name='clickProfilePic'></center><p></p>
                <center><input id="submitPhoto" name="submitPhoto" type="submit" value="Upload Image"></center>
            </form>
        </div>


        <div id='form'>
            <form enctype="multipart/form-data" method="POST">
                <label for="username" id="usernameLabel"><b>User Name:</b></label><br>
                <input type="text" name="username" id="username" required><br><br>

                <label for="password" id="passwordLabel"><b>Password:</b></label><br>
                <input type="text" name="password" id="password" required><br><br>

                <label for="phonenumber" id="phonenumberLabel"><b>Phone Number:</b></label><br>
                <input type="number" name="phonenumber" id="phonenumber" required><br>

                <input id="submitForm" name="submitForm" type="submit" value="Submit">
            </form> 
        </div>

        <footer>
            © Khallid Konnections 2020 | Developer: Khallid Williams | <a href="mailto:williams.khallid@gmail.com">williams.khallid@gmail.com</a>
        </footer>

        <?php 
            // if file uploaded and submit button pressed and all other forms are empty - do something
            $picture = $_FILES['clickProfilePic']['name'];
            if(isset($_POST["submitPhoto"])) {
                if(!empty($picture)) {
                    mysqli_query($success,"UPDATE $tablename Set Account_Photo = '$picture' Where Username = '$user'");
                    move_uploaded_file($_FILES['clickProfilePic']['tmp_name'],$_FILES['clickProfilePic']['name']);
                    echo "<script>alert('Image uploaded');</script>";
                    header("Refresh:0");
                }
            }
        ?>

        <?php
            $username = $_POST["username"];
            $password = $_POST["password"];
            $phoneNumber = $_POST["phonenumber"];

            if(isset($_POST["submitForm"])) {
                if(!empty($username) && empty($password) && empty($phoneNumber)) {
                    mysqli_query($sucess,"UPDATE $tablename Set Username = '$username' Where Username = '$user'");

                    echo "<script>alert('Username Updated');</script>";
                    header("Location: theSolootionAccountSettings.php");
            }
        }
        ?>
        
        <?php
            }
        ?>
    </body>
</html>