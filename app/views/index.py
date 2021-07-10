from . import view_pages, render_template, request

@view_pages.route('/')
def index():
    return render_template('index.html', title='Sports events',)
