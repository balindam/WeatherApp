import tkinter as tk
from tkinter import  font
import requests
HEIGHT = 700
WIDTH = 800
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
# myapi daeceb7485df4fc88db2a44f341a9c37
# url api.openweathermap.org/data/2.5/weather?q={city name}
bg_image = tk.PhotoImage(file='landscape.png')
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

def formatResponse(weather):
    try:
        name = weather['name']
        desp = weather['weather'][0]['description']
        temp = str(weather['main']['temp'])
        resp = 'City: ' + name + '\n' + 'Condition: ' + desp + '\n' + 'Temperature: ' + temp + '°C'
    except:
        resp = 'Wrong city entered or can\'t fetch data'
    return resp

def getWeather(city):
    # print(city)
    api_key = 'daeceb7485df4fc88db2a44f341a9c37'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': api_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = formatResponse(weather)


frame = tk.Frame(root, bg='#80c1ff', bd=4)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('courier', 20), bg='black', fg='white')
entry.place(relheight=1, relwidth=.7)

button = tk.Button(frame, text="Show Weather", command=lambda: getWeather(entry.get()), font=('courier', 15))
button.place(relx=.75, relheight=1, relwidth=0.25)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.65, anchor='n')

label = tk.Label(lower_frame, bd=4, font=('courier', 20), anchor='nw', justify='left', bg='black', fg='white')
label.place(relheight=1, relwidth=1)

root.mainloop()