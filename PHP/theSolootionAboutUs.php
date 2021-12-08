<html>
<head>
    <title>About Us page</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
                background-color: darkgrey;
            }
        
        #text {
            text-align: center;
        }

        img {
                box-shadow: 10px 10px 5px grey;
            }

        h1 {
            font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
            font-size: 50px;
        }

        h3 {
            font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
            font-size: 20px;
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

@media screen and (max-width: 600px) {
        h1 {
            font-size: 28px;
        }

        h3 {
            font-size: 16px;
        }

        img {
            width: 50%;
            height: 30%;
        }

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
            <li><div class="dropdown">
            <button class="dropbtn">More 
            <i class="fa fa-caret-down"></i>
            </button>
            <div class="dropdown-content">
                <a href="#" id='aboutUs'>About Us</a>
                <a href="Testomony.php" id='Testimonies'>Testimonies</a>
                <a href="#" id='help'>Help</a>
            </div>
        </div></li>
          </ul>
    </nav>
    <div class='firstDiv'>
        <center><img id='image' src="aboutMe.jpg" alt="Grad Pic" width="300" height="300"></center><br>
    </div>
    <div id='text'>
        <h3>- Our Mission -</h3>
        <h1>BRING POLICE JUSTICE <br> AND AWARENESS <br> TO EVERY CIVILIAN <br> IN THE WORLD. </h1>
        <!--Welcome to Solootion, your number one source for police ratings. We're dedicated to giving you the very best of police rating software.

Founded in 2018 by Khallid Konnections, Khallid Konnections has come a long way from its beginnings. When Khallid Konnections first started out, their passion for victims and civilians to essentially police the police drove them to quit day jobs, do tons of research and build an iOS app (The Shield) so that Khallid Konnections can offer you the ability to rate police officers, anonymously file police reports, view uploads, etc. We now serve customers all over the United States, and are thrilled that we're able to turn our passion into our own mobile app.

We hope you enjoy our product as much as we enjoy offering them to you. If you have any questions or comments, please don't hesitate to contact us. 

NO ONES ABOVE THE LAW.



<p>Sincerely,</p>
<p>Khallid Konnections<p>-->
    </div>

    <footer>
        © Khallid Konnections 2020 | <a href="https://www.instagram.com/codingwithkhallid/"><img src="ig1.png" style="width:25px;height:25px;"></a>
      </footer>
</body>
</html>