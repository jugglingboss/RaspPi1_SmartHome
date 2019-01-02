<!DOCTYPE html>
<html>
<head>
	<title>Alarm Time</title>
	<style type="text/css">
	
		{
		margin:0;
		padding:0;
		}
		body{
			text-align:center;
			background-color:white;
			

			font-size:75px;
			font-family:Arial, Helvetica, sans-seriff;	
		}
		.left{
			float:left;
			width:29%;
			padding-bottom:620px;
			background-image:url('images/alarm.png');
			background-repeat:space;
			background-position:center 20px;
			background-size: Auto 394px;
		}
		.right{
			padding-bottom:620px;
			float:right;
			width:29%;
			background-image:url('images/alarm.png');
			background-repeat:space;
			background-position:center 20px;
			background-size: Auto 394px;
		}
		
		.title{margin-top:100px;}
		
		a{
			text-decoration:none;
			color:#00ffee;	
		}
		a:hover{color:red;}
		p{
			color:#00ffee;
		}
		
	</style>
	
</head>
<body>
	<div class="left">
		
	</div>
	<div class = "right">
		
	</div>
	<header class="title">	
		<p> Alarm Time </p>
		<?php 
		$filename = "Data.txt";
		 
		$file_content = file($filename); 
		$x = count($file_content); 
		$fp = fopen($filename, "w+");  
		$file_content[2] = $_POST["time"]; 
		if ($file_content[2]){
			echo $_POST["time"];	
		}else{
			echo "Alarm Off";
			$file_content[2] = "Off";
		}
		
		$y = 0; 

		while($y < $x) 
		{ 
		fwrite($fp, $file_content[$y]); 
		$y++; 
		} 
		fclose($fp);  

		?>
		<p><p>
		<a href="http://jugglingboss.hopto.org">Home Page</a>
	</header>
	
	
</body>
</html>