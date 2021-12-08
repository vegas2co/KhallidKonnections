<?php   
session_start();  
if(!isset($_SESSION["sess_user"])){  
    header("location:theSolootion2.php");  
} else {  
?> 

<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css" integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU" crossorigin="anonymous">
        <link rel="stylesheet" href="https://unpkg.com/purecss@1.0.0/build/pure-min.css" integrity="sha384-nn4HPE8lTHyVtfCBi5yW9d20FjT8BJwUXyWZT9InLYax14RDjBj46LmSztkmNP9w" crossorigin="anonymous">
               
        <title> Submission Page</title>
        <style>
            body {
                background-color: darkgrey;
            }

            /* Full-width input fields */
            input[type=text], input[type=password], input[type=number], input[type=email] {
              width: 98%;
              padding: 15px;
              margin: 5px 0 22px 0;
              display: inline-block;
              border: none;
              background: #f1f1f1c8;
            }
            
            /* Add a background color when the inputs get focus */
            input[type=text]:focus, input[type=password]:focus, input[type=number]:focus, input[type=email]:focus {
              background-color: #ddd;
              outline: none;
            }  
            
            .pure-control-group {
              margin: 5% auto 15% auto;
            }
            
            /* Modal Content/Box */
            .pure-form {
              background-color: #fefefe;
              margin: 5% auto 15% auto; /* 5% from the top, 15% from the bottom and centered */
              border: 1px solid #888;
              width: 70%; /* Could be more or less, depending on screen size */
            }

            .pure-form #rating {
              width: 10%;
            }

            .pure-form #city {
              width: 40%;
            }

            .pure-form #badgeNumber {
              width: 40%;
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

            textarea {
                width: 300px;
                height: 100px;
                resize: none;
            }

            footer {
                padding: 3px;
                text-align: center;
                position: fixed;
                height: 50px;
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

            #Name {
              width: 10%;
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
            @media only screen and (max-width: 480px) {
              h1 center {
                font-size: 26px;
              }

              body {
                background-color: darkgrey;
            }
              .pure-control-group {
                width: 100%;
                height: 100%;
              }

              #signOut {
                width: 45%;
              }

              .pure-form {
              text-align: center;
              background-color: #fefefe;
               /* 5% from the top, 15% from the bottom and centered */
              border: 1px solid #888;
              width: 90%; /* Could be more or less, depending on screen size */
            }

            .registerbtn  {
              background-color: #4CAF50;
              color: white;
              padding: 14px 20px;
              margin: 8px 0;
              border: none;
              cursor: pointer;
              width: 50%;
              opacity: 0.9;
            }

            .pure-form #city, .pure-form #badgeNumber  {
              width: 60%;
              position: relative;
              left: 20%;
            }

            .pure-form #fileToUpload {
              position: relative;
              left: 20%;
            }

            .pure-form #rating {
              position: relative;
              left: 40%;
              width: 20%;
            }

            i {
              cursor: pointer;
            }
          }
        </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script>
            $(document).ready(function() {
                $('i').click(function() {
                    alert('Click the checkbox if you dont know the badge number and we will get the badge number for you.');
              });
            });

            function checkBox() {
              var checkBox = document.getElementById("noBD");
              var text = document.getElementById("badgeNumber");
              if (checkBox.checked == true){
                document.getElementById("badgeNumber").value = "Pending...";
                document.getElementById("badgeNumber").readOnly = true;
              }
              
              if (checkBox.checked == false){
                document.getElementById("badgeNumber").readOnly = false;
                document.getElementById("badgeNumber").value = "";
              }
            }
        </script>
    </head>
    <body>
        <?php
        $user = 'root';
        $password = '';
        $db = 'Solution';
        $host = 'localhost';
        $port = 8080;
            $tablename = 'PoliceRatings';

            $success = new mysqli(
            $host,
            $user,
            $password,
            $db
  );  ?>
      <nav>
        <ul>
            <li><a href="theSolootionMainMenu.php" id='Login'>Home</a></li>
            <li><a href="<?php $uri ?>theSolootionSearch.php" id='Videos'>Videos</a></li>
            <li><a href="theSolootionDonate.php" id='Donate'>Donate</a></li>
            <li><a href="theSolootionContact.php" id='Contact'>Contact</a></li>
        </ul>
    </nav>

        <form id='OfficerSubmitForm' class="pure-form pure-form-aligned" enctype="multipart/form-data" method="post">
            <div class="pure-control-group, gform">
              <h1><center>Enter Police Credientials</center></h1>
              <p><center>Please fill in this form to submit a form submission.</center></p>
              <hr>

              <i class="fa fa-info-circle"></i>
              <input type="checkbox" id="noBD" onclick="checkBox()"/> Unsure<br>
              <label for="badgeNumber"><b>Badge Number</b></label><br>
              <input type="text" placeholder="000001" name="badgeNumber" id="badgeNumber" required><br>

              <label for="state"><b>State</b></label><br>
              <select id="state" name="state" required>
                <option value="Alabama" selected>Alabama</option>
                <option value="Arizona">Arizona</option>
                <option value="Arkansas">Arkansas</option>
                <option value="California">California</option>
                <option value="Colorado">Colorado</option>
                <option value="Connecticut">Connecticut</option>
                <option value="Delaware">Delaware</option>
                <option value="Florida">Florida</option>
                <option value="Georgia">Georgia</option>
                <option value="Hawaii">Hawaii</option>
                <option value="Idaho">Idaho</option>
                <option value="Illinois">Illinois</option>
                <option value="Indiana">Indiana</option>
                <option value="Iowa">Iowa</option>
                <option value="Kansas">Kansas</option>
                <option value="Kentucky">Kentucky</option>
                <option value="Louisiana">Louisiana</option>
                <option value="Maine">Maine</option>
                <option value="Maryland">Maryland</option>
                <option value="Massachusetts">Massachusetts</option>
                <option value="Michigan">Michigan</option>
                <option value="Minnesota">Minnesota</option>
                <option value="Mississippi">Mississippi</option>
                <option value="Missouri">Missouri</option>
                <option value="Montana">Montana</option>
                <option value="Nebraska">Nebraska</option>
                <option value="Nevada">Nevada</option>
                <option value="New Hampshire">New Hampshire</option>
                <option value="New Jersey">New Jersey</option>
                <option value="New Mexico">New Mexico</option>
                <option value="New York">New York</option>
                <option value="North Carolina">North Carolina</option>
                <option value="North Dakota">North Dakota</option>
                <option value="Ohio">Ohio</option>
                <option value="Oklahoma">Oklahoma</option>
                <option value="Oregon">Oregon</option>
                <option value="Pennsylvania">Pennsylvania</option>
                <option value="Rhode Island">Rhode Island</option>
                <option value="South Carolina">South Carolina</option>
                <option value="South Dakota">South Dakota</option>
                <option value="Tennessee">Tennessee</option>
                <option value="Texas">Texas</option>
                <option value="Utah">Utah</option>
                <option value="Vermont">Vermont</option>
                <option value="Virginia">Virginia</option>
                <option value="Washington">Washington</option>
                <option value="West Virginia">West Virginia</option>
                <option value="Wisconsin">Wisconsin</option>
                <option value="Wyoming">Wyoming</option>
              </select><br><br>

              <label for="city"><b>City</b></label><br>
              <input type="text" placeholder="Las Vegas" name="city" id="city" required><br>

              <label for="rating"><b>Rating</b></label><br>
              <input type="number" name="rating" id="rating" min="1" max="5">    Please enter a rating 1 - 5 <br>

              <label for="comment"><b>Comment</b></label><br>
              <textarea rows="4" cols="50" type="text" placeholder="The officer was very..." name="comment" id="comment" required></textarea><br><br>

              <label for="Upload"><b>Upload File</b></label>
              <input type="file" name="fileToUpload" id="fileToUpload">
          
              <hr>
          
              <input id="submitButton" name="submitButton" type="submit" class="pure-button pure-button-primary" value='Submit'>
            </div><br><br>
          </form>

          <footer>
            © Khallid Konnections 2020 | <a href="https://www.instagram.com/codingwithkhallid/"><img src="ig1.png" style="width:25px;height:25px;"></a>
          </footer>

          <?php 
              date_default_timezone_set("America/Chicago");
              $date = date("m/d/Y h:i:sa");
              $uploadUser = $_SESSION["sess_user"]; //User thats logged in  
              if(isset($_POST['submitButton'])) {
              if(isset($_POST["badgeNumber"]) /*&& isset($_POST["city"]) && isset($_POST["state"]) && isset($_POST["rating"]) && isset($_POST["comment"]) && isset($_POST["fileToUpload"])*/) {
                $bn_= $_POST["badgeNumber"];
                $city_= $_POST["city"];
                $state_= $_POST["state"];
                $rating_= $_POST["rating"];
                $comment_= $_POST["comment"];
                $upload_= $_FILES["fileToUpload"]["name"]; //Dont forget ["name"]
                echo "<script>alert('Uploading')</script>";

                if (strpos($upload_, ".mp4") !== false) {
                  $upload_2 = str_replace(".mp4",".mov",$upload_);
                  $stmt2 =("INSERT INTO `$tablename`(`Badge_Number`, `City`, `State`, `Rating`, `Comment`, `Upload`, `User`, `Date`) VALUES ('$bn_','$city_','$state_','$rating_','$comment_','$upload_2','$uploadUser', '$date')");
                  move_uploaded_file($_FILES['fileToUpload']['tmp_name'],$upload_2);
                  mysqli_query($success, $stmt2) or die(mysqli_error($success));
                  echo "<script>alert('Everything has been uploaded successfully!)</script>";
                } 
                else {
                  $stmt =("INSERT INTO `$tablename`(`Badge_Number`, `City`, `State`, `Rating`, `Comment`, `Upload`, `User`, `Date`) VALUES ('$bn_','$city_','$state_','$rating_','$comment_','$upload_','$uploadUser', '$date')");
                  move_uploaded_file($_FILES['fileToUpload']['tmp_name'],$upload_);
                  mysqli_query($success, $stmt) or die(mysqli_error($success));         
                  echo "<script>alert('Everything has been uploaded successfully.')</script>";
                }
              }
            }
          }
          ?>
    </body>
</html>