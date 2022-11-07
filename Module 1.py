#MODULE 1!!!!!!!!!!!!!!!!!!

import time
import random
datum = time.strftime('%Y-%m-%d', time.localtime())
tijd = time.strftime('%I:%M:%S', time.localtime())

#bericht wordt geopend 
#checkt of het bericht kort genoeg is
with open('berichten.csv', 'a') as f:
    while True:
        while True:
            bericht = str(input('Wat wilt u meegeven aan de NS? '))
            if len(bericht) > 140:
                vals_bericht = bericht
                print('Uw bericht mag maar een maximum van 140 karakters bevatten!')
            else:
                bericht = bericht
                break
        #kiest een willekeurig station uit
        with open('stations.txt', 'r') as file:
            text = file.read()
            stations = text.split()
            gekozen_station = random.choice(stations)

        #messenger kan zijn naam geven (of niet)
        naam = str(input('Wat is uw naam? '))
        if naam == '':
            naam = 'Anoniem'
        berichtnummer = random.choice(range(0,1500))

        print(f'{berichtnummer}, {bericht}, {datum}, {tijd}, {naam}, {gekozen_station}', file=f)

