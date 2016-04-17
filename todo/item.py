""" Basic item list using webpy 0.3 """
import web
import model

### Url mappings

urls = (
        '/', 'Index',
        '/new', 'New',
        '/delete/(\d+)', 'Delete',
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
    
  
    def POST(self):
        """ Add new entry """
        form = self.form()
        if not form.validates():
            items = model.get_items()
            return render.index(items, form)
        model.new_item(form.d.title)
        raise web.seeother('/')

    def DELETE(self, id):
        """ Delete based on ID """
        id = int(id)
        model.del_item(id)
        raise web.seeother('/')


class Delete:

    def POST(self, id):
        """ Delete based on ID """
        id = int(id)
        model.del_item(id)
        raise web.seeother('/')

class New:
    
    form = web.form.Form()
        
    def GET(self):
        form = self.form()
        return render.new(form)
                             

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
