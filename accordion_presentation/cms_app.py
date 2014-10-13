# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class PresentationApp(CMSApp):
    name = _("Presentation App")        # give your app a name, this is required
    urls = ["accordion_presentation.urls"]       # link your app to url configuration(s)
    app_name = "accordion_presentation"          # this is the application namespace

apphook_pool.register(PresentationApp) # register your app
