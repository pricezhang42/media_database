# interface.py
import pyodbc
import pandas as pd
import PySimpleGUI as sg

# ----- Full layout -----
open_row = [
    [
        sg.Text("Connect to Database:"),
    ],
    [
        sg.Text("Server:    "),
        sg.In(size=(20, 1), enable_events=True, key="-Connection-"),
    ],
    [
        sg.Text("Database:"),
        sg.In(size=(20, 1), enable_events=True, key="-Database-"),
    ],
    [
        sg.Button("Connect", key="-Connect-"),
    ]
]

first_row = [
    [
        sg.Text("Artist:"),
        sg.In(size=(20, 1), enable_events=True, key="-Artist1-"),
        sg.Button("Search", key="-Artist1B-"),
        sg.Button("Top 5 Best Selling Artists", key="-Top 5-")
    ],
    [
        sg.Text("Retrieve"),
        sg.Button("Albums", key="-AlbumB-"),
        sg.Button("Sales", key="-Sales-"),
        sg.Button("Genres", key="-Genres-"),
        sg.Text("of Above Artist"),
     ],
]
second_row = [
    [
        sg.Text("Retrieve people who bought a song from an artist in a country:")
    ],
    [
        sg.Text("Artist:   "),
        sg.In(size=(25, 1), enable_events=True, key="-Artist2-"),
        sg.Button("Search", key="-Artist2B-"),
    ],
    [
        sg.Text("Country:"),
        sg.In(size=(25, 1), enable_events=True, key="-Country-"),
        sg.Button("Search", key="-CountryB-"),
    ],
    [
        sg.Button("Run", key="-Run-")
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, horizontal_scroll=True, size=(58, 20), key="-LIST-"
        )
    ],
]

layout_open = [
    [
        [sg.Column(open_row)],
    ]
]

layout = [
    [
        [sg.Column(first_row)],
        [sg.HorizontalSeparator()],
        [sg.Column(second_row)],
    ]
]

window_open = sg.Window("Connect", layout_open)

ifConnected = False
# Connection window
# Run the Event Loop
while True:
    event, values = window_open.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "-Connect-":
        try:
            conn = 'Driver={{SQL Server}};Server={};Database={};Trusted_Connection=yes;'.format(values["-Connection-"],values["-Database-"])
            myconn = pyodbc.connect(conn)
            ifConnected = True
            break
        except pyodbc.Error as err:
            print(err)
            sg.popup("Connection Error")

window_open.close()

# Main window
window = sg.Window("Database Viewer", layout)
marker = ""
while ifConnected:
    try:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-Artist1B-":
            query = 'SELECT * FROM Artist where Name like CONCAT(?, \'%\')'
            dataR=pd.read_sql_query(sql=query,con=myconn,params=[values["-Artist1-"]])
            fnames = [list(dataR.columns.values)]
            fnames.extend(dataR.values.tolist())
            window["-LIST-"].update(fnames)
            marker = "-Artist1B-"
        elif event == "-LIST-" and (marker=="-Artist1B-" or marker=="-Top 5-"):
            print(values["-LIST-"][0][1])
            window.Element('-Artist1-').update(values["-LIST-"][0][1])
        elif event == "-AlbumB-":
            query = 'SELECT ar.ArtistId, Name, AlbumId, Title FROM Artist ar, Album al where ar.ArtistId=al.ArtistId AND ar.Name=?'
            dataR=pd.read_sql_query(sql=query,con=myconn,params=[values["-Artist1-"]])
            fnames = [list(dataR.columns.values)]
            fnames.extend(dataR.values.tolist())
            window["-LIST-"].update(fnames)
            marker = "-AlbumB-"
        elif event == "-Sales-":
            query = 'SELECT ar.ArtistId, ar.Name, SUM(i.Quantity) Sales FROM Artist ar, Album al, Track t, InvoiceLine i where ar.ArtistId=al.ArtistId AND t.AlbumId=al.AlbumId AND t.TrackId=i.TrackId AND ar.Name=? group by ar.ArtistId, ar.Name'
            dataR=pd.read_sql_query(sql=query,con=myconn,params=[values["-Artist1-"]])
            fnames = [list(dataR.columns.values)]
            fnames.extend(dataR.values.tolist())
            window["-LIST-"].update(fnames)
            marker = "-Sales-"
        elif event == "-Genres-":
            query = '''SELECT DISTINCT g.Name AS Genres FROM 
                       Artist A 
                       JOIN Album alb ON A.ArtistId = alb.ArtistId 
                       JOIN Track t ON alb.AlbumId = t.AlbumId 
                       JOIN Genre g ON g.GenreId = t.GenreId
                       WHERE A.Name = ?
                    '''
            dataR=pd.read_sql_query(sql=query,con=myconn,params=[values["-Artist1-"]])
            fnames = [list(dataR.columns.values)]
            fnames.extend(dataR.values.tolist())
            window["-LIST-"].update(fnames)
            marker = "-Genres-"
        elif event == "-Top 5-":
            query = 'SELECT TOP (5) ar.ArtistId, ar.Name, SUM(i.Quantity) Sales FROM Artist ar, Album al, Track t, InvoiceLine i where ar.ArtistId=al.ArtistId AND t.AlbumId=al.AlbumId AND t.TrackId=i.TrackId group by ar.ArtistId, ar.Name order by Sales Desc'
            dataR=pd.read_sql_query(query,myconn)
            fnames = [list(dataR.columns.values)]
            fnames.extend(dataR.values.tolist())
            window["-LIST-"].update(fnames)
            marker = "-Top 5-"
        elif event == "-Artist2B-":
            query = 'SELECT * FROM Artist where Name like CONCAT(?, \'%\')'
            dataR=pd.read_sql_query(sql=query,con=myconn,params=[values["-Artist2-"]])
            fnames = [list(dataR.columns.values)]
            fnames.extend(dataR.values.tolist())
            window["-LIST-"].update(fnames)
            marker = "-Artist2B-"
        elif event == "-LIST-" and marker=="-Artist2B-":
            print(values["-LIST-"][0][1])
            window.Element('-Artist2-').update(values["-LIST-"][0][1])
        elif event == "-CountryB-":
            query = 'SELECT distinct i.BillingCountry from Invoice i where i.BillingCountry like CONCAT(?, \'%\')'
            dataR=pd.read_sql_query(sql=query,con=myconn,params=[values["-Country-"]])
            fnames = [list(dataR.columns.values)]
            fnames.extend(dataR.values.tolist())
            window["-LIST-"].update(fnames)
            marker = "-CountryB-"
        elif event == "-LIST-" and marker=="-CountryB-":
            print(values["-LIST-"][0][0])
            window.Element('-Country-').update(values["-LIST-"][0][0])
        elif event == "-Run-":
            query = 'SELECT c.FirstName, c.LastName FROM Artist ar, Album al, Track t, InvoiceLine i, Invoice inv, Customer c where ar.ArtistId=al.ArtistId AND t.AlbumId=al.AlbumId AND t.TrackId=i.TrackId AND i.InvoiceId=inv.InvoiceId AND inv.CustomerId=c.CustomerId AND ar.Name=? AND inv.BillingCountry=? group by c.FirstName, c.LastName'
            dataR=pd.read_sql_query(sql=query,con=myconn,params=[values["-Artist2-"], values["-Country-"]])
            fnames = [list(dataR.columns.values)]
            fnames.extend(dataR.values.tolist())
            window["-LIST-"].update(fnames)
            marker = "-Run-"

    except Exception as err:
        print(err)

myconn.close() 
window.close()
