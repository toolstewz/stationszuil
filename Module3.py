import tkinter
from PIL import Image, ImageTk
import json
import requests
import psycopg2

#connect database:
conn = psycopg2.connect(
    host="localhost", database="Stationszuil", user="postgres", password="Gerard13"
)

with conn.cursor() as cursor:
    cursor.execute(
        """SELECT inhoud, plaats FROM bericht WHERE goedkeuring_bericht = 'true' ORDER BY tijd_bericht DESC LIMIT 5"""
    )

    rows = cursor.fetchall()

    inhoud = [row[0] for row in rows]
    stations = [row[1] for row in rows]

    print(stations)

#laat berichten op chronologische volgorde zien
def berichten(inhoud):
    bericht1 = inhoud[0]
    bericht2 = inhoud[1]
    bericht3 = inhoud[2]
    bericht4 = inhoud[3]
    bericht5 = inhoud[4]

    format = " %s \n\n %s \n \n%s \n\n %s \n \n%s" % (
        bericht1,
        bericht2,
        bericht3,
        bericht4,
        bericht5,
    )
    return format


print(berichten(inhoud))


def format_response(weather):
    name = weather["name"]
    description = weather["weather"][0]["description"]
    temp = weather["main"]["temp"]

    forecast = "City: %s, Conditions: %s, Temperature (°C): %s" % (
        name,
        description,
        temp,
    )
    return forecast


def get_information(city):
    weather_information = get_weather(city)

    # haal faciliteiten op
    with conn.cursor() as tweede:
        tweede.execute(
            f"""SELECT ov_bike, elevator, toilet, park_and_ride FROM station_service WHERE station_city = '{city}'"""
        )

        faciliteiten = tweede.fetchone()

        ov_bike = faciliteiten[0]
        elevator = faciliteiten[1]
        toilet = faciliteiten[2]
        park_and_ride = faciliteiten[3]

    faciliteiten_information = "Facilities: "

    if ov_bike == True:
        faciliteiten_information += "OV-bike "
    if elevator == True:
        faciliteiten_information += "Elevator "
    if toilet == True:
        faciliteiten_information += "Toilet "
    if park_and_ride == True:
        faciliteiten_information += "P&R"

    label["text"] = faciliteiten_information + "\n" +  weather_information

#haalt data op van api.openweathermap.org
def get_weather(city):
    weather_key = "c8bd17b214573ae71418943906492149"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key, "q": city, "units": "metric"}
    response = requests.get(url, params=params)
    weather = response.json()

    anderelabel["text"] = berichten(inhoud)
    return format_response(weather)


window = tkinter.Tk()
window.title("Stationszuil")
window.geometry("1366x768")
window.config(bg="blue")

color_frame = tkinter.Frame(window, bg="#f7d417")
color_frame.place(relx=0.15, relwidth=1, relheight=1)


button_frame = tkinter.Frame(window, bg="#e0e0de")
button_frame.place(relx=0.17, rely=0.15, relwidth=0.7, relheight=0.8)

button = tkinter.Button(
    button_frame,
    text="Stationshalscherm",
    font=("NSfont", 13),
    command=lambda: get_information(entry.get()),
)
button.place(relx=1, rely=0.03, relwidth=0.20, relheight=0.08, anchor="e")

label = tkinter.Label(
    window, text="Welkom bij de NS", font=("NSfont", 35, "bold"), bg="#f7d417"
)
label.pack(ipadx=10, ipady=10)

entry = tkinter.Entry(button_frame, bg="white", font=("NSfont", 15))
entry.pack(ipadx=7, ipady=7)


anderelabel = tkinter.Label(button_frame, font=("NSfont", 20, "bold"), bg="#e0e0de")
anderelabel.place(relx=0.09, rely=0.12, relwidth=0.8, relheight=0.7)

label = tkinter.Label(button_frame, font=("NSfont", 14), bg="#e0e0de")
label.pack(side="bottom")


window.mainloop()