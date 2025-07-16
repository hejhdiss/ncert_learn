import mysql.connector
mydb=''

error='mysql.connector.errors.DatabaseError,mysql.connector.errors.DataError,mysql.connector.errors.Error,mysql.connector.errors.IntegrityError,mysql.connector.errors.InterfaceError\
mysql.connector.errors.InternalError,mysql.connector.errors.Mapping,mysql.connector.errors.NotSupportedError,mysql.connector.errors.OperationalError,mysql.connector.errors.OperationalError\
mysql.connector.errors.ProgrammingError,mysql.connector.errors.Warning'
def mysqlconnectwithdatabase(database,host='localhost',user='root',password='',port='3306',):


    """
    Connects to a MySQL database with the specified database name.

    Parameters
    ----------
    database : str
        The name of the database to connect to.
    host : str, optional
        The hostname or IP address of the MySQL server. Defaults to 'localhost'.
    user : str, optional
        The MySQL username. Defaults to 'root'.
    password : str, optional
        The MySQL password. Defaults to an empty string ''.
    port : str, optional
        The port number of the MySQL server. Defaults to '3306'.

    Returns
    -------
    bool
        True if the connection was successful, False otherwise.
    """


    try:
        global mydb
        if mydb!='':
            mydb.close()
        mydb=mysql.connector.connect(host=host,user=user,passwd=password,port=port,database=database)
    except mysql.connector.errors.DatabaseError:
        return False
    except mysql.connector.errors.DataError:
            return False
    except mysql.connector.errors.Error:
            return False
    except mysql.connector.errors.IntegrityError:
            return False
    except mysql.connector.errors.InterfaceError:
            return False
    except mysql.connector.errors.InternalError:
            return False
    except mysql.connector.errors.Mapping:
            return False
    except mysql.connector.errors.NotSupportedError:
            return False
    except mysql.connector.errors.OperationalError:
            return False
    except mysql.connector.errors.ProgrammingError:
            return False
    except mysql.connector.errors.Warning:
            return False
    except mysql.connector.errors.PoolError:
            return False
    except Exception:
        return False
    else:
        return True

def mysqlconnect(host='localhost',user='root',password='',port='3306'):



    """
    Connects to a MySQL server without specifying a database.

    Parameters
    ----------
    host : str, optional
        The hostname or IP address of the MySQL server. Defaults to 'localhost'.
    user : str, optional
        The MySQL username. Defaults to 'root'.
    password : str, optional
        The MySQL password. Defaults to an empty string ''.
    port : str, optional
        The port number of the MySQL server. Defaults to '3306'.

    Returns
    -------
    bool
        True if the connection was successful, False otherwise.
    """

    try:
        global mydb
        if mydb!='':
            mydb.close()
        mydb=mysql.connector.connect(host=host,user=user,passwd=password,port=port)
    except mysql.connector.errors.DatabaseError:
        return False
    except mysql.connector.errors.DataError:
            return False
    except mysql.connector.errors.Error:
            return False
    except mysql.connector.errors.IntegrityError:
            return False
    except mysql.connector.errors.InterfaceError:
            return False
    except mysql.connector.errors.InternalError:
            return False
    except mysql.connector.errors.Mapping:
            return False
    except mysql.connector.errors.NotSupportedError:
            return False
    except mysql.connector.errors.OperationalError:
            return False
    except mysql.connector.errors.ProgrammingError:
            return False
    except mysql.connector.errors.Warning:
            return False
    except mysql.connector.errors.PoolError:
            return False
    except Exception:
        return False
    else:
        return True

def mysqlshowdatabases():

    """
    Shows all databases in the MySQL server.

    Returns
    -------
    tuple
        A tuple of strings, where each string is a database name
    """
    

    if mydb=='':
        return False
    else:
        mycursor=mydb.cursor()
        mycursor.execute('show databases;')
        z=()
        for x in mycursor:
            z+=x
        return z
def mysqlcreatedatabase(a):

    """
    Creates a new database in the MySQL server with the specified name.

    Parameters
    ----------
    a : str
        The name of the database to be created.

    Returns
    -------
    bool
        True if the database was created successfully, False if the connection to the database is not established.
    """

    if mydb=='':
        return False
    else:
        mycursor=mydb.cursor()
        mycursor.execute(f'create database {a};')
        return True
def mysqlshowtables():

    """
    Returns a tuple of strings containing the names of all tables in the current database.

    Returns
    -------
    tuple
        A tuple of strings, where each string is a table name
    """
    if mydb=='':
        return False
    else:
        mycursor=mydb.cursor()
        mycursor.execute('show tables;')
        z=()
        for x in mycursor:
            z+=x
        return z
