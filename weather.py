from flask import Flask, render_template, request
import requests
from tkinter import messagebox

app = Flask(__name__)


@app.route('/climate', methods=['POST'])
def temperature():
    latitude=request.form['latitude']
    longitude=request.form['longitude']
    latitude,y_dir=latitude.split()
    longitude,x_dir=longitude.split()
    if x_dir not in ('e','E','w','W'):
        messagebox.showwarning(title="Warning", message="Kindly enter correct latitude and longitude values")
    if y_dir not in ('n','N','s','S'):
        messagebox.showwarning(title="Warning", message="Kindly enter correct latitude and longitude values")
        
    if y_dir=='S' or y_dir=='s':
        latitude=str(-abs(float(latitude)))
    if x_dir=='W' or x_dir=='w':
        longitude=str(-abs(float(longitude)))
         
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat='+latitude+'&lon='+longitude+'&appid=9ba94414c6d5291f735ec4c691e68930')
    json_object = r.json()
    #print(json_object)
    temp_k = float(json_object['main']['temp'])
    location=json_object['name']
    temp_c = (temp_k - 273.15)
    
    # if request.form['kelvin_to_celsius']=='Convert to Celsius':
    #     temp_c = (temp_k - 273.15)
    #     return render_template('index.html', place=location, temp=round(temp_c,2))
    # if request.form['kelvin_to_fahrenheit']=='Convert to Fahrenheit':
    #     temp_f = (temp_k - 273.15) * 1.8 + 32
    #     return render_template('index.html', place=location, temp=round(temp_f,2))   
 
    return render_template('climate.html', place=location, temp=round(temp_c,2))
    
@app.route('/')
def index(): 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)