TITLE = 'LiveWell Network'
ART = 'art-default.jpg'
ICON = 'icon-default.png'
NS = {'dig':'http://livewellnetwork.com/',
            'media':'http://search.yahoo.com/mrss/'}

HOME_FEED = 'http://livewellnetwork.com/xml?c=livewell'
SWT_RTRTS = 'http://livewellnetwork.com/xml?c=sweetretreats'
FD_RSH = 'http://livewellnetwork.com/xml?c=foodrush'
DEALS = 'http://livewellnetwork.com/xml?c=deals'
QUINN = 'http://livewellnetwork.com/xml?c=homewithlisaquinn'
TRAVELER = 'http://livewellnetwork.com/xml?c=traveler'
DISH = 'http://livewellnetwork.com/xml?c=letsdish'
LIVE_BIG = 'http://livewellnetwork.com/xml?c=livebigwithalivincent'
WOW = 'http://livewellnetwork.com/xml?c=weowewhat'
MEXICO = 'http://livewellnetwork.com/xml?c=mexicooneplate'
MIRROR = 'http://livewellnetwork.com/xml?c=mirrormirror'
MOTION = 'http://livewellnetwork.com/xml?c=motion'
FAMILY_RECIPE = 'http://livewellnetwork.com/xml?c=myfamilyreciperocks'
STEVEN_CHRIS = 'http://livewellnetwork.com/xml?c=stevenandchris'
BEST_RECIPES = 'http://livewellnetwork.com/xml?c=bestrecipesever'

###################################################################################################

# Set up containers for all possible objects
def Start():

  ObjectContainer.title1 = TITLE

###################################################################################################
@handler('/video/livewellnetwork', TITLE, art=ART, thumb=ICON)
def Mainmenu():
    oc = ObjectContainer()
    oc.add(DirectoryObject(key=Callback(Homefeed, title="LiveWell Homepage"), title="LiveWell Homepage"))
    oc.add(DirectoryObject(key=Callback(Swtrtrs, title="Sweet Retreats"), title="Sweet Retreats"))
    oc.add(DirectoryObject(key=Callback(Foodrush, title="Food Rush"), title="Food Rush"))
    oc.add(DirectoryObject(key=Callback(Deals, title="Deals"), title="Deals"))
    oc.add(DirectoryObject(key=Callback(Quinn, title="Home with Lisa Quinn"), title="Home with Lisa Quinn"))
    oc.add(DirectoryObject(key=Callback(Traveler, title="Laura McKenzie's Traveler"), title="Laura McKenzie's Traveler"))
    oc.add(DirectoryObject(key=Callback(Dish, title="Let's Dish"), title="Let's Dish"))
    oc.add(DirectoryObject(key=Callback(Livebig, title="Live Big with Ali Vincent"), title="Live Big with Ali Vincent"))
    oc.add(DirectoryObject(key=Callback(Wow, title="We Owe What"), title="We Owe What"))
    oc.add(DirectoryObject(key=Callback(Mexico, title="Mexico: One Plate At A Time"), title="Mexico: One Plate At A Time"))
    oc.add(DirectoryObject(key=Callback(Mirror, title="Mirror/Mirror"), title="Mirror/Mirror"))
    oc.add(DirectoryObject(key=Callback(Motion, title="Motion"), title="Motion"))
    oc.add(DirectoryObject(key=Callback(Familyrecipe, title="My Family Recipe Rocks"), title="My Family Recipe Rocks"))
    oc.add(DirectoryObject(key=Callback(Stevenchris, title="Steven and Chris"), title="Steven and Chris"))
    oc.add(DirectoryObject(key=Callback(Bestrecipes, title="Best Recipes Ever"), title="Best Recipes Ever"))
    return oc

###################################################################################################
@route('/video/livewellnetwork/homefeed')
def Homefeed(title):
    oc = ObjectContainer(title2=title)

    for video in XML.ElementFromURL(HOME_FEED).xpath('//item'):
        url = video.xpath('./link')[0].text
        title = video.xpath('./title')[0].text
        date = video.xpath('./pubDate')[0].text
        date = Datetime.ParseDate(date)
        summary = video.xpath('./description')[0].text
        #thumb = video.xpath('./dig:url', namespaces=NS)[0].get('url')

        oc.add(VideoClipObject(
              url = url,
              title = title,
              summary = summary,
              #thumb = Callback(Thumb, url=thumb)
              ))

    return oc


