
<!DOCTYPE html>
<html>
<head>	
	<title>Closing Blinds</title>
	<style type="text/css">
		body{
			text-align:center;
			background-color:black;
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
			$file = 'Data.txt';
			$search = 'Blinds are Opened';
			
			$result = 0;
			$lines = file('/var/www/html/Data.txt');
			foreach($lines as $line)
			{
			  // Check if the line contains the string we're looking for, and print if it does
			  if(strpos($line, $search) !== false)
			    $result = 1;
				
			}
			if($result == 1)
				echo exec("python /var/www/html/PythonScripts/pythonMQTT2.py");
				
			else{
				echo "Error: Already Closed";
						
			}
		?>
	</div>
	<header class="title">
		<h1>Darkness</h1>
			<div class="link">
				<a href="http://jugglingboss.hopto.org">Home Page</a>
			</div>
	</header>
	<p id="demo"></p>

	<script>
	// Set the date we're counting down to
	
	var t = new Date();
	t.setSeconds(t.getSeconds() + 12.9);
	
	
	// Update the count down every 1 second
	var x = setInterval(function() {
	
	    // Get todays date and time
	    var now = new Date().getTime();
	    
	    // Find the distance between now an the count down date
	    var distance = t - now;
	    
	    // Time calculations for days, hours, minutes and seconds
	    var seconds = Math.floor(distance/1000)
	    
	    // Output the result in an element with id="demo"
	    
	    document.getElementById("demo").innerHTML = "Time Until Blinds Fully Close" + "<br/>" + seconds + "s ";
	    
	    // If the count down is over, write some text 
	    if (distance < 0) {
	        clearInterval(x);
		
	        document.getElementById("demo").innerHTML = "Blinds Closed";
	    }
	}, 1000);
	</script>
</body>
</html>