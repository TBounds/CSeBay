import web

#db = web.database(dbn='mysql', db='test', user='')
db = web.database(dbn='sqlite', db='../sqlite.db')

def get_items():
    return db.select('items', order='id')

def new_todo(text):
    db.insert('item', title=text)

def del_todo(id):
    db.delete('item', where="id=$id", vars=locals())
