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
/* INCLUDE REGISTRATION CODE */
require_once("code/registration.php");
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
        <h2>registration</h2>
        <?php echo $errormsg; ?>
        <?php echo $passerrormsg; ?>
        <?php echo $regusererrormsg; ?>
        <?php echo $regsuccessmsg; ?>
        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="post">
            <p><label>First Name*: <input name="firstname" type="text" value="<?php echo $firstname; ?>"></label></p>
            <p><label>Last Name*: <input name="lastname" type="text" value="<?php echo $lastname; ?>"></label></p>
            <p><label>eMail Address*: <input name="email" type="email" value="<?php echo $email; ?>"></label></p>
            <p><label>Password*: <input name="password" type="password"></label></p>
            <p><label>Confirm Password*: <input name="confpass" type="password"></label></p>
            <p><label>Premium Account: <input name="premium" type="checkbox"></label></p>
            <p>
                <button type="submit" value="register">register</button>
                <button type="reset" value="reset">reset</button>
            </p>
            <p>*: required field</p>
        </form>
    </main>
    <?php echo $footer; ?>
</body>
</html>