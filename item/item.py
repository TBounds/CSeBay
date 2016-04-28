""" Basic item list using webpy 0.3 """
import web
import model
import datetime

### Url mappings

urls = (
        '/', 'Index',
        '/new', 'New',
        '/newbid/(\d+)', 'New_Bid',
        '/item/(\d+)', 'Item',
        '/searchid', 'Search_ID',
        '/searchdesc', 'Search_Desc',
        '/searchcat', 'Search_Cat',
        '/searchbid', 'Search_Bid',
        '/searchED', 'Search_ED',
        '/searchopen', 'Search_OPEN',
        )


### Templates
render = web.template.render('templates', base='base')


class Index:

    form = web.form.Form()

    def GET(self):
        """ Show page """
        items = model.get_items()
        print(items)
        form = self.form()
        return render.index(items, form)


class New:
    
    form = web.form.Form()
        
    def GET(self):
        form = self.form()
        return render.new(form)

    def POST(self):
        """ Add new entry """
        form = web.input()
        form.buyPrice = float(form.buyPrice)
        form.startDate = bool(form.startDate)
        # form.endDate = datetime('now')

        result = model.new_item(form.Category, form.Title, form.Description, float(form.buyPrice), form.startDate, form.endDate)
        print("result")
        print(result)
        model.place_bid(result, float(0), "No current bids")
        raise web.seeother('/')

class New_Bid:
    
    form = web.form.Form()

    def POST(self, id):
        """ Add new bid """
        print("In New_Bid")
        form = web.input()

        try:
           form.bid = float(form.bid)
        except:
           raise web.seeother("/")
        print(form)
        print(form.user)
        print(form.bid)
        print(id)

        print("Here")
        model.place_bid(id, form.bid, form.user)
        item = model.get_one_item(id)
        bid = model.get_bid(id)

        return render.item(item, bid)


class Item:
    
    def GET(self, id):
        """ View single post """
        item = model.get_one_item(int(id))
        bid = model.get_bid(int(id)) 
        print(item)
        print(bid)
        return render.item(item, bid)


class Search_ID:
    print("In Search")
    form = web.form.Form()

    def GET(self):
        """ Show page """
        print("In GET")
        try:
            sform = web.input()
            sform.id = int(sform.id)
        except:
            raise web.seeother('/')

        print(sform.id) # Print value
        items = model.search_id(sform.id)

        print(items)

        form = self.form()
        return render.index(items, form)

class Search_Desc:
    print("In Search")
    form = web.form.Form()

    def GET(self):
        """ Show page """
        print("In GET")

        sform = web.input()
        if sform.id == '':
            raise web.seeother('/')

        print(sform.id) # Print value
        items = model.search_desc(sform.id)

        print(items)

        form = self.form()
        return render.index(items, form)

class Search_Cat:
    print("In Search")
    form = web.form.Form()

    def GET(self):
        """ Show page """
        print("In GET")

        sform = web.input()
        if sform.id == '':
            raise web.seeother('/')

        print(sform.id) # Print value
        items = model.search_cat(sform.id)

        print(items)

        form = self.form()
        return render.index(items, form)

class Search_Bid:
    print("In Search")
    form = web.form.Form()

    def GET(self):
        """ Show page """
        print("In GET")
        try:
            sform = web.input()
            sform.id = float(sform.id)
        except:
            raise web.seeother('/')

        print(sform.id) # Print value
        items = model.search_bid(sform.id)

        print(items)

        form = self.form()
        return render.index(items, form)

class Search_ED:
    print("In Search")
    form = web.form.Form()

    def GET(self):
        """ Show page """
        print("In GET")

        sform = web.input()
        if sform.id == '':
            raise web.seeother('/')

        print(sform.id) # Print value
        items = model.search_ed(sform.id)

        print(items)

        form = self.form()
        return render.index(items, form)

class Search_OPEN:
    print("In Search")
    form = web.form.Form()

    def GET(self):
        """ Show page """
        print("In GET")

        sform = web.input()
        if bool(sform.id) == 0:
            raise web.seeother('/')

        print(sform.id) # Print value
        items = model.search_open(sform.id)

        print(items)

        form = self.form()
        return render.index(items, form)

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()