""" Basic item list using webpy 0.3 """
import web
import model
import datetime

### Url mappings

urls = (
        '/', 'Index',
        '/new', 'New',
        '/item/(\d+)', 'Item',
        '/search', 'Search',
        )


### Templates
render = web.template.render('templates', base='base')


class Index:

    form = web.form.Form()

    def GET(self):
        """ Show page """
        items = model.get_items()
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
        form.endDate = datetime('now')
        model.new_item(form.Category, form.Title, form.Description, float(form.buyPrice), form.startDate, form.endDate)
        raise web.seeother('/')

class Item:
    
    def GET(self, id):
        """ View single post """
        item = model.get_one_item(int(id))
        return render.item(item)


class Search:
    
    form = web.form.Form()

    def GET(self):
        """ Show page """
        sform = web.input()
        sform.id = int(sform.id)
        return sform
        items = model.search_items(sform.id)
        form = self.form()
        return render.index(items, form)


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
