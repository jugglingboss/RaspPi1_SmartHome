
<!DOCTYPE html>
<html>
<head>	
	<title>Climate Control</title>
	<style type="text/css">
		body{
			text-align:center;
			background-color:#01054c;
			color:white;
			font-size:75px;
			font-family:Arial, Helvetica, sans-seriff;
			
		}
		
		h1{margin-top:100px;}
		.link{margin-top:-50px;}
		a{
			text-decoration:none;
			color:#00ffee;
		}
		a:hover{color:red;}
		p{
			margin-top:90px;
			color:#00ffee;
			font-size:40px;
		}
		.php{
			color:red;
			font-size:120px;
			
		}
	</style>

</head>
<body>
	<div class="php">
		<?php	
			echo exec("python /var/www/html/PythonScripts/pythonMQTTair.py");
			
		?>
	</div>
	<header class="title">
		<h1>On/Off Button Clicked</h1>
			<div class="link">
				<a href="http://jugglingboss.hopto.org">Home Page</a>
			</div>
	</header>
	<p id="demo"></p>

	
</body>
</html>