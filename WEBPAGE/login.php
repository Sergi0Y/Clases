<?php
session_start();

// Obtener datos del formulario
$user = $_POST['user'] ?? '';
$pass = $_POST['pass'] ?? '';

// Lista de usuarios válidos
$usuarios_validos = [
    'admin' => '1234',
    'sergio' => $cdatras
];

// Validar usuario
if (array_key_exists($user, $usuarios_validos) && $usuarios_validos[$user] === $pass) {
    $_SESSION['usuario'] = $user;

    // Redirigir según el usuario
    if ($user === 'admin') {
        header("Location: http://localhost/WEBPAGE/admin.php");
    } else {
        header("Location: http://localhost/WEBPAGE/dashboard.html");
    }
    exit();
} else {
    echo "Usuario o contraseña incorrectos. <a href='login.html'>Volver</a>";
}
?>
