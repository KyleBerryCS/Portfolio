<?php
/* INCLUDE GLOBAL CONSTANTS */
require_once("constants.php");
/* INCLUDE DATABASE UTILITIES */
require_once("utilities/dbutils.php");
/* INCLUDE THE SESSION */
require_once("code/session.php");
/* INCLUDE HTML MARKUP */
require_once("markup/header.php");
require_once("markup/navigation.php");
require_once("markup/footer.php");
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
        <p>Welcome to our company website!</p>
    </main>
    <?php echo $footer; ?>
</body>
</html>