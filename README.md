# Easy Database Access through SqlAlchemy

Purpose of this simplify access process to different types of databases through SQLAlchemy

## Installation

Copy the repo and run a 

```
pip install db-access
```

in the root directory of the repo.

You may also need to install other applications on your computer for these connections to work (i.e. drivers). You can find the links to each of the driver installations below.

## Databases Support

So far the package supports the following databases:

* [Oracle](https://cx-oracle.readthedocs.io/en/latest/installation.html#install-oracle-instant-client)
* [MS SQL](https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Mac-OSX)
* MySQL
* Impala

Feel free to let me know if there is a need for additional database coverage

## Use

Import the corresponding class for the database type you are connecting to and add the required login info. From the object, you can create a SQLAlchemy engine and get that engine. You can also get specific sqlalchemy.Table objects from that connection.

