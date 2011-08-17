"""
 Routes to controllers
"""

urls = (
  '/api/([\w\.]+)/users/(\d+)', 'app.controllers.main.Users',
  '/sitemap.xml', 'app.controllers.main.Sitemap',
  '/robots.txt', 'app.controllers.main.Robots',
  '/_ah/warmup','app.controllers.admin.Warmup',
  '/', 'app.controllers.main.Index',
)

