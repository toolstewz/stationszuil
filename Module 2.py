import time
import psycopg2
import random

moderatorID = random.choice(range(0,1500))

datum_beoordeling = time.strftime('%Y-%m-%d', time.localtime())
tijd_beoordeling = time.strftime('%I:%M:%S', time.localtime())

conn = psycopg2.connect(
    host = 'localhost',
    database = 'Stationszuil',
    user = 'postgres',
    password = 'Gerard13'
)


moderator_naam = input('Wat is uw naam? ')
moderator_mail = input('Wat is uw email? ')


with conn.cursor() as cursor:
    cursor.execute(
        f"""INSERT INTO moderator (moderatorid, email_adres, naam) 
        VALUES ({moderatorID}, '{moderator_mail}', '{moderator_naam}')"""
        )

    conn.commit()

with open('berichten.csv', 'r') as f:
    lines = f.read().splitlines()[1:]
    for line in lines:
        print(line)

        check = str(input('Is het een goed bericht: True / False? '))

        elements = line.split(',')

        berichtnummer = elements[0]
        bericht = elements[1]
        datum_bericht = elements[2]
        tijd_bericht = elements[3]
        naam = elements[4]
        station = elements[5]

        with conn.cursor() as l:
            l.execute(
                f"""INSERT INTO bericht (berichtnummer, inhoud, datum_bericht, tijd_bericht, naam_reiziger, datum_beoordeling, tijd_beoordeling, plaats, goedkeuring_bericht, moderatorid)
                VALUES ({berichtnummer}, '{bericht}', '{datum_bericht}', '{tijd_bericht}', '{naam}', '{datum_beoordeling}', '{tijd_beoordeling}', '{station}', {check}, {moderatorID})"""
                )    
        conn.commit()

with open('berichten.csv', 'w') as remove:
    remove.write(f'berichtnummer, bericht, datum, tijd, naam, station \n')