def mysqlshowtablesfromdatabase(a):

    """
    Returns a tuple of strings containing the names of all tables in the specified database.

    Parameters
    ----------
    a : str
        The name of the database

    Returns
    -------
    tuple
        A tuple of strings, where each string is a table name
    """

    if mydb=='':
        return False
    elif not('str' in str(type(a))):
        return False
    elif a=='':
        return False
    else:
        mycursor=mydb.cursor()
        mycursor.execute('show databases;')
        m=()
        for x in mycursor:
            m+=x
        if a in m:
            mycursor=mydb.cursor()
            mycursor.execute(f'use {a};')
            mycursor.execute('show tables;')
            z=()
            for x in mycursor:
                z+=x
            return z
        else:
            return False

def mysqldescribetable(a):

    """
    Describes the structure of a specified table in the current database.

    Parameters
    ----------
    a : str
        The name of the table to describe.

    Returns
    -------
    tuple
        A tuple containing the description of the table's columns,
        including field name, type, nullability, key information, default values, 
        and extra information. Returns False if the connection to the database
        is not established or if the table does not exist.
    """

    if mydb=='':
        return False
    elif not('str' in str(type(a))):
        return False
    elif a=='':
        return False
    else:
        mycursor=mydb.cursor()
        mycursor.execute('show tables;')
        z=()
        for x in mycursor:
            z+=x
        if a in z:
            mycursor.execute(f'desc {a};')
            k=()
            for x in mycursor:
                k+=(x,)
            return k
        else:
            return False
def mysqldescribetablefromdatabase(b,a):

    """
    Describes the structure of a specified table in a specified database.

    Parameters
    ----------
    b : str
        The name of the database
    a : str
        The name of the table to describe.

    Returns
    -------
    tuple
        A tuple containing the description of the table's columns,
        including field name, type, nullability, key information, default values, 
        and extra information. Returns False if the connection to the database
        is not established or if the table does not exist.
    """
    

    if mydb=='':
        return False
    elif not('str' in str(type(a))):
        return False
    elif a=='':
        return False
    elif not('str' in str(type(b))):
        return False
    elif b=='':
        return False
    else:
        mycursor=mydb.cursor()
        mycursor.execute('show databases;')
        m=()
        for x in mycursor:
            m+=x
        if b in m:
            mycursor.execute(f'use {b};')
            mycursor.execute('show tables;')
            z=()
            for x in mycursor:
                z+=x
            if a in z:
                mycursor.execute(f'desc {a};')
                k=()
                for x in mycursor:
                    k+=(x,)
                return k
            else:
                return False
        else:
            return False
def mysqlfetchalltable(a):

    """
    Fetches all rows from a specified table in the current database.

    Parameters
    ----------
    a : str
        The name of the table.

    Returns
    -------
    tuple
        A tuple of tuples, where each inner tuple is a row in the table.
        Returns False if the connection to the database is not established or 
        if the table does not exist.
    """

    if mydb=='':
        return False
    elif not('str' in str(type(a))):
        return False
    elif a=='':
        return False
    else:
        mycursor=mydb.cursor()
        mycursor.execute('show tables;')
        z=()
        for x in mycursor:
            z+=x
        if a in z:
            mycursor.execute(f'select * from {a};')
            k=mycursor.fetchall()
            return k
        else:
            return False

def mysqlfetchalltablefromdatabase(b,a):

    """
    Fetches all rows from a specified table in a specified database.

    Parameters
    ----------
    b : str
        The name of the database.
    a : str
        The name of the table.

    Returns
    -------
    tuple
        A tuple of tuples, where each inner tuple is a row in the table.
    """

    if mydb=='':
        return False
    elif not('str' in str(type(a))):
        return False
    elif a=='':
        return False
    elif not('str' in str(type(b))):
        return False
    elif b=='':
        return False
    else:
        mycursor=mydb.cursor()
        mycursor.execute('show databases;')
        m=()
        for x in mycursor:
            m+=x
        if b in m:
            mycursor.execute(f'use {b};')
            mycursor.execute('show tables;')
            z=()
            for x in mycursor:
                z+=x
            if a in z:
                mycursor.execute(f'select * from {a};')
                k=mycursor.fetchall()
                return k
            else:
                return False
        else:
            return False
