<?php
	if (!empty($_SERVER['HTTPS']) && ('on' == $_SERVER['HTTPS'])) {
		$uri = 'https://';
	} else {
		$uri = 'http://';
	}
	$uri .= $_SERVER['HTTP_HOST'];
	//header('Location: '.$uri.'/dashboard/');
	//exit;
?>
<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <style>
            body {
                background-color: darkgrey;
            }

            #image {
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 25%;
                height: 15%;
            }

            #secondDiv {
                text-align: center;
                font-size: 60px;
            }

            #protect {
                text-align: center;
                font-size: 30px;
            }

            div.firstDiv {
                display: none
            }

            #searchDiv a img {
                box-shadow: 10px 10px 5px grey;
                background-color: white;
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

#QrCode {
  display: none;
}

            @media only screen and (max-width: 700px) {
                #ratethepolice {
                    font-size: 40px;
                }

                #QrCode {
                  display: block;
                  width: 200px; 
                  height: 200px;
                }
            }

        </style>
        <script>
            $(document).ready(function(){
                $("div.firstDiv").fadeIn(1000).removeClass('firstDiv');
            });

            $(document).ready(function(){
                $("#help").click(function(){
                    alert('Under Construction. Coming Soon')
                });
            });
        </script>
        <title> The Solootion </title>
    </head>
    <body>
        <nav>
            <ul>
                <li><a href="theSolootion2.php" id='Login'>Sign in</a></li>
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

        <div class='firstDiv'>
            <img id='image' src="theShield.png" alt="The Shield" width="300" height="300">
        </div>

        <div id='secondDiv'>
            Solootion
            <p id='ratethepolice'> Let's Police the Police </p>
            <p id='protect'><em>To Protect and serve</em></p>
        </div>

        <div id='thirdDic'>
            <center><img id='QrCode' src="solootionGRCode.png" alt="QR Code"></center>
        </div>

        <footer>
            © Khallid Konnections 2020 |  <a href="https://www.instagram.com/codingwithkhallid/"><img src="ig1.png" style="width:25px;height:25px;"></a>
        </footer>
    </body>
</html>

