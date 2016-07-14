import connection as c
db,de = c.con()
from IPython.core.display import HTML

def go(name = 'John Doe', age=46, country='China',gender=None):

    table = db['user']

    # Insert a new record.
    table.insert(dict(name=name, age=age, country=country,gender=gender))

    return HTML('<h4>Inserted into database succesfully...</h4>')

    #df.to_sql("my_table_name", engine)