###################################################################################################
@route('/video/livewellnetwork/swtrtrs')
def Swtrtrs(title):
    oc = ObjectContainer(title2=title)

    for video in XML.ElementFromURL(SWT_RTRTS).xpath('//item'):
        url = video.xpath('./link')[0].text
        title = video.xpath('./title')[0].text
        date = video.xpath('./pubDate')[0].text
        date = Datetime.ParseDate(date)
        summary = video.xpath('./description')[0].text
        thumb = video.xpath('./dig:url')[0].get('url')

        oc.add(VideoClipObject(
              url = url,
              title = title,
              summary = summary,
              #thumb = Callback(Thumb, url=thumb)
              ))

    return oc

###################################################################################################
@route('/video/livewellnetwork/foodrush')
def Foodrush(title):
    oc = ObjectContainer(title2=title)

    for video in XML.ElementFromURL(FD_RSH).xpath('//item'):
        url = video.xpath('./link')[0].text
        title = video.xpath('./title')[0].text
        date = video.xpath('./pubDate')[0].text
        date = Datetime.ParseDate(date)
        summary = video.xpath('./description')[0].text
        thumb = video.xpath('./dig:url')[0].get('url')

        oc.add(VideoClipObject(
              url = url,
              title = title,
              summary = summary,
              #thumb = Callback(Thumb, url=thumb)
              ))

    return oc

###################################################################################################
@route('/video/livewellnetwork/deals')
def Deals(title):
    oc = ObjectContainer(title2=title)

    for video in XML.ElementFromURL(DEALS).xpath('//item'):
        url = video.xpath('./link')[0].text
        title = video.xpath('./title')[0].text
        date = video.xpath('./pubDate')[0].text
        date = Datetime.ParseDate(date)
        summary = video.xpath('./description')[0].text
        thumb = video.xpath('./dig:url')[0].get('url')

        oc.add(VideoClipObject(
              url = url,
              title = title,
              summary = summary,
              #thumb = Callback(Thumb, url=thumb)
              ))

    return oc
###################################################################################################
@route('/video/livewellnetwork/quinn')
def Quinn(title):
    oc = ObjectContainer(title2=title)

    for video in XML.ElementFromURL(QUINN).xpath('//item'):
        url = video.xpath('./link')[0].text
        title = video.xpath('./title')[0].text
        date = video.xpath('./pubDate')[0].text
        date = Datetime.ParseDate(date)
        summary = video.xpath('./description')[0].text
        thumb = video.xpath('./dig:url')[0].get('url')

        oc.add(VideoClipObject(
              url = url,
              title = title,
              summary = summary,
              #thumb = Callback(Thumb, url=thumb)
              ))

    return oc
###################################################################################################
@route('/video/livewellnetwork/traveler')
def Traveler(title):
    oc = ObjectContainer(title2=title)

    for video in XML.ElementFromURL(TRAVELER).xpath('//item'):
        url = video.xpath('./link')[0].text
        title = video.xpath('./title')[0].text
        date = video.xpath('./pubDate')[0].text
        date = Datetime.ParseDate(date)
        summary = video.xpath('./description')[0].text
        thumb = video.xpath('./dig:url')[0].get('url')

        oc.add(VideoClipObject(
              url = url,
              title = title,
              summary = summary,
              #thumb = Callback(Thumb, url=thumb)
              ))

    return oc
###################################################################################################
@route('/video/livewellnetwork/dish')
def Dish(title):
    oc = ObjectContainer(title2=title)

    for video in XML.ElementFromURL(DISH).xpath('//item'):
        url = video.xpath('./link')[0].text
        title = video.xpath('./title')[0].text
        date = video.xpath('./pubDate')[0].text
        date = Datetime.ParseDate(date)
        summary = video.xpath('./description')[0].text
        thumb = video.xpath('./dig:url')[0].get('url')

        oc.add(VideoClipObject(
              url = url,
              title = title,
              summary = summary,
              #thumb = Callback(Thumb, url=thumb)
              ))

    return oc
###################################################################################################
@route('/video/livewellnetwork/livebig')
def Livebig(title):
    oc = ObjectContainer(title2=title)

    for video in XML.ElementFromURL(LIVE_BIG).xpath('//item'):
        url = video.xpath('./link')[0].text
        title = video.xpath('./title')[0].text
        date = video.xpath('./pubDate')[0].text
        date = Datetime.ParseDate(date)
        summary = video.xpath('./description')[0].text
        thumb = video.xpath('./dig:url')[0].get('url')

        oc.add(VideoClipObject(
              url = url,
              title = title,
              summary = summary,
              #thumb = Callback(Thumb, url=thumb)
              ))

    return oc
