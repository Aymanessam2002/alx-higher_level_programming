# Alx School - 0x0D-SQL_introduction

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/rtcwz.jpg)

## Setup
1. Install sql ``sudo apt-get install mysql-server``
2. Connect to your MySQL server
  1. ``~> mysql -hlocalhost -uroot -p``
  2. ``mysql> quit``
  3. ``Bye``

## New commands / functions used:
``mysql> help``, ``DDL``, ``DML``, ``CREATE``, ``ALTER``, ``SELECT``, ``INSERT``, ``UPDATE``, ``DELETE``

## Helpful Links
* [Youtube primer on MySQL](https://www.youtube.com/watch?v=FR4QIeZaPeM)
* [Basic MySQL tutorial](https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial)
* [Basic SQL Statements: DDL and DML](http://www.tomjewett.com/dbdesign/dbdesign.php?page=ddldml.php)
* [Basic SQL Queries: SQL and RA](http://www.tomjewett.com/dbdesign/dbdesign.php?page=queries.php)
* [SQL Technique: functions](http://www.tomjewett.com/dbdesign/dbdesign.php?page=functions.php)
* [SQL Technique: subqueries](http://www.tomjewett.com/dbdesign/dbdesign.php?page=subqueries.php)
* [Resource for SQL information: dev.mysql.com](https://dev.mysql.com/doc/refman/5.7/en/sql-syntax.html)

##  Requirements

### Python Scripts
*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be executed on Ubuntu 20.04 LTS using gcc, using python3 (version 3.8.5).
*   All your files should end with a new line.
*   All your files must be executable.
*	All your SQL queries should have a comment just before.
*	All your files should start by a comment describing the task.
*	All SQL keywords should be in uppercase (`SELECT`, `WHERE`…).
*   The length of your files will be tested using `wc`.

## Project Description
Learn what’s a database.
What’s a relational database.
What does SQL stand for.
What’s MySQL.
How to create a database in MySQL.
What does `DDL` and `DML` stand for.
How to `CREATE` or `ALTER` a table.
How to `SELECT` data from a table.
How to `INSERT`, `UPDATE` or `DELETE` data.
What are subqueries.
How to use MySQL functions.

Examples of how to run your files:
```
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                  
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ 
```

The database name will be passed as an argument to the mysql command.
```
guillaume@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Tables_in_hbtn_0c_0
first_table
guillaume@ubuntu:~/$  
```

## Introduction to databases

|                  File                                    |                     Description                     |
| :-----------------------------------------: |  :-----------------------------------------------:  |
|   0-list_databases.sql                      |  List all databases of a MySQL server.  |
|   1-create_database_if_missing.sql                 |  Create a database in a MySQL server.  |
|    2-remove_database.sql                |  Delete a database in a MySQL server.  |
|    3-list_tables.sql               |  List all the tables of a database in a MySQL server.  |
|    4-first_table.sql               |  Create a table in a MySQL  server.  |
|    5-full_table.sql                |   Print full description of the table from the database in a MySQL server.  |
|    6-list_values.sql               |  List sall rows of a table from a database in a MySQL server.  |
|    7-insert_value.sql                |  Insert a new row in the table in your MySQL server.  |
|    8-count_89.sql               |  Display the number of records with id = 89 in the table of a particular database in a MySQL server.  |
|    9-full_creation.sql                |  Create a table in the same database in a MySQL server and add multiple rows.  |
|    10-top_score.sql                  |  List all records of a table of the database in a MySQL server .  |
|    11-best_score.sql               |  List all records with a score above 10 in the second table of the same database in a MySQL server.  |
|   12-no_cheating.sql                 |  Update the score of a certain person to 10.  |
|   13-change_class.sql                 |  Remove all records with a score less than 5 in the second table of the database in a MySQL server.  |
|   14-average.sql                 |  Compute the average score of all records in the second table of the database.  |
|   15-groups.sql                 |  List the number of records with the same score in the second table of the database.  |
|   16-no_link.sql                 |  List all records of the second table of the database.  |