def mysqlcreatetable(database,name,d,s):

    """
    Creates a new table in the specified database with the specified name
    and structure.

    Parameters
    ----------
    database : str
        The name of the database to create the table in.
    name : str
        The name of the table to create.
    d : tuple
        A tuple of strings, where each string is a field name.
    s : tuple
        A tuple of strings, where each string is a data type.
        The length of this tuple should be equal to the length of d.

    Returns
    -------
    bool
        True if the table was created successfully, False if the connection to the database is not established or if the table already exists.
    """

    if mydb=='':
        return False
    elif not('tuple' in str(type(d)) and 'tuple' in str(type(s))):
        return False
    elif s==() and d==():
        return False
    elif not('str' in str(type(name))):
        return False
    elif name=='':
        return False
    elif not('str' in str(type(database))):
        return False
    elif database=='':
        return False
    else:
        try:
            mycursor=mydb.cursor()
            mycursor.execute('show databases;')
            m=()
            for x in mycursor:
                m+=x
            if database in m:
                j=1
                for i in d:
                    s.insert(j,i)
                    j+=2
                k='('
                for i in range(len(s)):
                    if i==0 or i%2==0:
                        k+=s[i]
                        k+=' '
                    elif i!=(len(s)-1):
                        k+=s[i]
                        k+=','
                    else:
                        k+=s[i]
                        k+=')'
                mycursor.execute(f'use {database};')
                mycursor.execute(f'create table {name}{k};')
        except Exception:
            return False
        except ValueError:
            return False
        except TypeError:
            return False
        except mysql.connector.errors.DatabaseError:
            return False
        except mysql.connector.errors.DataError:
                return False
        except mysql.connector.errors.Error:
                return False
        except mysql.connector.errors.IntegrityError:
                return False
        except mysql.connector.errors.InterfaceError:
                return False
        except mysql.connector.errors.InternalError:
                return False
        except mysql.connector.errors.Mapping:
                return False
        except mysql.connector.errors.NotSupportedError:
                return False
        except mysql.connector.errors.OperationalError:
                return False
        except mysql.connector.errors.ProgrammingError:
                return False
        except mysql.connector.errors.Warning:
                return False
        except mysql.connector.errors.PoolError:
                return False
        else:
            return  True
def mysqltableinsert(database,name,s):

    """
    This function is used to insert data into a table in a MySQL database.

    Parameters:
    database (str): The name of the database to insert into.
    name (str): The name of the table to insert into.
    s (tuple): The data to insert into the table. The tuple should contain the data in the order of the columns in the table.

    Returns:
    bool: True if the data was inserted successfully, False otherwise.

    """
    

    if mydb=='':
        return False
    elif not('tuple' in str(type(s))):
            return False
    elif s==():
        return False
    elif not('str' in str(type(name))):
        return False
    elif name=='':
        return False
    elif not('str' in str(type(database))):
        return False
    elif database=='':
        return False
    else:
        try:
            mycursor=mydb.cursor()
            mycursor.execute('show databases;')
            m=()
            for x in mycursor:
                m+=x
            if database in m:
                mycursor.execute(f'use {database};')
                mycursor.execute('show tables;')
                z=()
                for x in mycursor:
                    z+=x
                if name in z:
                    mycursor.execute(f'insert into {name} values{s};')
                    mydb.commit()
                else:
                    return False
            else:
                return False
        except ValueError:
            return False
        except Exception:
            return False
        except TypeError:
            return False
        except mysql.connector.errors.DatabaseError:
            return False
        except mysql.connector.errors.DataError:
                return False
        except mysql.connector.errors.Error:
                return False
        except mysql.connector.errors.IntegrityError:
                return False
        except mysql.connector.errors.InterfaceError:
                return False
        except mysql.connector.errors.InternalError:
                return False
        except mysql.connector.errors.Mapping:
                return False
        except mysql.connector.errors.NotSupportedError:
                return False
        except mysql.connector.errors.OperationalError:
                return False
        except mysql.connector.errors.ProgrammingError:
                return False
        except mysql.connector.errors.Warning:
                return False
        except mysql.connector.errors.PoolError:
                return False
        else:
            return True
def mysqlrowcounttablefromdatabase(b,a):

    """
    Returns the number of rows in a specified table from a specified database.

    Parameters
    ----------
    b : str
        The name of the database.
    a : str
        The name of the table.

    Returns
    -------
    int
        The number of rows in the table if the database and table exist.
    bool
        False if the database or table does not exist, or if the connection is not established.
    """

    if mydb=='':
        return False
    else:
        mycursor=mydb.cursor()
        mycursor.execute('show databases;')
        m=()
        for x in mycursor:
            m+=x
        if b in m:
            mycursor.execute(f'use {b};')
            mycursor.execute('show tables;')
            z=()
            for x in mycursor:
                z+=x
            if a in z:
                mycursor.execute(f'select * from {a};')
                return mycursor.rowcount
            else:
                return False
        else:
            return False
