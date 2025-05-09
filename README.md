## Database for a Digital Media Store 

A database system built with SQL Server to manage record information and sales data for a digital media store along with a Python-based user interface for executing SQL queries. 
### Summary of the Data
The Chinook data model represents a digital media store, including the media, their customers and employees, and their invoice information.
•	Media-related data was created using real data from an Apple iTunes library.
•	Customer and employee information was created using fictitious names and addresses that can be located on Google maps, and other well formatted data (phone, fax, email, etc.)
•	Sales information was auto generated using random data for a four-year period.

The Chinook sample database includes:
•	11 tables
•	A variety of indexes, primary and foreign key constraints
•	Over 15,000 rows of data

Figure 1. ER Model
![alt text](/images/ER%20model.jpg)

Figure 2 - EER Diagram
![alt text](/images/EER%20diagram.jpg)

### Setup
Follow the steps below to create and populate the database. Note that it is important to change the “server” line within tables.py and insert.py before running.
1. First create an empty database with the name, “chinook” in Microsoft SQL Server.
2. Next, create tables and relationships by running tables.py. The dataset is stored in the filepath “./csv”.
3. Then populate the tables by running insert.py.

### Interface
The interface is implemented by Python with PySimpleGUI. To run the interface, first install the regular PySimpleGUI port:
```
$ python -m pip install pysimplegui
```
Then run interface.py. Note that if the application fails to connect to the database, the window will freeze for several seconds before an error window pops up. Please wait a few seconds before retrying. 
Once the connection succeeds, the application will then render the main window.

Fig 1. Connecting to the interface

![alt text](/images/Interface1.jpg)

Fig 2. Main Interface Window

![alt text](/images/Interface2.jpg)

#### Interesting Queries
Some of the interesting queries that our program can execute are:
● Selecting the Top 5 best selling artists.
● Searching by any artists present in the database by their name.
● Getting all of the albums, sales figures, and genres that an artist makes.
● The names of all the customers who have purchased a single or album from an artist in a country.

We found these queries to be interesting because they leverage SQL to summarize data that isn’t readily available. Each of the queries yield values that bridge at least three different relationships and give the user insight into important information that would be useful to a music industry insider.

Fig 4. Top 5 Best Selling Artists

![alt text](/images/Interface3.jpg)


#### Appendix
Source data was obtained from the Chinook sample database using the Microsoft Public License (Ms-PL).
https://github.com/w3c/csvw/tree/gh-pages/examples/tests/scenarios/chinook
EER Diagram image was made using ERDPlus.
https://erdplus.com/