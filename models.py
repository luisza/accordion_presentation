from django.db import models
from cms.models import CMSPlugin, Page
from django.utils.translation import ugettext_lazy as _

from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class PresentationAccordion(CMSPlugin):
    custom_classes = models.CharField(_('custom classes'), max_length=200, blank=True)
    
    def __str__(self):
        return _("%s columns") % self.cmsplugin_set.all().count()

@python_2_unicode_compatible
class PresentationModel(CMSPlugin):
    
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500,  blank=True, null=True)
    
    icon = models.ImageField(upload_to='icons')
    photo = models.ImageField(upload_to='photos')
    
    color = models.CharField(max_length=8)
    
    page_link = models.ForeignKey(Page, verbose_name=_("page"), 
        help_text=_("If present image will be clickable"), blank=True,
        null=True, limit_choices_to={'publisher_is_draft': True})
    
    def __str__(self):
        return self.title
    
    search_fields = ('short_description',)
