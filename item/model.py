import web

#db = web.database(dbn='mysql', db='test', user='')
db = web.database(dbn='sqlite', db='../sqlite.db')

def get_items():
    return db.select('items', order='id')

def new_item(category, title, description, price, start, end):
    result = db.insert('items',Category=category, Title=title, Description=description, Price=price, open=start, end_date=end)
    return result

def place_bid(id, bid, username):
    print("In place_bid")
    # db.update('items',where="id=$id", price = bid, vars=locals())
    # Grabs the highest bid so that a lower bid can't override a higher bid
    result =  db.query("SELECT max(price) AS price,buyer,id FROM bids WHERE id=$id", vars=locals())[0]
    
    db.insert('bids', price = bid, id = id, buyer = username)
    db.update('items', where="id=$id", highBid = result.price, vars=locals())

def get_bid(id):    
    print("In get_bid")
    result =  db.query("SELECT max(price) AS price,buyer,id FROM bids WHERE id=$id", vars=locals())[0]
    print("result")
    print(result)
    return result

def del_todo(id):
    db.delete('items', where="id=$id", vars=locals())

def search_id(id):
    print("In search_id")
    try:
       return db.select('items', where="id=$id", vars=locals())
    except IndexError:
        return None 

def search_desc(id):
    try:
        return db.query("SELECT * FROM items WHERE title LIKE" + web.sqlquote('%'+id+'%'))
    except IndexError:
        return Non

def search_cat(id):
    try:
        return db.query("SELECT * FROM items WHERE category LIKE" + web.sqlquote('%'+id+'%'))
    except IndexError:
        return None

def search_bid(id):
    print("In search_bid")
    try:
       return db.select('items', where="price<=$id", vars=locals())
    except IndexError:
        return None 

def search_ed(id):
    print("In search_ed")
    print(id)
    try:
       return db.select('items', where="end_date=$id", vars=locals())
    except IndexError:
        return None

def search_open(id):
    print("In search_ed")
    print(id)
    try:
       return db.select('items', where="open=$id", vars=locals())
    except IndexError:
        return None

def get_one_item(id):
    print("In get_one_item")
    try:
        return db.select('items', where='id=$id', vars=locals())[0]
    except IndexError:
        return None