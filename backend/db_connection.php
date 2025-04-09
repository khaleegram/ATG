<?php
$host = 'localhost';
$user = 'root';
$password = '787978';
$database = 'ATG_DB';

$conn = new mysqli($host, $user, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
