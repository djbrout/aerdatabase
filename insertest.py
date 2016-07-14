import connection as c
db,de = c.con()


def go(name = 'John Doe', age=46, country='China',gender=None):

    table = db['user']

    # Insert a new record.
    table.insert(dict(name=name, age=age, country=country,gender=gender))

    print('Inserted into database succesfully...')

    #df.to_sql("my_table_name", engine)