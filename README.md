# automatic_import_csv_to_postgres_db
Python script to automatically create a new postgres database with tables based on csv files.

The script uses the following libraries: *os, pandas, psycopg2, sqlalchemy*
Can be executed from a terminal.


## Necessary User Inputs:
*Postgres Password* - to connect to psql host<br>
*New Database* - choose name for new database<br>
*CSV File Folder Name* - name of target folder that contains the csv files being the database foundation

## Usage Remarks
1. If a csv file name contains *uppercase letters*, the script creates a table accordingly. However, to access that table with an SQL query or in the terminal, the table needs to be referred to with doublequotes ("table_name"). I recommend making sure that the csv file name is in lowercase in order to make SQL querying more comfortable.
This does not pose a major problem to me at this point. In case it will, I might fix it by adding a few lines to just automatically rename all csv files in the target folder with Python's lower() method.
2. The code does not create PRIMARY KEY and FOREIGN KEY for the tables. They need to be set manually afterwards.
   


## Improvement Ideas
For this script to become a general program that can be used by various users, in various networks and scenarios, I'd make the following adjustments:

### Flexibility of User Inputs:
- Prompt user to choose entire path of csv files instead of only the folder (with autocompletion) 
- Prompt user to choose further postgres connection parameters (driver, host, user, port) besides database name and password
- Prompt user to choose whether they would like to add new indices to the csv files/table rows

### New Database vs. New Tables for Existing Database:
Instead of always creating a new database, it would be more useful to have the script check the existence of the user's prompted database name. And consequently have the following use options:
- Create new database
- Create additional tables in existing database
- Overwrite existing database
- Overwrite existing tables in existing database
<br>
PostgreSQL does not support CREATE DATABASE IF NOT EXISTS syntax and it is a little more complicated to achieve this, plus I personally do not need this function currently. This is why for now I have not yet adjusted the code to that.

### Testing:
Confirmation of correct functionality by implementing try/except/finally blocks (e.g. connection) and tests.

### Success Message:
- Connect the message to the successful operation of the script {success vs. error}
- Display each created table with information about its name as well as row and column count in a single line

