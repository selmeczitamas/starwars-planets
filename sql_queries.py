import dbconnection


def add_new_user(data):
    """
    answer is a tuple which contain the username and the password
    """
    sql_string = "INSERT INTO usertable (username, password) \
                  VALUES (%s, %s);"
    sql_variable = tuple(data)
    dbconnection.edit_table(sql_string, sql_variable)


def check_user_login(data):
    sql_string = "SELECT username FROM usertable \
                  WHERE username=%s AND password=%s;"
    sql_variable = data
    return dbconnection.get_data_from_table(sql_string, sql_variable)