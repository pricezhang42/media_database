#import library
import pyodbc
import pandas as pd

# Connect to database
myconn = pyodbc.connect("Driver={SQL Server};"
                      "Server=LAPTOP-PG4Q56MI\SQLEXPRESS;"
                      "Database=chinook;"
                      "Trusted_Connection=yes;")
cursor = myconn.cursor()

table = pd.read_csv('csv\Genre.csv')
table['GenreId'] = pd.to_numeric(table['GenreId'], downcast='integer')

try:
    # insert bulk data into the table , use parameter ? to prevent sql injection
    query = "INSERT INTO Genre (GenreId, Name) values(?,?)"
    for index, row in table.iterrows():
        row = row.where(pd.notnull(row), None)
        print(row)
        cursor.execute(query, row.GenreId, row.Name)
        myconn.commit()
        print( str(index+1) + ' Rows inserted')
    
    #select number of record from the table to confirm insertiion
    count=cursor.execute("select count(*) from Genre")
    rst=cursor.fetchval()
    print('there are ' + str(rst) + ' rows in the table')
except:
    print("Attempt Unsuccessful") 


table = pd.read_csv('csv\MediaType.csv')
table['MediaTypeId'] = pd.to_numeric(table['MediaTypeId'], downcast='integer')

try:
    # insert bulk data into the table , use parameter ? to prevent sql injection
    query = "INSERT INTO MediaType (MediaTypeId, Name) values(?,?)"
    for index, row in table.iterrows():
        row = row.where(pd.notnull(row), None)
        print(row)
        cursor.execute(query, row.MediaTypeId, row.Name)
        myconn.commit()
        print( str(index+1) + ' Rows inserted')
    
    #select number of record from the table to confirm insertiion
    count=cursor.execute("select count(*) from MediaType")
    rst=cursor.fetchval()
    print('there are ' + str(rst) + ' rows in the table')
except:
    print("Attempt Unsuccessful") 


table = pd.read_csv('csv\Artist.csv')
table['ArtistId'] = pd.to_numeric(table['ArtistId'], downcast='integer')

try:
    # insert bulk data into the table , use parameter ? to prevent sql injection
    query = "INSERT INTO Artist (ArtistId, Name) values(?,?)"
    for index, row in table.iterrows():
        row = row.where(pd.notnull(row), None)
        print(row)
        cursor.execute(query, row.ArtistId, row.Name)
        myconn.commit()
        print( str(index+1) + ' Rows inserted')
    
    #select number of record from the table to confirm insertiion
    count=cursor.execute("select count(*) from Artist")
    rst=cursor.fetchval()
    print('there are ' + str(rst) + ' rows in the table')
except:
    print("Attempt Unsuccessful") 


table = pd.read_csv('csv\Album.csv')
table['AlbumId'] = pd.to_numeric(table['AlbumId'], downcast='integer')
table['ArtistId'] = pd.to_numeric(table['ArtistId'], downcast='integer')

try:
    # insert bulk data into the table , use parameter ? to prevent sql injection
    query = "INSERT INTO Album (AlbumId, Title, ArtistId) values(?,?,?)"
    for index, row in table.iterrows():
        row = row.where(pd.notnull(row), None)
        print(row)
        cursor.execute(query, row.AlbumId, row.Title, row.ArtistId)
        myconn.commit()
        print( str(index+1) + ' Rows inserted')
    
    #select number of record from the table to confirm insertiion
    count=cursor.execute("select count(*) from Album")
    rst=cursor.fetchval()
    print('there are ' + str(rst) + ' rows in the table')
except:
    print("Attempt Unsuccessful") 


table = pd.read_csv('csv\Track.csv')
table['TrackId'] = pd.to_numeric(table['TrackId'], downcast='integer')
table['AlbumId'] = pd.to_numeric(table['AlbumId'], downcast='integer')
table['MediaTypeId'] = pd.to_numeric(table['MediaTypeId'], downcast='integer')
table['GenreId'] = pd.to_numeric(table['GenreId'], downcast='integer')
table['Milliseconds'] = pd.to_numeric(table['Milliseconds'], downcast='integer')
table['Bytes'] = pd.to_numeric(table['Bytes'], downcast='integer')

