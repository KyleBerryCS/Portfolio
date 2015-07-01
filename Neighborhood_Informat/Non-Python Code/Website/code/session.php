<?php
session_start();
if ($_SESSION['valid']) {
    if ($mysqli = ConnectToDB()) {
        $users = $mysqli->query(SelectElementsWhere("*", "id = " . $_SESSION['uid'] . "", "users"));
        if ($users->num_rows == 1) {
            $user = $users->fetch_assoc();
            $_SESSION['firstname'] = $user['firstname'];
        }
        $users->free();
    }
    if (CloseDBConnection($mysqli)) { }
} else {
    $_SESSION['firstname'] = "Guest";
}
?>