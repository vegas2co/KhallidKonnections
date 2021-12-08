<?php   
session_start();  
if(!isset($_SESSION["sess_user"])){  
    header("location:theSolootion2.php");  
} else {  
?> 

<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Update Password</title>
        <style>
            body {
                background-color: darkgrey;
            }
            #form, h1 {
                text-align: center;
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

                    #account {
                        background-color: #008CBA;
                        color: black;
                    }

                    #mainmenu {
                        background-color: #cb5a14;
                        color: black;
                    }
        </style>
  </head>
  <body>
<?php
    $user = 'root';
    $password = '';
    $db = 'Solution';
    $host = 'localhost';
    $port = 8080;
    $tablename = 'AccountInfo';

    $success = new mysqli($host,$user,$password,$db);  
?>

    <nav>
        <ul>
            <li><a href="theSolootionAccountSettings.php" id='account'>< Back</a></li>
            <li><a href="<?php $uri ?>theSolootionMainMenu.php" id='mainmenu'>Home</a></li>
        </ul>
    </nav>
    
      <h1> Change Password </h1>
      <div id='form'>
        <form method="post">
            Update password:<input type='text' id='password' name='password' required>
            <input type='submit' id='submit' name='submit'>
        </form>
      </div>
      <?php 
              date_default_timezone_set("America/Chicago");
              $date = date("m/d/Y h:i:sa");
              $username = $_SESSION["sess_user"];

              if(isset($_POST['submit'])) {
                if(!empty($_POST['password'])) {
                    $pword = $_POST['password']; 

                    $stmt = (
                        "UPDATE `$tablename` 
                        SET `Password` = '$pword' 
                        WHERE `Username` = '$username'"
                    );


                    if (mysqli_query($success, $stmt)) {
                        echo "<script>alert('Password updated successfully! Your new Password is $pword.')</script>";
                     } else {
                        echo "Error updating record: " . mysqli_error($success);
                     }
                     mysqli_close($success);
                    
                }
                else {
                    echo "Can not update contact support.";
                }
            }
        }
          ?>
  </body>
</html>