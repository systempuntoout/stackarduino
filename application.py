"""
    StackArduino: StackExchange API for Arduino hosted on Google App Engine
"""
from app.config.urls import urls
import app.config.settings as settings 
from google.appengine.ext.webapp.util import run_wsgi_app

import app.utility.utils as utils
import logging
import web
import os

global_template = {
            'safemarkdown':web.safemarkdown,
            'commify': web.utils.commify,
            'urlquote':web.net.urlquote,
            'htmlquote':web.net.htmlquote,
            'settings': settings,
            'utils': utils,
            'development' : os.environ['SERVER_SOFTWARE'].startswith('Dev')
          }

web.render = render = web.template.render('app/views/', globals = global_template, cache = True)
                                               
def notfound():
    return web.notfound(render.oops(settings.NOT_FOUND_ERROR))
def internalerror():
    return web.internalerror(render.oops(settings.SERVER_ERROR))

app = web.application(urls, globals())
app.notfound = notfound
app.internalerror = internalerror

def main():
    logging.getLogger().setLevel(logging.DEBUG)
    application = app.wsgifunc()
    run_wsgi_app(application)

if __name__ == '__main__':
    main()


