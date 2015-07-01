<?php
$firstname = $lastname = $email = $password = $confpass = $errormsg = "";
$passerrormsg = $regusererrormsg = $regsuccessmsg = "";
$fieldspassed = TRUE;
$errorcount = 0;
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (empty($_POST["firstname"])) {
        $errorcount++;
    } else {
        $firstname = CleanInput($_POST["firstname"]);
    }
    if (empty($_POST["lastname"])) {
        $errorcount++;
    } else {
        $lastname = CleanInput($_POST["lastname"]);
    }
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
    if (empty($_POST["confpass"])) {
        $errorcount++;
    } else {
        $confpass = $_POST["confpass"];
    }
    if ($errorcount > 0) {
        $errormsg = "<p>One or more required field is missing!</p>";
        $fieldspassed = FALSE;
    }
    if ($password != $confpass) {
        $passerrormsg = "<p>The passwords do not match!</p>";
        $fieldspassed = FALSE;
    }
    if ($fieldspassed) {
        if ($mysqli = ConnectToDB()) {
            $firstname = $mysqli->real_escape_string($firstname);
            $lastname = $mysqli->real_escape_string($lastname);
            $email = $mysqli->real_escape_string($email);
            $password = $mysqli->real_escape_string($password);
            $okToRegisterUser = TRUE;
            $existingusers = $mysqli->query(SelectElementsWhere("*", "email = '$email'", "users"));
            if ($existingusers->num_rows > 0) {
                $okToRegisterUser = FALSE;
                $regusererrormsg = "<p>A user with this email address (username) already exists!</p>";
                $email = "";
            }
            if ($okToRegisterUser) {
                if ($mysqli->query("INSERT INTO users (id, firstname, lastname, email, password) VALUES (NULL, '$firstname', '$lastname', '$email', '$password')")) {
                    $regsuccessmsg = "<p>Registration successful!!</p>";
                }
            }
            $existingusers->free();
        }
        if (CloseDBConnection($mysqli)) { }
    }
}
?>