def mysqlexecutequery(s):

    """
    Executes a specified SQL query.

    Parameters
    ----------
    s : str
        The SQL query to execute.

    Returns
    -------
    bool
        True if the query was executed successfully.
        False if the connection is not established, or if an error occurs.
    """

    if mydb=='':
        return False
    elif s=='':
        return False
    elif not('str' in str(type(s))):
        return False
    else:
        try:
            mycursor=mydb.cursor()
            mycursor.execute(s)
        except Exception:
            return False
        except ValueError:
            return False
        except TypeError:
            return False
        except mysql.connector.errors.DatabaseError:
            return False
        except mysql.connector.errors.DataError:
            return False
        except mysql.connector.errors.Error:
            return False
        except mysql.connector.errors.IntegrityError:
            return False
        except mysql.connector.errors.InterfaceError:
            return False
        except mysql.connector.errors.InternalError:
            return False
        except mysql.connector.errors.Mapping:
            return False
        except mysql.connector.errors.NotSupportedError:
            return False
        except mysql.connector.errors.OperationalError:
            return False
        except mysql.connector.errors.ProgrammingError:
            return False
        except mysql.connector.errors.Warning:
            return False
        except mysql.connector.errors.PoolError:
            return False
        else:
            return True
import mysql.connector

mydb = None

def mysql_execute_advanced_mode(operation, database=None, table=None, query=None, data=None, host='localhost', user='root', password='', port='3306'):
    """
    Generalized function to perform various MySQL operations like connect, create DB, show DBs, fetch rows, etc.

    Parameters
    ----------
    operation : str
        The operation to perform. Can be 'connect', 'show_databases', 'create_database', 'show_tables', 
        'fetch_all', 'create_table', 'insert', 'count_rows', 'execute_query'.
    database : str, optional
        The database name, required for operations like 'create_table', 'insert', etc.
    table : str, optional
        The table name for operations like 'show_tables', 'fetch_all', 'insert', etc.
    query : str, optional
        The SQL query for 'execute_query' operations.
    data : tuple, optional
        The data to insert into a table (for 'insert' operations).
    host : str, optional
        The hostname or IP address of the MySQL server. Defaults to 'localhost'.
    user : str, optional
        The MySQL username. Defaults to 'root'.
    password : str, optional
        The MySQL password. Defaults to an empty string ''.
    port : str, optional
        The port number of the MySQL server. Defaults to '3306'.

    Returns
    -------
    tuple or bool
        Returns the result of the operation or True/False depending on success or failure.
    """
    global mydb

    try:
        # Connect to MySQL server
        if operation == 'connect':
            if mydb and mydb.is_connected():
                mydb.close()
            mydb = mysql.connector.connect(host=host, user=user, passwd=password, port=port, database=database)
            return mydb.is_connected()

        # Show all databases
        elif operation == 'show_databases':
            if not mydb or not mydb.is_connected():
                return False
            cursor = mydb.cursor()
            cursor.execute('SHOW DATABASES')
            return tuple(database[0] for database in cursor.fetchall())

        # Create a new database
        elif operation == 'create_database':
            if not mydb or not mydb.is_connected():
                return False
            cursor = mydb.cursor()
            cursor.execute(f'CREATE DATABASE {database}')
            return True

        # Show all tables in the current database
        elif operation == 'show_tables':
            if not mydb or not mydb.is_connected() or not database:
                return False
            cursor = mydb.cursor()
            cursor.execute(f'USE {database}')
            cursor.execute('SHOW TABLES')
            return tuple(table[0] for table in cursor.fetchall())

        # Fetch all rows from a table
        elif operation == 'fetch_all':
            if not mydb or not mydb.is_connected() or not database or not table:
                return False
            cursor = mydb.cursor()
            cursor.execute(f'USE {database}')
            cursor.execute(f'SELECT * FROM {table}')
            return tuple(cursor.fetchall())

        # Create a table in the specified database
        elif operation == 'create_table':
            if not mydb or not mydb.is_connected() or not database or not table or not data:
                return False
            cursor = mydb.cursor()
            cursor.execute(f'USE {database}')
            columns = ', '.join([f'{field} {dtype}' for field, dtype in zip(data[0], data[1])])
            cursor.execute(f'CREATE TABLE {table} ({columns})')
            return True

        # Insert data into a table
        elif operation == 'insert':
            if not mydb or not mydb.is_connected() or not database or not table or not data:
                return False
            cursor = mydb.cursor()
            cursor.execute(f'USE {database}')
            placeholders = ', '.join(['%s'] * len(data))
            cursor.execute(f'INSERT INTO {table} VALUES ({placeholders})', data)
            mydb.commit()
            return True

        # Count the number of rows in a table
        elif operation == 'count_rows':
            if not mydb or not mydb.is_connected() or not database or not table:
                return False
            cursor = mydb.cursor()
            cursor.execute(f'USE {database}')
            cursor.execute(f'SELECT COUNT(*) FROM {table}')
            return cursor.fetchone()[0]

        # Execute a custom SQL query
        elif operation == 'execute_query':
            if not mydb or not mydb.is_connected() or not query:
                return False
            cursor = mydb.cursor()
            cursor.execute(query)
            return cursor.fetchall()

    except mysql.connector.Error as err:
 
        return False
    except Exception as ex:

        return False







