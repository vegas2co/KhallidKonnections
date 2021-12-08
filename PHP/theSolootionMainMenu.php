<?php  
/*
$user = 'solootio_khallidkonnect';
$password = 'Lilalnisa23$';
$db = 'solootio_khallidkonnect';
$host = '50.87.199.45';
$port = 8080;
$tablename = 'AccountInfo';

*/
session_start();  
if(!isset($_SESSION["sess_user"])){  
    header("location:theSolootion2.php");  
} else {  
?> 
<!DOCTYPE html>
<html>
    <head>
        <title>Main Menu</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script>

            $(document).ready(function() {
                $('#signOut').click(function() {
                    confirm('You are about to sign out!');
                });
            });

        </script>
        <style>

            body {
                background-color: darkgrey;
            }

            center {
                font-size: 40px;
                font-weight: bold;
            }

            #image {
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 30%;
                height: 30%;
            }

            #secondDiv {
                max-width: 100%;
                height: auto;
                /*border: 1px solid #c3c3c3;*/
                display: flex;
                justify-content: space-between;
            }

            #secondDiv a {
                width: 70px;
                height: 70px;
            }

            #secondDiv a img:hover {
                background-color: #869ba2;
            }

            #entries h3  {
                position: absolute;
                left: 2%;
                top: 4%;
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

            #secondDiv a img {
                box-shadow: 10px 10px 5px grey;
                background-color: white;
            }

            #secondDiv a img p {
                color: white;
            }

            #info img, #smartphone img, #home img, #upload img, #videos img {
                border-radius: 20%;
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

li a:hover:not(.active) {
  background-color: red;
}

.active {
  background-color: #4CAF50;
}

            @media screen and (max-width: 600px) {
              .cancelbtn, .signupbtn {
                 width: 100%;
              }

              #signOut, #donate {
                  width: 25%;
                  left: 40%;
              }

              #settings {
                  width: 25%;
              }


              div#name {
                position: relative;
                top: 60px;
            }

            div#firstDiv {
                position: relative;
                top: 80px;
            }

            div#secondDiv {
                position: relative;
                top:150px;
            }

            #entries h3 {
                padding-left: 12.5%;
                padding-right: 12.5%;
                width: 75%;
            }
              
            }
        </style>
    </head>
    <body>
    
    <?php
        date_default_timezone_set("America/Chicago");
        $date = date("m/d/Y");
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
        $results = mysqli_query($success,"SELECT count(*) c FROM PoliceRatings WHERE Date like '$date%'") or die(mysqli_error($success));
       
        $row=mysqli_fetch_array($results);
        
    ?>
        <nav>
            <ul>
                <li><a href="theSolootionLogOut.php" id='signOut'>LogOut</a></li>
                <li style="float:right"><a class="active" href="theSolootionAccountSettings.php">Settings</a></li>
                <li style="float:right"><a href="theSolootionDonate.php">Donate</a></li>
              </ul>
        </nav>
        <div id='entries'>
            <h3><br><br>Number of uploads added today: <?php echo $row['c']; ?></h3>
        </div>
        <div id='name'>
            <center>The Solootion</center>
            <center>Welcome <u><?php echo ucfirst($_SESSION["sess_user"]) ?></u></center>
        </div>
        <div id='firstDiv'>
            <img id='image' src="theShield.png" alt="The Shield">
        </div>

        <div id='secondDiv'>
            <a href="theSolootionSubmit.php" id='upload'>
                <img src="user.png" alt="Submit Officer" style="width:42px;height:42px;"><p>Upload</p>
            </a>

            <a href="theSolootionSearch.php" id='videos'>
                <img src="search.png" alt="Search Officer" style="width:42px;height:42px;"><p>Search</p>
            </a>

            <!--theSolootionAboutUs.php-->

            <a href="theSolootionAboutUs.php" id='info'>
                <img src="info.png" alt="About Solootion" style="width:42px;height:42px;"><p>About</p>
            </a>

            <a href="theSolootionContact.php" id='smartphone'>
                <img src="smartphone.png" alt="Contact Khallid Konnections" style="width:42px;height:42px;"><p>Contact</p>
            </a>

            <a href="Testomony.php" id='home'>
                <img src="home.png" alt="Search Officer" style="width:42px;height:42px;"><p>Testimonies</p>
            </a>
        </div>
        
        <footer>
            © Khallid Konnections 2020 |    <a href="https://www.instagram.com/codingwithkhallid/"><img src="ig1.png" style="width:25px;height:25px;"></a>
        </footer>
        <?php
            }
        ?>
    </body>
</html>