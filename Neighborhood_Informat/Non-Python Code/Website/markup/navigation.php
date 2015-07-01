<?php
$navigation = '<nav>
    <h2>navigation</h2>
    <p>Welcome, ' . $_SESSION["firstname"] . '!</p>
    <ul>
        <li><a href="' . BASE . '">home</a></li>
        <li><a href="register.php">register</a></li>
        <li><a href="login.php">login</a></li>
        <li><a href="downloads.php">downloads</a></li>
        <li><a href="contact.php">contact us</a></li>
        <li><a href="about.php">about us</a></li>
        <li><a href="logout.php">logout</a></li>
    </ul>
</nav>';
?>