try:
    # insert bulk data into the table , use parameter ? to prevent sql injection
    query = "INSERT INTO Track (TrackId, Name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, UnitPrice) values(?,?,?,?,?,?,?,?,?)"
    for index, row in table.iterrows():
        row = row.where(pd.notnull(row), None)
        print(row)
        cursor.execute(query, row['TrackId'], row['Name'], row['AlbumId'], row['MediaTypeId'], row['GenreId'], row['Composer'], row['Milliseconds'], row['Bytes'], row['UnitPrice'])
        myconn.commit()
        print( str(index+1) + ' Rows inserted')
    
    #select number of record from the table to confirm insertiion
    count=cursor.execute("select count(*) from Track")
    rst=cursor.fetchval()
    print('there are ' + str(rst) + ' rows in the table')
except:
    print("Attempt Unsuccessful") 


table = pd.read_csv('csv\Employee.csv')
table['EmployeeId'] = pd.to_numeric(table['EmployeeId'], downcast='integer')
table['ReportsTo'] = pd.to_numeric(table['ReportsTo'], downcast='integer')

try:
    # insert bulk data into the table , use parameter ? to prevent sql injection
    query = "INSERT INTO Employee (EmployeeId, LastName, FirstName, Title, ReportsTo, BirthDate, HireDate, Address, City, State, Country, PostalCode, Phone, Fax, Email) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    for index, row in table.iterrows():
        row = row.where(pd.notnull(row), None)
        print(row)
        cursor.execute(query, row['EmployeeId'], row['LastName'], row['FirstName'], row['Title'], row['ReportsTo'], row['BirthDate'], row['HireDate'], row['Address'], row['City'], row['State'],row['Country'],row['PostalCode'],row['Phone'],row['Fax'],row['Email'])
        myconn.commit()
        print( str(index+1) + ' Rows inserted')
    
    #select number of record from the table to confirm insertiion
    count=cursor.execute("select count(*) from Employee")
    rst=cursor.fetchval()
    print('there are ' + str(rst) + ' rows in the table')
except Exception as err:
    print("Attempt Unsuccessful") 
    print(err)



table = pd.read_csv('csv\Customer.csv')
table['CustomerId'] = pd.to_numeric(table['CustomerId'], downcast='integer')
table['SupportRepId'] = pd.to_numeric(table['SupportRepId'], downcast='integer')

try:
    # insert bulk data into the table , use parameter ? to prevent sql injection
    query = "INSERT INTO Customer (CustomerId, FirstName, LastName, Company, Address, City, State, Country, PostalCode, Phone, Fax, Email, SupportRepId) values(?,?,?,?,?,?,?,?,?,?,?,?,?)"
    for index, row in table.iterrows():
        row = row.where(pd.notnull(row), None)
        print(row)
        cursor.execute(query, row['CustomerId'], row['FirstName'], row['LastName'], row['Company'], row['Address'], row['City'], row['State'], row['Country'], row['PostalCode'],row['Phone'],row['Fax'],row['Email'],row['SupportRepId'])
        myconn.commit()
        print( str(index+1) + ' Rows inserted')
    
    #select number of record from the table to confirm insertiion
    count=cursor.execute("select count(*) from Customer")
    rst=cursor.fetchval()
    print('there are ' + str(rst) + ' rows in the table')
except Exception as err:
    print("Attempt Unsuccessful") 
    print(err)


table = pd.read_csv('csv\Invoice.csv')
table['InvoiceId'] = pd.to_numeric(table['InvoiceId'], downcast='integer')
table['CustomerId'] = pd.to_numeric(table['CustomerId'], downcast='integer')

