<!DOCTYPE html>
<!-- Hye Mi Kim 5044613 -->
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Calendar	Input</title>
    <link rel="stylesheet" type="text/css" href="my_style.css" />
  </head>
  <body>
  <?php 
  	$eventErr = $sTimeErr = $eTimeErr = $locErr = $dayErr = "";
  ?>


  <h1>Calendar Input</h1>
	<nav>
		<button onclick="window.location.href='calendar.php'">My Calendar</button>
		<button onclick="window.location.href='input.php'">Form Input</button>
	</nav>
	<br>
	<br>    
	<form method="get" action = "#">
		<table>
		<tr>
			<td><label>Event Name:</label></td>
			<td><input type="text" name="eventname"></td>
		</tr>
		<tr>
			<td><label>Start Time:</label></td>
			<td><input type="time" name="starttime"></td>
		</tr>
		<tr>
			<td><label> End Time:</label></td>
			<td><input type="time" name="endtime"></td>
		</tr>
		<tr>
			<td><label>Location:</label></td>
			<td><input type="text" name="location"></td>
		</tr>
		<tr>
			<td><label>Day of the week:</label></td>
			<td>
				<select name = "day">
					<option value="Mon">Mon</option>
					<option value="Tue">Tue</option>
					<option value="Wed">Wed</option>
					<option value="Thur">Thur</option>
					<option value="Fri">Fri</option>
				</select>
			</td>
		</tr>
		<tr>
			<td colspan="2"> 
				<input type = "submit" value = "Submit" >
				<input type = "reset" value = "Clear" >
			</td>
		</tr>
		</table>
		<br>
		<br>
	</form>
  </body>
</html>
  