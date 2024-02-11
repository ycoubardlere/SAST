<?php
require_once('../_helpers/strip.php');


$name = isset($_GET['name']) ? strip_tags($_GET['name']) : '';
echo 'Hello, ' . htmlspecialchars($name, ENT_QUOTES, 'UTF-8');
?>