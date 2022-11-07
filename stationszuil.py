import tkinter
import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    database = 'Stationszuil',
    user = 'postgres',
    password = 'Gerard13'
)

#laatste 5 berichten worden op chronologische volgorde laten zien:
with conn.cursor() as cursor:
    cursor.execute(
        """SELECT inhoud FROM bericht ORDER BY goedkeuring_bericht = 'true' DESC LIMIT 5"""
    )
    
    rows = cursor.fetchall()

    result = [row[0] for row in rows]

    window = tkinter.Tk()
    window.title("Stationszuil")
    window.geometry("1366x768")
    # window.config(bg='white')

    def tab1():
        def tab2():
            page1_text.destroy()
            b1.destroy()

            label1 = tkinter.Label(window, text = result[0], font=("NSfont", 30, "bold"))
            label1.pack(ipadx=10, ipady=5)
            label2 = tkinter.Label(window, text = result[1], font=("NSfont", 30, "bold"))
            label2.pack(ipadx=10, ipady=5)
            label3 = tkinter.Label(window, text = result[2], font=("NSfont", 30, "bold"))
            label3.pack(ipadx=10, ipady=5)
            label4 = tkinter.Label(window, text = result[3], font=("NSfont", 30, "bold"))
            label4.pack(ipadx=10, ipady=5)
            label5 = tkinter.Label(window, text = result[4], font=("NSfont", 30, "bold"))
            label5.pack(ipadx=10, ipady=5)

            def back():
                label1.destroy()
                label2.destroy()
                label3.destroy()
                label4.destroy()
                label5.destroy()
                b2.destroy()
                tab1() 
            b2 = tkinter.Button(window, text='Thuispagina', font=("NSfont", 15), command=back)
            b2.pack(side="bottom")

        page1_text = tkinter.Label(window, text="Welkom bij de NS", font=("NSfont", 40, "bold"))
        page1_text.pack(ipadx = 10, ipady= 10)
        b1 = tkinter.Button(window, text='Berichten', font=("NSfont", 15), command=tab2)
        b1.pack(side="bottom")
    tab1()

    window.mainloop() 






