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
    );
    $resultss = mysqli_query($success,"SELECT Badge_Number, City, State, Rating, Comment, Upload, User, Date FROM $tablename where 'Upload' like '%.mov'");
    $comments_files_array = [];
    while($rows=mysqli_fetch_array($resultss)){
        $comment_files = "Comments_$rows[Upload].php";
        if(strpos($comment_files, ".mov") !== false) {
            $comments_files_ = str_replace(".mov","",$comment_files);
            array_push($comments_files_array, $comments_files_);
        }
        if (strpos($comment_files, ".mp4") !== false) {
            $comments_files_ = str_replace(".mp4","",$comment_files);
            array_push($comments_files_array, $comments_files_);
        }

    }
?>