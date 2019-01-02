<!DOCTYPE html>
<html>
<head>

	<title>Playing Music</title>
	<style type="text/css">
		body{
			text-align:center;
			background-color:black;
			background-image:url('images/play2.jpg');
			background-repeat:no-repeat;
			background-position:center -25px;
			background-size: Auto 700px;
			
			color:white;
			font-size:75px;
			font-family:Arial, Helvetica, sans-seriff;	
		}
		.title{margin-top:275px;}
		
		a{
			text-decoration:none;
			color:white;	
		}
		a:hover{color:red;}
		.php{
			color:red;
			font-size:150px;
			margin-top:-300px;
		}
		
	</style>

</head>
<body>
	<header class="title">	
		<a href="http://jugglingboss.hopto.org">Home Page</a>
	</header>
	<div class="php">
		<?php	
			$file = '/var/www/html/Data.txt';
			$search = 'Music is On';
			
			$result = 0;
			$lines = file('/var/www/html/Data.txt');
			foreach($lines as $line)
			{
			  // Check if the line contains the string we're looking for, and print if it does
			  if(strpos($line, $search) !== false)
			    $result = 1;
				
			}
			if($result == 1)
				echo "Already on, Skipping Song";
			else{
				
		
				$content = file_get_contents($file);
				
			
				$content = str_replace('Music is Off', 'Music is On', $content);
				$handle = fopen($file, 'w') or die('Cannot open file:  '.$file);
				fwrite($handle, $content);
				fclose($handle);
			}
		?>
	</div>


	
</body>
</html>