try:
    # insert bulk data into the table , use parameter ? to prevent sql injection
    query = "INSERT INTO Invoice (InvoiceId, CustomerId, InvoiceDate, BillingAddress, BillingCity, BillingState, BillingCountry, BillingPostalCode, Total) values(?,?,?,?,?,?,?,?,?)"
    for index, row in table.iterrows():
        row = row.where(pd.notnull(row), None)
        print(row)
        cursor.execute(query, row['InvoiceId'], row['CustomerId'], row['InvoiceDate'], row['BillingAddress'], row['BillingCity'], row['BillingState'], row['BillingCountry'], row['BillingPostalCode'], row['Total'])
        myconn.commit()
        print( str(index+1) + ' Rows inserted')
    
    #select number of record from the table to confirm insertiion
    count=cursor.execute("select count(*) from Invoice")
    rst=cursor.fetchval()
    print('there are ' + str(rst) + ' rows in the table')
except Exception as err:
    print("Attempt Unsuccessful") 
    print(err)


table = pd.read_csv('csv\InvoiceLine.csv')
table['InvoiceLineId'] = pd.to_numeric(table['InvoiceLineId'], downcast='integer')
table['InvoiceId'] = pd.to_numeric(table['InvoiceId'], downcast='integer')
table['TrackId'] = pd.to_numeric(table['TrackId'], downcast='integer')
table['Quantity'] = pd.to_numeric(table['Quantity'], downcast='integer')

try:
    # insert bulk data into the table , use parameter ? to prevent sql injection
    query = "INSERT INTO InvoiceLine (InvoiceLineId, InvoiceId, TrackId, UnitPrice, Quantity) values(?,?,?,?,?)"
    for index, row in table.iterrows():
        row = row.where(pd.notnull(row), None)
        print(row)
        cursor.execute(query, row['InvoiceLineId'], row['InvoiceId'], row['TrackId'], row['UnitPrice'], row['Quantity'])
        myconn.commit()
        print( str(index+1) + ' Rows inserted')
    
    #select number of record from the table to confirm insertiion
    count=cursor.execute("select count(*) from InvoiceLine")
    rst=cursor.fetchval()
    print('there are ' + str(rst) + ' rows in the table')
except Exception as err:
    print("Attempt Unsuccessful") 
    print(err)


table = pd.read_csv('csv\Playlist.csv')
table['PlaylistId'] = pd.to_numeric(table['PlaylistId'], downcast='integer')

try:
    # insert bulk data into the table , use parameter ? to prevent sql injection
    query = "INSERT INTO Playlist (PlaylistId, Name) values(?,?)"
    for index, row in table.iterrows():
        row = row.where(pd.notnull(row), None)
        print(row)
        cursor.execute(query, row['PlaylistId'], row['Name'])
        myconn.commit()
        print( str(index+1) + ' Rows inserted')
    
    #select number of record from the table to confirm insertiion
    count=cursor.execute("select count(*) from Playlist")
    rst=cursor.fetchval()
    print('there are ' + str(rst) + ' rows in the table')
except Exception as err:
    print("Attempt Unsuccessful") 
    print(err)


table = pd.read_csv('csv\PlaylistTrack.csv')

try:
    # insert bulk data into the table , use parameter ? to prevent sql injection
    query = "INSERT INTO PlaylistTrack (PlaylistId, TrackId) values(?,?)"
    for index, row in table.iterrows():
        row = row.where(pd.notnull(row), None)
        print(row)
        cursor.execute(query, int(row['PlaylistId']), int(row['TrackId']))
        myconn.commit()
        print( str(index+1) + ' Rows inserted')
    
    #select number of record from the table to confirm insertiion
    count=cursor.execute("select count(*) from PlaylistTrack")
    rst=cursor.fetchval()
    print('there are ' + str(rst) + ' rows in the table')
except Exception as err:
    print("Attempt Unsuccessful") 
    print(err)

#close the connection
myconn.close() 




