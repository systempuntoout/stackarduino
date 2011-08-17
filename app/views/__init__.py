from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def index():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n'])
    extend_([u'<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US">\n'])
    extend_([u'<head>\n'])
    extend_([u'    <meta http-equiv="content-type" content="', escape_(settings.HTML_MIME_TYPE, True), u'"/>\n'])
    extend_([u'    <link rel="stylesheet" type="text/css" href="/stylesheets/screen.css"/>\n'])
    extend_([u'    <title> StackArduino</title> \n'])
    extend_([u'</head>\n'])
    extend_([u'<body>\n'])
    extend_([u"I'm alive\n"])
    extend_([u'\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

index = CompiledTemplate(index, 'app/views/index.html')
join_ = index._join; escape_ = index._escape

# coding: utf-8
def oops (message):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n'])
    extend_([u'<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US">\n'])
    extend_([u'<head>\n'])
    extend_([u'    <meta http-equiv="content-type" content="', escape_(settings.HTML_MIME_TYPE, True), u'"/>\n'])
    extend_([u'    <link rel="stylesheet" type="text/css" href="/stylesheets/screen.css"/>\n'])
    extend_([u'    <title> StackArduino - Error </title> \n'])
    extend_([u'</head>\n'])
    extend_([u'<body>\n'])
    extend_([u'    <div id="oops">                                                    \n'])
    extend_([u'              <p>', escape_(settings.RELAXING_MESSAGE_ERROR, True), u'</p>\n'])
    extend_([u'              <p><img src="/images/oops.png" alt="Error"/></p>\n'])
    extend_([u'              <p>', escape_((message), True), u' </p>\n'])
    extend_([u'    </div>\n'])
    extend_([u'\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

oops = CompiledTemplate(oops, 'app/views/oops.html')
join_ = oops._join; escape_ = oops._escape

# coding: utf-8
def robots():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'User-Agent: *\n'])
    extend_([u'Disallow: /api\n'])
    extend_([u'Sitemap: http://stackarduino.appspot.com/sitemap.xml\n'])

    return self

robots = CompiledTemplate(robots, 'app/views/robots.txt')
join_ = robots._join; escape_ = robots._escape

# coding: utf-8
def sitemap():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<?xml version="1.0" encoding="UTF-8"?>\n'])
    extend_([u'<urlset\n'])
    extend_([u'      xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'])
    extend_([u'      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n'])
    extend_([u'      xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9\n'])
    extend_([u'http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n'])
    extend_([u'    <url>\n'])
    extend_([u'      <loc>http://stackarduino.appspot.com</loc>\n'])
    extend_([u'    </url>\n'])
    extend_([u'</urlset>\n'])

    return self

sitemap = CompiledTemplate(sitemap, 'app/views/sitemap.xml')
join_ = sitemap._join; escape_ = sitemap._escape

