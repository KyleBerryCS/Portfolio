<?php
function ConnectToDB() {
	$mysqli = new mysqli(DBHOST, DBUSERNAME, DBPASSWORD, DBNAME);
	if ($mysqli->connect_error) {
		return false;
	}
	return $mysqli;
}

function SelectAllElements($tablename) {
	$query = "SELECT * FROM ";
	$query .= $tablename;
    return $query;
}

function SelectSpecificElements($columns, $tablename) {
	$query = "SELECT ";    
	for ($i = 0; $i < count($columns); $i++) {
        $query .= $columns[$i];
        if ($i != (count($columns) - 1)) {
            $query .= ", ";
        }
    }
	$query .= " FROM ";
	$query .= $tablename;
    return $query;
}

function SelectElementsWhere($columns, $conditions, $tablename) {
    $query = "SELECT ";
    $query .= $columns;
    $query .= " FROM ";
    $query .= $tablename;
    $query .= " WHERE ";
    $query .= $conditions;
    return $query;
}

function CloseDBConnection($connection) {
	return $connection->close();
}
?>