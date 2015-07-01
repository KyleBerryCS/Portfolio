<?php
/* INCLUDE GLOBAL CONSTANTS */
require_once("constants.php");
/* INCLUDE DATABASE UTILITIES */
require_once("utilities/dbutils.php");
/* INCLUDE STRING UTILITIES */
require_once("utilities/stringutils.php");
/* INCLUDE THE SESSION */
require_once("code/session.php");
/* INCLUDE HTML MARKUP */
require_once("markup/header.php");
require_once("markup/navigation.php");
require_once("markup/footer.php");
/* INCLUDE LOGIN CODE */
require_once("code/verification.php");
?>
<!DOCTYPE html>
<head>
	<meta charset="utf-8">
	<title><?php echo TITLE; ?></title>
	<base href="<?php echo BASE; ?>">
</head>
<body>
    <?php echo $header; ?>
    <?php echo $navigation; ?>
    <main>
        <h2>login</h2>
        <?php echo $errormsg; ?>
        <?php echo $loginerrormsg; ?>
        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="post">
            
            <p><label>Username (email)*: <input name="email" type="email" value="<?php echo $email; ?>"></label></p>
            <p><label>Password*: <input name="password" type="password"></label></p>
            <p>
                <button type="submit" value="register">login</button>
                <button type="reset" value="reset">reset</button>
            </p>
            <p>*: required field</p>
        </form>
    </main>
    <?php echo $footer; ?>
</body>
</html>