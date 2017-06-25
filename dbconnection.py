import psycopg2
import credentials


def establish_connection():
    try:
        connect_str = "dbname={} user={} host={} password={}".format(credentials.login['dbname'],
                                                                     credentials.login['user'],
                                                                     credentials.login['host'],
                                                                     credentials.login['password'])
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True

    except Exception as e:
        print("Cannot connect to database.")
        print(e)

    else:
        return conn


def get_data_from_table(sql_string, sql_variables=None):
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(sql_string, sql_variables)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def edit_table(sql_string, sql_variables=None):
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(sql_string, sql_variables)
    cursor.close()
    conn.close()