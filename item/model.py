import web

#db = web.database(dbn='mysql', db='test', user='')
db = web.database(dbn='sqlite', db='../sqlite.db')

def get_items():
    return db.select('items', order='id')

def new_item(category, title, description, price, start, end):
    db.insert('items',Category=category, Title=title, Description=description, Price=price, open=start, end_date=end)

def del_todo(id):
    db.delete('items', where="id=$id", vars=locals())

def search_items(id):
    try:
        return db.select('items', where='id=$id', vars=locals())[0]
    except IndexError:
        return None
                         
def get_one_item(id):
    try:
        return db.select('items', where='id=$id', vars=locals())[0]
    except IndexError:
        return None