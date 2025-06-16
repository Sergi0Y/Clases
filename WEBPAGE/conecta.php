<?php
ob_start();

$host = "localhost";
$usuario = "root";
$contrasena = "";
$bd = "evento_roblox";

$conn = new mysqli($host, $usuario, $contrasena, $bd);
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

$nombre = $_POST['name'];
$apellido = $_POST['sname'];
$email = $_POST['email'];
$telefono = $_POST['tel'];
$ciudad = $_POST['city'];
$pais = $_POST['pais'];
$cdfrente = $_POST['cdfrente'];
$cdatras = $_POST['cdatras'];

$stmt = $conn->prepare("INSERT INTO participantes (nombre, apellido, email, telefono, ciudad, pais, cd_frente, cd_atras) VALUES (?, ?, ?, ?, ?, ?, ?, ?)");
$stmt->bind_param("ssssssii", $nombre, $apellido, $email, $telefono, $ciudad, $pais, $cdfrente, $cdatras);

if ($stmt->execute()) {
    header("Location: /WEBPAGE/dashboard.html");
    exit();
} else {
    echo "❌ Error al registrar: " . $stmt->error;
}

$stmt->close();
$conn->close();
?>
