import requests
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, Entry, messagebox

def get_weather():
    city = entry_city.get()
    api_key = 'DEIN_API_SCHLÜSSEL_HIER'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}'

    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()

        weather_list = []
        for data in weather_data['list']:
            weather = {
                'Datum': data['dt_txt'],
                'Temperatur': data['main']['temp'],
                # Weitere relevante Informationen hier hinzufügen
            }
            weather_list.append(weather)

        weather_df = pd.DataFrame(weather_list)
        weather_df['Datum'] = pd.to_datetime(weather_df['Datum'])

        # Tabelle anzeigen
        top = Tk()
        top.title('Wetterdaten')
        table_label = Label(top, text=weather_df.to_string(), justify='left')
        table_label.pack()

        # Diagramm anzeigen
        plt.figure(figsize=(8, 5))
        plt.plot(weather_df['Datum'], weather_df['Temperatur'], marker='o', linestyle='-')
        plt.title('Temperaturverlauf')
        plt.xlabel('Datum und Uhrzeit')
        plt.ylabel('Temperatur in °C')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    else:
        messagebox.showerror('Fehler', 'Fehler beim Abrufen der Daten. Überprüfe deine Eingabe und den API-Schlüssel.')

# GUI erstellen
root = Tk()
root.title('Wetterdaten Abrufen')

label = Label(root, text='Stadt:')
label.pack()

entry_city = Entry(root)
entry_city.pack()

get_button = Button(root, text='Wetterdaten abrufen', command=get_weather)
get_button.pack()

root.mainloop()
