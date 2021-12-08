<!DOCTYPE html>
<html>
<body>
        
<?php $db = new SQLite3('/Users/khallidwilliams/Library/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/KhallidKonnections.db');
?>

<form enctype="multipart/form-data" method="POST" >
  Select image to upload:
  <input type="file" name="fileToUpload" id="fileToUpload">
  <input type="submit" value="Upload Image" name="submit">
</form>

<?php
if(isset($_POST["submit"])) {
          echo "<script>alert('Please wiorkasdf.')</script>"; //please work
          
          $upload_= $_FILES["fileToUpload"]["name"]; //Dont forget ["name"]
          $db->exec("insert into images ([Upload]) VALUES ($upload_)");

          echo "<script>alert('Everything has been uploaded successfully - HHAHAHAHAH')</script>";
          
          
}
        ?>

</body>
</html>