<?php
session_start();
require_once "variables.php";  
$comments_files_array;
$fileName = str_replace("/","",$_SERVER['PHP_SELF']);

?> 

<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Comment Section</title>
        <style>
            .comment {
                display: block;
            }

            textarea {
                width: 300px;
                height: 100px;
                resize: none;
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
            $tablename = 'Comments';
            $tablename2 = 'AccountInfo';
            
            $success = new mysqli(
                $host,
                $user,
                $password,
                $db
            );  
            $user = $_SESSION["sess_user"];
            $count_ = mysqli_query($success,"SELECT count(*) c FROM $tablename where etc = '$fileName'") or die(mysqli_error($success)); //count number of comments per click
            $count = mysqli_fetch_array($count_); //get number of comments per click
        ?>

        <h1>Comment section</h1><br>
        
        <?php
        
            date_default_timezone_set("America/Chicago");
            $date = date("m/d/Y h:i:sa");
            $results_ = mysqli_query($success,"SELECT * FROM $tablename where etc = '$fileName' order by id desc") or die(mysqli_error($success)); //get comment page value
            
         ?> 
            
        <?php
        
        ?>
        <h2>Number of comments: <?php echo $count['c']; ?></h2>
        <form id="form" action="" method="post">
            <h1>Leave a comment:</h1>
            <!-- Here the shit they must fill out -->
            <textarea type="text" name="postid" id="postid"></textarea><br>
            <input type="submit" id="submit" name="submit">
        </form>
        <?php
        
            while($row = mysqli_fetch_array($results_)) {
                $author = $row['Author'];
                $bomments = $row['Etc'];
                if($fileName==$bomments) {
                $userImage = mysqli_query($success,"SELECT Username, Account_Photo FROM $tablename2 where Username = '$author'") or die(mysqli_error($success));
                $image = mysqli_fetch_array($userImage);
                $pic = $image['Account_Photo'];
        ?>
        
        <div class="comment">
            <br><br>By: <?php echo "<img src='$pic'width='42px' height='42px'>" ?>
            <?php 
            echo ucfirst($author); //Or similar in your table ?>
            <p>
                <?php echo "<b>Comment: </b>" . $row['Body'] . '<br>';
                    echo "Date " . $row['Date']; ?><br>
                <hr>
            </p>
        </div>
        <?php
            }
            else {
                echo $bomments;
            } 
            
        }      
        ?>

        <?php
            $body_ = $_POST["postid"];
                
            if(isset($_POST["submit"])) {
                if($user!==NULL) {
                mysqli_query($success,"insert into $tablename (Author, Body, Etc, Date) VALUES ('$user', '$body_', '$fileName', '$date')") or die(mysqli_error($success));
                echo "<script>alert('$user Submitted Comment.')</script>";
                header("Refresh:1");
            }
            else {
                echo "<script>alert('Please login Account to submit comment.')</script>";
            }
        }
        
        ?>
    </body>
</html>