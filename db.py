import mysql.connector

'''
State your group member name and id here:
ex: 1. 2023001chea - Joe Chea

'''


# TODO:
# host can be 'localhost' or '127.0.0.1'
# if you are using mamp, password is root
# and port is 8889
# use cat_db as database.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cat_db",
    port="3306"
)


cursor = mydb.cursor()



def register_cat(cat_info):
    '''
    TODO:
    cat_info is in a form of list ex: ["rose", "f", "Siberian", "2020-03-08", "smart one"], that register_cat function will insert the provided
    list to cats table as an insert record.
    '''
    sql = "INSERT INTO cats (name, gender, breed, dob, description) VALUES (%s, %s, %s, %s, %s)"
    val = (cat_info)
    cursor.execute(sql, val)
    mydb.commit()
    pass


def get_cats():
    '''
    TODO:
    this function will get all cat from cats table 
    '''
    cursor.execute("SELECT * FROM cats")
    result = cursor.fetchall()
    return result
    pass


def get_cat(id):
    '''
    TODO:
    this function will get a single cat data from cat table base on the id parameter
    '''
    cursor.execute(f"SELECT * FROM cats WHERE id={id}")
    result = cursor.fetchone()
    return result
    



def update_cat(cat_info):
    '''
    TODO:
    cat_info is in a form of list ex: [1,"rose", "f", "Siberian", "2020-03-08", "smart one"], that update_cat function will use as 
    an update record for specific cat information where equal to cat_info[0]
    '''

    sql=(f"UPDATE cats SET name=%s, gender=%s, breed=%s, dob=%s, description=%s WHERE id={cat_info[0]}")
    val= (cat_info[1],cat_info[2],cat_info[3],cat_info[4],cat_info[5])
    cursor.execute(sql,val)
    mydb.commit()
    pass


def remove_cat(id):
    '''
    TODO:
    this function will remove record from cat table base on id parameter.
    '''
    sql=(f"DELETE FROM cats WHERE id={id}")
    cursor.execute(sql)
    mydb.commit()
    pass
