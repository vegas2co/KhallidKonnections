<?php   

$_SESSION["sess_user"];

?> 

<!DOCTYPE html>
<html>
    <head>
        <title>Donate to Khallid Konnections</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <style>
            body {
                background-color: darkgrey;
            }
            
            #mainMenuButton {
              background-color: #4CAF50;
              color: white;
              padding: 14px 20px;
              margin: 8px 0;
              border: none;
              cursor: pointer;
              width: 100px;
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

            #img {
                box-shadow: 10px 10px 5px grey;

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
        </style>
        
    </head>
    <body>

    <nav>
                <ul>
                    <li><a href="theSolootionMainMenu.php" id='Login'>Home</a></li>
                    <li><a href="<?php $uri ?>theSolootionSearch.php" id='Videos'>Videos</a></li>
                    <li><a href="theSolootionDonate.php" id='Donate'>Donate</a></li>
                    <li><a href="theSolootionContact.php" id='Contact'>Contact</a></li>
                </ul>
            </nav>
            <center><h1>Donate to The Solootion</h1></center>
            <center><?php echo ucfirst($_SESSION["sess_user"]) ?> would you like to donate to The Solootion to help improve?</center><br>

        <div id='div2'>

            <center><a href="https://cash.app/$khallidwilliams" target="_blank">
                <img src="cashapp.png" id="img" alt="Cash App" style="width:200px;height:200px;"><p>Cash App</p>
            </a>


            <a href="https://www.paypal.me/khallidkonnections" id='paypal' target="_blank">
                <img src="paypal.jpg" id="img" alt="PayPal" style="width:200px;height:200px;"><p>PayPal</p>
            </a></center>
            
        </div>

        <footer>
            © Khallid Konnections 2020 | <a href="https://www.instagram.com/codingwithkhallid/"><img src="ig1.png" style="width:25px;height:25px;"></a>
        </footer>

  
    </body>
</html>