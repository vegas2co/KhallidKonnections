<?php
    $user = 'root';
    $password = '';
    $db = 'Solution';
    $host = 'localhost';
    $port = 8080;
    $tablename = 'Contact';
      
    $success = new mysqli($host,$user,$password,$db); 

    if(!$success) {
        die('Could not connect: ' . mysqli_error($success));
    }
?>

<!DOCTYPE html>
<html>
        <head>
                <title> Contact Us</title>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="stylesheet" href="webpageStyles.css">
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
                <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css" integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU" crossorigin="anonymous">
                <link rel="stylesheet" href="https://unpkg.com/purecss@1.0.0/build/pure-min.css" integrity="sha384-nn4HPE8lTHyVtfCBi5yW9d20FjT8BJwUXyWZT9InLYax14RDjBj46LmSztkmNP9w" crossorigin="anonymous">
                <style>

                    body {
                        background-color: darkgray;
                    }
                    textarea {
                        width: 150px; 
                        height: 100px;
                    }
        
                    #top {
                        font-weight: bold; /* exercise 2 - 8 */
                    }
        
                    span {
                        font-weight: bold; /* exercise 2 - 8 */
                    }
        
                    header {
                        font-size: 40px;
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
        
                    #contact {
                        color: white;
                        font-size: 20px;
                    }
        
                    label {
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

                    @media screen and (max-width: 600px) {
                        #Message {
                            width: 90%;
                        }

                        body {
                            height: 1000px;
                        }
                    }
                    
</style>
    </head>
    <body>
        <div class="page">

            <nav>
                <ul>
                    <li><a href="theSolootionMainMenu.php" id='Login'>Home</a></li>
                    <li><a href="<?php $uri ?>theSolootionSearch.php" id='Videos'>Videos</a></li>
                    <li><a href="theSolootionDonate.php" id='Donate'>Donate</a></li>
                    <li><a href="theSolootionContact.php" id='Contact'>Contact</a></li>
                </ul>
            </nav>
    
            <section id="contact">
                <center><h2 class="content-head is-center">Contact Us!</h2>
                         <p>
                             We would <em>love</em> to hear from you! </p>
                             <p>Please use the <b><em>Contact Form</em></b>
                             to send us a message.
                         </p>
                </center>
            </section>
    
            <center>
                <form class="pure-form pure-form-aligned" action="" name="myForm" method="post">
                    <div class="pure-control-group, gform">
                            <input id="Name" name="Name" type="text" placeholder="Name" required>

                            <br><br>
                        
                            <input id="email" name="Email" type="Email" placeholder="Email Address" required>
                            
                            <br><br>
                
                            <input id="PhoneNumber" name="PhoneNumber" type="number" placeholder="Phone Number" required>
                            
                            <br><br>
                            
                            <select id="Reason" name="Reason" required>
                                    <option value='Reason for inquiry'>Reason for inquiry</option>
                                    <option value='Credentials'>Credentials</option>
                                    <option value='Account'>Account</option>
                                    <option value='Post'>Post</option>
                                    <option value='Feedback'>Feedback</option>
                                    <option value='Donation'>Donation</option>
                                    <option value='Other'>Other</option>
                            </select>
                            
                        <br><br>
                
                            <textarea type='text' id="Message" name="Message" class="pure-input-1-2" placeholder="Enter your message..." required></textarea>
                            
                        <br><br>
                        
                
                            <input id="submit" type="submit" name='submit' class="pure-button pure-button-primary" value="Submit"></button>
                        <br><br>
                    </div>
                </form>
            </center>
    
        <footer>
            © Khallid Konnections 2020  | <a href="https://www.instagram.com/codingwithkhallid/"><img src="ig1.png" style="width:25px;height:25px;"></a>
        </footer>

        <?php
      date_default_timezone_set("America/Chicago");
        $date = date("m/d/Y");

      if(isset($_POST["submit"])) {
        if(!empty($_POST["Name"])) {
        $name_ = $_POST["Name"];
        $email_ = $_POST["Email"];
        $number_ = $_POST["PhoneNumber"];
        $reason_ = $_POST["Reason"];
        $comment_ = $_POST["Message"];

        $stmt = "INSERT INTO $tablename(Name, Email,`Phone Number`, Reason, Message, Date) VALUES ('$name_','$email_','$number_','$reason_','$comment_','$date')";
        mysqli_query($success, $stmt) or die(mysqli_error($success));
        echo "<script>alert('We have received your inquiry. Thanks')</script>";
        } 
        else {
            echo "<script>alert('Please use my email at the bottom of the page.')</script>";
        }
    }
?>
        </div>
    </body>
</html>