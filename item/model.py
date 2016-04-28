import web

#db = web.database(dbn='mysql', db='test', user='')
db = web.database(dbn='sqlite', db='../sqlite.db')

def get_items():
    return db.select('items', order='id')

def new_item(category, title, description, price, start, end):
    db.insert('items',Category=category, Title=title, Description=description, Price=price, open=start, end_date=end)

def del_todo(id):
    db.delete('items', where="id=$id", vars=locals())

def search_id(id):
    print("In search_id")
    try:
       return db.select('items', where="id=$id", vars=locals())
    except IndexError:
        return None 

def search_desc(id):
    print("In search_desc")
    print(id)
    try:
       return db.select('items', where="title=$id", vars=locals())
    except IndexError:
        return None

def search_cat(id):
    print("In search_cat")
    print(id)
    try:
       return db.select('items', where="category=$id", vars=locals())
    except IndexError:
        return None
  
def get_one_item(id):
    print("In get_one_item")
    try:
        return db.select('items', where='id=$id', vars=locals())[0]
    except IndexError:
        return None