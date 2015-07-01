<?php
$download = '';
if ($_SESSION['valid']) {
    $download = '<p>Welcome to the downloads page!! You have access!!</p>
        <p><a href="utilities/download.php">Download your file!</a></p>';
} else {
    $download = '<p>You don\'t have permission to view the downloads page!! Jerk!</p>';
}
?>