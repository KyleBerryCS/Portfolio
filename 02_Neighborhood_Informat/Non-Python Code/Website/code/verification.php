<?php
$email = $password = $errormsg = $loginerrormsg = "";
$fieldspassed = TRUE;
$errorcount = 0;
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (empty($_POST["email"])) {
        $errorcount++;
    } else {
        $email = $_POST["email"];
    }
    if (empty($_POST["password"])) {
        $errorcount++;
    } else {
        $password = $_POST["password"];
    }
    if ($errorcount > 0) {
        $errormsg = "<p>One or more required field is missing!</p>";
        $fieldspassed = FALSE;
    }
    if ($fieldspassed) {
        if ($mysqli = ConnectToDB()) {
            $email = $mysqli->real_escape_string($email);
            $password = $mysqli->real_escape_string($password);
            $regusers = $mysqli->query(SelectElementsWhere("*", "email = '$email' AND password = '$password'", "users"));
            if ($regusers->num_rows == 1) {
                $email = "";
                $password = "";
                $user = $regusers->fetch_assoc();
                $_SESSION['valid'] = TRUE;
                $_SESSION['uid'] = $user['id'];
                header("Location: index.php");
                exit;
            } else {
                $password = "";
                $loginerrormsg = "<p>The username or password was incorrect!</p>";
            }
            $regusers->free();
        }
        if (CloseDBConnection($mysqli)) { }
    }
}
?>