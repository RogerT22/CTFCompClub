<!DOCTYPE html>
<html lang="en" dir="ltr">
<?php
  $host = "localhost";
  $user = "root";
  $password = "";
  $db = "demo";
  $conn = mysqli_connect($host,$user,$password, $db);
  //mysql_connect_db($db);
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
  if(isset($_POST['username'])) {
    //echo "YES";
    $sql = "SELECT ID, User, Pass FROM loginform";
    $result = $conn->query($sql);
    //var_dump($_POST);
    if ($result->num_rows > 0) {
      while($row = $result->fetch_assoc()) {
        if( ($row["User"] == $_POST['username']) && ($row["Pass"] == $_POST['password']) ) {
          echo "LOGGED IN";
        }
        //echo "id: " . $row["ID"]. " - Name: " . $row["User"]. " " . $row["Pass"]. "<br>";
      }
    } else {
        echo "0 results";
    }
  }
    $conn->close();
?>
  <head>
    <meta charset="utf-8">
    <script type="text/javascript" src="./login.css"></script>
    <p id="demo"></p>
    <title></title>
    <link rel="stylesheet" href="./LoginFormstyle.css">
  </head>
  <body>

    <div class="login-box">
      <h1>Login</h1>
      <form method= "post" action = "LoginForm.php">
      <div class="textbox">
        <i class="fas fa-user"></i>
        <input type="text" name = "username" placeholder="Username">
      </div>
      <div class="textbox">
        <i class="fas fa-lock"></i>
        <input type="password" name = "password" placeholder="Password">
      </div>
      <input type="submit" class="btn" value="Sign in">
      </form>
    </div>
      <button type="button" onclick = "reveal()"></button>
  </body>
</html>
