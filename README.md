# simple_weather-app
A simple flask application for checking temperature of a place using Latitude and Longitude as input

Here, Flask is used to create and run the the application on local server.

1. latitude and longitudes are taken as input from the user and then OpenWeatherMap API is used to get the response 
for the weather of that particular region.
2. The response from the API is then converted to json and the temperature and location are fetched from it.
3. The temperature fetched in Kelvin is converted to Degree Celsius.
4. The temperature along with the location is then displayed on the app as output.
