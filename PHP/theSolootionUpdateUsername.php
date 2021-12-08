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
    <title>Update User name</title>
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
    $user = 'solootio_khallidkonnect';
    $password = 'Lilalnisa23$';
    $db = 'solootio_khallidkonnect';
    $host = '50.87.199.45';
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
    
      <h1> Update Username </h1>
      <div id='form'>
        <form method="post">
            Update Username:<input type='text' id='username' name='username' required>
            <input type='submit' id='submit' name='submit'>
        </form>
      </div>
      <?php 
              date_default_timezone_set("America/Chicago");
              $date = date("m/d/Y h:i:sa");
              $username = $_SESSION["sess_user"];

              if(isset($_POST['submit'])) {
                if(!empty($_POST['username'])) {
                    $uname_ = $_POST['username'];
                    $usernameQuery = "SELECT count(Username) u FROM $tablename WHERE Username = '$uname_'"; 
                    $usernamecount = mysqli_query($success,$usernameQuery) or die(mysqli_error($success));
                    $userrow=mysqli_fetch_array($usernamecount);
                    if($userrow['u']==0) {
                        $stmt = (
                            "UPDATE `$tablename` 
                            SET `Username` = '$uname_' 
                            WHERE `Username` = '$username'"
                        );

                        $policeRating = (
                            "UPDATE `PoliceRatings` 
                            SET `User` = '$uname_' 
                            WHERE `User` = '$username'"
                        );

                        $Comments = (
                            "UPDATE `Comments` 
                            SET `Author` = '$uname_' 
                            WHERE `Author` = '$username'"
                        );


                        if (mysqli_query($success, $stmt)) {
                            mysqli_query($success, $policeRating);
                            mysqli_query($success, $Comments);
                            echo "<script>alert('Username updated successfully! Your new Username is $uname_.')</script>";
                            echo "<script>alert('Log out and log back in to see changes.')</script>";
                        } else {
                            echo "Error updating record: " . mysqli_error($success);
                        }
                        mysqli_close($success);
                    } else {
                        echo "<script>alert('Username already exist!')</script>";
                    }
                    
                }
                else {
                    echo "Can not update contact support.";
                }
            }
        }
          ?>
  </body>
</html>