###################################################################################################
@route('/video/livewellnetwork/wow')
def Wow(title):
    oc = ObjectContainer(title2=title)

    for video in XML.ElementFromURL(WOW).xpath('//item'):
        url = video.xpath('./link')[0].text
        title = video.xpath('./title')[0].text
        date = video.xpath('./pubDate')[0].text
        date = Datetime.ParseDate(date)
        summary = video.xpath('./description')[0].text
        thumb = video.xpath('./dig:url')[0].get('url')

        oc.add(VideoClipObject(
              url = url,
              title = title,
              summary = summary,
              #thumb = Callback(Thumb, url=thumb)
              ))

    return oc
###################################################################################################
@route('/video/livewellnetwork/mexico')
def Mexico(title):
    oc = ObjectContainer(title2=title)

    for video in XML.ElementFromURL(MEXICO).xpath('//item'):
        url = video.xpath('./link')[0].text
        title = video.xpath('./title')[0].text
        date = video.xpath('./pubDate')[0].text
        date = Datetime.ParseDate(date)
        summary = video.xpath('./description')[0].text
        thumb = video.xpath('./dig:url')[0].get('url')

        oc.add(VideoClipObject(
              url = url,
              title = title,
              summary = summary,
              #thumb = Callback(Thumb, url=thumb)
              ))

    return oc
###################################################################################################
@route('/video/livewellnetwork/mirror')
def Mirror(title):
    oc = ObjectContainer(title2=title)

    for video in XML.ElementFromURL(MIRROR).xpath('//item'):
        url = video.xpath('./link')[0].text
        title = video.xpath('./title')[0].text
        date = video.xpath('./pubDate')[0].text
        date = Datetime.ParseDate(date)
        summary = video.xpath('./description')[0].text
        thumb = video.xpath('./dig:url')[0].get('url')

        oc.add(VideoClipObject(
              url = url,
              title = title,
              summary = summary,
              #thumb = Callback(Thumb, url=thumb)
              ))

    return oc
###################################################################################################
@route('/video/livewellnetwork/motion')
def Motion(title):
    oc = ObjectContainer(title2=title)

    for video in XML.ElementFromURL(MOTION).xpath('//item'):
        url = video.xpath('./link')[0].text
        title = video.xpath('./title')[0].text
        date = video.xpath('./pubDate')[0].text
        date = Datetime.ParseDate(date)
        summary = video.xpath('./description')[0].text
        thumb = video.xpath('./dig:url')[0].get('url')

        oc.add(VideoClipObject(
              url = url,
              title = title,
              summary = summary,
              #thumb = Callback(Thumb, url=thumb)
              ))

    return oc
###################################################################################################
@route('/video/livewellnetwork/familyrecipe')
def Familyrecipe(title):
    oc = ObjectContainer(title2=title)

    for video in XML.ElementFromURL(FAMILY_RECIPE).xpath('//item'):
        url = video.xpath('./link')[0].text
        title = video.xpath('./title')[0].text
        date = video.xpath('./pubDate')[0].text
        date = Datetime.ParseDate(date)
        summary = video.xpath('./description')[0].text
        thumb = video.xpath('./dig:url')[0].get('url')

        oc.add(VideoClipObject(
              url = url,
              title = title,
              summary = summary,
              #thumb = Callback(Thumb, url=thumb)
              ))

    return oc
###################################################################################################
@route('/video/livewellnetwork/stevenchris')
def Stevenchris(title):
    oc = ObjectContainer(title2=title)

    for video in XML.ElementFromURL(STEVEN_CHRIS).xpath('//item'):
        url = video.xpath('./link')[0].text
        title = video.xpath('./title')[0].text
        date = video.xpath('./pubDate')[0].text
        date = Datetime.ParseDate(date)
        summary = video.xpath('./description')[0].text
        thumb = video.xpath('./dig:url')[0].get('url')

        oc.add(VideoClipObject(
              url = url,
              title = title,
              summary = summary,
              #thumb = Callback(Thumb, url=thumb)
              ))

    return oc
###################################################################################################
@route('/video/livewellnetwork/bestrecipes')
def Bestrecipes(title):
    oc = ObjectContainer(title2=title)

    for video in XML.ElementFromURL(BEST_RECIPES).xpath('//item'):
        url = video.xpath('./link')[0].text
        title = video.xpath('./title')[0].text
        date = video.xpath('./pubDate')[0].text
        date = Datetime.ParseDate(date)
        summary = video.xpath('./description')[0].text
        thumb = video.xpath('./dig:url')[0].get('url')

        oc.add(VideoClipObject(
              url = url,
              title = title,
              summary = summary,
              #thumb = Callback(Thumb, url=thumb)
              ))

    return oc
###################################################################################################
