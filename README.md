# Geocoder
Geocoder for CSV files. Written in Python 3.

## Introduction
### What is Geocoding?
Geocoding is the process of converting addresses (like "1600 Amphitheatre Parkway, Mountain View, CA") into geographic coordinates (like latitude 37.423021 and longitude -122.083739), which you can use to place markers on a map, or position the map.

## Requirements
* **Python 3**: To run the script it is necessary to have installed any version of python 3. You can download the latest version [here](https://www.python.org/downloads).
* **Google Maps Geocoding API key**: In order to obtain the coordinates, it is necessary to have an API key for a project that has Google Maps Geocoding API enabled. If you do not have one, you can get one [here](https://developers.google.com/maps/documentation/geocoding/get-api-key).
* **CSV file with address list with UTF-8 encoding**: Each address must occupy a single row and can occupy more than one column. For example:

<table>
	<tr>
		<th>Address</th>
	</tr>
	<tr>
		<td>2146 Keller Crescent Union NJ 07083</td>
	</tr>
	<tr>
		<td>705 Old Fallston Rd Fallston MD 21047</td>
	</tr>
	<tr>
		<td>1216 Oakshire Ln Kirkwood Missouri 63122</td>
	</tr>
	<tr>
		<td>61 Atlantic St Stamford CT 06901</td>
	</tr>
	<tr>
		<td>124 Ash Ave Findlay Ohio 45840</td>
	</tr>
</table>

## Instructions
1. Create an environment variable **GOOGLE\_MAPS\_GEOCODING\_API\_KEY** with the value of the API key.
2. Run the next command to start the script:

	``` 
	python3 geocoder.py example.csv
	```
3. The result will be generated in the file **output\_example.csv** like this:

<table>
	<tr>
		<th>Address</th>
		<th>Latitude</th>
		<th>Longitude</th>
	</tr>
	<tr>
		<td>2146 Keller Crescent Union NJ 07083</td>
		<td>40.7135534</td>
		<td>-74.2644933</td>
	</tr>
	<tr>
		<td>705 Old Fallston Rd Fallston MD 21047</td>
		<td>39.5073035</td>
		<td>-76.4051319</td>
	</tr>
	<tr>
		<td>1216 Oakshire Ln Kirkwood Missouri 63122</td>
		<td>38.5622740</td>
		<td>-90.4124120</td>
	</tr>
	<tr>
		<td>61 Atlantic St Stamford CT 06901</td>
		<td>41.0545296</td>
		<td>-73.5395942</td>
	</tr>
	<tr>
		<td>124 Ash Ave Findlay Ohio 45840</td>
		<td>41.0499991</td>
		<td>-83.6490571</td>
	</tr>
</table>

## Acknowledgments
Many thanks to [Javier Luna](https://github.com/JavierLuna) for helping me as always.


David