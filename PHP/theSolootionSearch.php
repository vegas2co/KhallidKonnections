<?php
session_start();
    
$user = 'root';
$password = '';
$db = 'Solution';
$host = 'localhost';
$port = 8080;
$tablename = 'PoliceRatings';
  
  $success = new mysqli($host,$user,$password,$db); 

  if(!$success) {
    die('Could not connect: ' . mysqli_error($success));
  }
    if(isset($_POST['searchsubmit'])) {
        $valueToSearch = $_POST['search'];

        $results = mysqli_query($success,"SELECT id, Badge_Number, City, State, Rating, Comment, Upload, User, Date FROM $tablename
        WHERE Badge_Number LIKE '%$valueToSearch%' or City LIKE '%$valueToSearch%' or
        State LIKE '%$valueToSearch%' or Rating LIKE '%$valueToSearch%' or User LIKE '%$valueToSearch%' or
        Date LIKE '%$valueToSearch%' order by id DESC") or die(mysqli_error($success));
    }
    else {
        $results = mysqli_query($success,"SELECT id, Badge_Number, City, State, Rating, Comment, Upload, User, Date FROM $tablename order by id DESC") or die(mysqli_error($success));
    }
?>

<!DOCTYPE html>
<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Search Page</title>
        <style>
            body {
                background-color: darkgrey;
            }

            table, th, td {
                width: 70%;
                border: 1px solid black;
                border-collapse: collapse;
                }
                th, td {
                padding: 5px;
                text-align: left;
                background-color: white;
            }

            caption {
                font-size: 40px;
            }

            button {
              background-color: #4CAF50;
              color: white;
              padding: 14px 20px;
              margin: 8px 0;
              border: none;
              cursor: pointer;
              width: 10%;
              opacity: 0.9;
            }

            video {
                border: 1px solid green;
                cursor: pointer;
                background-color: black;
            }

            .delete {
                cursor: pointer;
                position: relative;
                left:80%;
            }

            img:hover {
                background-color: #869ba2;
            }

            .edit {
                cursor: pointer;
                position: relative;
                left:78%;
            }

            footer {
                padding: 3px;
                text-align: center;
                height: auto;
                background-color: black;
                margin-bottom: 0px;
                color: white;
                width: 100%;
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

            @media screen and (max-width: 600px) {
              #signOut {
                    width: 40%;
              }

              #search {
                  width: 50%;
              }

              #searchsubmit {
                  width: auto;
                  height: 30px;
              }

              footer {
                  width:100%;
              }

              .delete {
                  position: relative;
                  left: 80%;
              }
            }
            
        </style>
        <script>
            $(document).ready(function() {
                $('.delete').click(function() {
                    alert('Delete Information function coming soon');
              });
            });

            $(document).ready(function() {
                $('.edit').click(function() {
                    alert('Edit Information function coming soon');
              });
            });
        </script>

    </head>
    <body>
        <div>
        <!--<img src='trash.png' onclick="alert('Hello World')" alt='' /> -->
        <nav>
        <ul>
            <li><a href="theSolootionMainMenu.php" id='Login'>Home</a></li>
            <li><a href="<?php $uri ?>theSolootionSubmit.php" id='Videos'>Upload</a></li>
            <li><a href="theSolootionDonate.php" id='Donate'>Donate</a></li>
            <li><a href="theSolootionContact.php" id='Contact'>Contact</a></li>
        </ul>
    </nav>
                <form id='SearchResults' class="modal-content" method="POST">
                    <input type="text" placeholder="Search.." name="search" id="search">
                    <input type="submit" name="searchsubmit" id="searchsubmit">
                </form>
            
            <?php
                echo '<center><table>';
                echo '<caption>Police Ratings</caption>';
                
                while($row=mysqli_fetch_array($results)){ // add if statement to determine if file has endes with mov or not
                    $comment_files = "Comments_$row[Upload].php";
                    $comments_files_ = str_replace(".mov","",$comment_files);
                    $upup = str_replace(".mp4",".mov",$row['Upload']);
                    $deleteRow = $row['id'];
                    //str_replace("' '","''",$row[Upload]);
                    echo '<tr>';
                    echo "<th>Uploaded By: $row[User]   
                       <p>Date: $row[Date]</p></th>";
                    echo '</tr>';
                    if($upup) {
                    echo "<td><b>Views:</b> <center><video id='myVideo' width=480 height=320 controls>
                                <source src=$upup type=video/mp4>
                                <source src=$upup type=video/ogg>
                                <source src=$upup type=video/mov>
                                Your browser does not support the video tag.
                        </video></center>";
                        
                        if($row['User'] == $_SESSION["sess_user"]) {
                            echo "<form method='POST'>
                                    <img src='edit.png' alt='Edit Post' class='edit'>
                                    <img src='trash.png' alt='Delete Post' class='delete' name='delete'>
                                </form>";
                        }
                    } else {
                        echo "<td><center style=font-size:40px;><b>No video uploaded</b></center>";
                        if($row['User'] == $_SESSION["sess_user"]) {
                            echo "<form method='POST'>
                                    <img src='edit.png' alt='Edit Post' class='edit'>
                                    <img src='trash.png' alt='Delete Post' class='delete' name='delete'>
                                </form>";
                        }
                    }                        
                        
                        echo "<p>
                            <b>Description/Comment:</b> $row[Comment]
                        </p>

                        <p>
                            <b><u>Badge Number:</u></b> $row[Badge_Number]
                        </p>

                        <p>
                            <b><u>State:</u></b> $row[State]
                        </p>

                        <p>
                            <b><u>City:</u></b> $row[City]
                        </p>

                        <p>
                            <b><u>Rating:</u></b> $row[Rating]
                        </p>

                        <p>
                            <a href=$comments_files_
                            target='popup' 
                            onclick=window.open('$comments_files_','popup','width=600,height=600,scrollbars=no,resizable=no'); return true;>
                            <b>Comment Section</b>
                        </a>
                        </p>
                        </td>
                        ";

                    echo '</tr>';
                    $comments_files_; //Comments_{name of video}.php
                    $myfile = fopen($comments_files_, "w") or die("Unable to open file!");
                    $current = "<?php include 'Comments.php';?>";
                    fwrite($myfile, $current);
                    //$current = file_get_contents($comments_files_);
                    

                    //file_put_contents($comments_files_, $current);
                }
                echo '</table></center>';
                //$ballgame = $row['Upload'];
                $_SESSION['video']=$row;

            ?>

            <footer>
                © Khallid Konnections 2020 | <a href="https://www.instagram.com/codingwithkhallid/"><img src="ig1.png" style="width:25px;height:25px;"></a>
            </footer>

            <script>
                function delete() {
                    //mysqli_query("DELETE FROM $tablename where id = $deleteRow") or die(mysqli_error($success));
                }
            </script>
        </div>
    </body>
</html>