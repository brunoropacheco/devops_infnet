<!DOCTYPE html>
<html >
<?php
	ini_set('display_errors', 1);
	ini_set('display_startup_errors', 1);
	error_reporting(E_ALL);
	$servidor = 'banco_ap';
	$usuario = 'root';
	$senha = 'Noki@500';
	$banco = "pup";
  $mysqli = new mysqli($servidor, $usuario, $senha, $banco);
  $query = "SELECT * FROM membros";
	$result = mysqli_query($mysqli, $query);
?>
<head>
  <meta charset="UTF-8">
  <title>PickUp Presence</title>
      <link rel="stylesheet" href="css/style.css">
</head>

<body>
  <section>
  <!--for demo wrap-->
  <h1>PickUp Presence SmartTel Jr</h1>
  <div class="tbl-header">
    <table cellpadding="0" cellspacing="0" border="0">
      <thead>
        <tr>
          <th>Nome</th>
          <th>Departamento</th>
          <th>MAC Address</th>
          <th>Esta Presente</th>
          <th>Visto Ultima Vez</th>
        </tr>
      </thead>
    </table>
  </div>
  <div class="tbl-content">
    <table cellpadding="0" cellspacing="0" border="0">
      <tbody>
        <?php while ($row = mysqli_fetch_array($result)){?>
          <tr>
      		<td>
      		    <?php echo $row['Nome'];?>
      		</td>
          <td>
      		    <?php echo $row['Departamento'];?>
      		</td>
      		<td>
      		    <?php echo $row['MAC_Address'];?>
      		</td>
          <td>
            <?php echo ($row['Presenca'] == 1) ? 'sim' : 'nao'; ?>
          </td>
          <td>
      		    <?php echo $row['Visto_Ultima_Vez'];?>
      		</td>
      		</td>
      		</tr>
      		<?php } ?>
      </tbody>
    </table>
  </div>
</section>


<!-- follow me template -->
<div class="made-with-love">
  Made with
  <i>♥</i> by
  <a target="_blank" href="https://codepen.io/nikhil8krishnan">Nikhil Krishnan</a>
</div>
  <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>

    <script src="js/index.js"></script>

</body>
<?
  mysqli_close($mysqli);
?>
</html>
