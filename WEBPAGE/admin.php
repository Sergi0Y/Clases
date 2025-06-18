<?php
// admin.php

$host = "localhost";
$usuario = "root";
$contrasena = "";
$bd = "evento_roblox";

$conn = new mysqli($host, $usuario, $contrasena, $bd);

if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Consulta para obtener todos los registros
$sql = "SELECT * FROM participantes";
$resultado = $conn->query($sql);
?>

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Formulario eva2</title>
    <link rel="stylesheet" href="/WEBPAGE/Styles/styles.css" />
    <script src="js/script.js" defer></script>
</head>

<body>
    <h6>@autor: Isidora Paz Cisterna Vergara</h6>
    <!--  <div class="flor">
      <h4>Autorizado por Roblox y patentado por Rodny_Roblox</h4>
        <h1>MI CUENTA</h1>
            <img src="https://www.gizlogic.com/wp-content/uploads/2020/05/TodoRoblox-1536x864.png" width="460">            
    </div> -->
    <main class="main-container">
        <h1>ADMIN DASHBOARD</h1>
        <h2>Tabla de usuarios</h2>
        <table class="users-table">

            <thead>
                <tr>
                    <th>Id</th>
                    <th>nombre</th>
                    <th>Apellido</th>
                    <th>Email</th>
                    <th>Teléfono</th>
                    <th>Ciudad</th>
                    <th>Pais</th>
                    <th>Cd_frente</th>
                    <th>Cd_atras</th>
                    <th>Fecha registro</th>
                </tr>
            </thead>
             <tbody>
            <?php
            if ($resultado->num_rows > 0) {
                // Mostrar cada fila
                while($fila = $resultado->fetch_assoc()) {
                    echo "<tr>";
                    echo "<td>" . $fila['id'] . "</td>";
                    echo "<td>" . htmlspecialchars($fila['nombre']) . "</td>";
                    echo "<td>" . htmlspecialchars($fila['apellido']) . "</td>";
                    echo "<td>" . htmlspecialchars($fila['email']) . "</td>";
                    echo "<td>" . htmlspecialchars($fila['telefono']) . "</td>";
                    echo "<td>" . htmlspecialchars($fila['ciudad']) . "</td>";
                    echo "<td>" . htmlspecialchars($fila['pais']) . "</td>";
                    echo "<td>" . htmlspecialchars($fila['cd_frente']) . "</td>";
                    echo "<td>" . htmlspecialchars($fila['cd_atras']) . "</td>";
                    echo "<td>" . htmlspecialchars($fila['fecha_registro']) . "</td>";
                    echo "</tr>";
                }
            } else {
                echo "<tr><td colspan='9' style='text-align:center;'>No hay registros</td></tr>";
            }
            ?>
        </tbody>

        </table>
    </main>

    <img
        src="https://s.elyex.com/media/applinks/is/conseguir-robux-gratis1.webp"
        class="robux" />
    <!--espero mínimo un 8
https://media1.tenor.com/m/ALNgfWrgk1cAAAAC/sad-hamster-meme-sad-hamster.gif
agradecimiento a mis 4 gatos virtuales que me acompañaron en mi ascenso a la locura-->
    <script src="js/script.js"></script>
</body>

</html>


<?php
$conn->close();
?>