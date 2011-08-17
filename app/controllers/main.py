from app.config.settings import *
import app.utility.utils as utils
import logging, web, re
from google.appengine.ext import ereporter
ereporter.register_logger()
from app.lib import pyso

render = web.render 


    
class Index:
    """
    Homepage
    """
    def GET(self):        
        return render.index()


class Users:
    """
    Post
    """
    def GET(self, endpoint, user_id):
        logging.debug(endpoint, user_id)
        web.header('Content-type', 'application/json')   
        
        pyso.install_site(pyso.APISite("api.%s" % endpoint, "1.0"))
        user = pyso.get_user(user_id)
        return '{"reputation": %s \
                 ,"gold_badge": %s \
                 ,"silver_badges": %s \
                 ,"bronze_badges": %s \
                 }' % (user['reputation'],
                       user['badge_counts'].get('gold',0),
                       user['badge_counts'].get('silver',0),
                       user['badge_counts'].get('bronze',0))

class Sitemap:
      """
      Sitemap
      """
      def GET(self):
          web.header('Content-type', 'text/xml')
          return render.sitemap()

class Robots:
       """
       Robots
       """
       def GET(self):
           return render.robots()          