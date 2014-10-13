from django.db import models
from cms.models import CMSPlugin, Page
from django.utils.translation import ugettext_lazy as _

from django.utils.encoding import python_2_unicode_compatible
from paintstore.fields import ColorPickerField

@python_2_unicode_compatible
class PresentationAccordion(CMSPlugin):
    custom_classes = models.CharField(_('custom classes'), max_length=200, blank=True)
    custom_min_width = models.IntegerField(_('custom minimum width'), null=True, blank=True,
                                           help_text=_("Size for closed accordion, if not set default is 7% of the device screen"))
    custom_max_width = models.IntegerField(_('custom maximum width'), null=True, blank=True,
                                           help_text=_("Size for open accordion, if not set default is 80% of the device screen"))
    custom_duration = models.IntegerField(_('custom duration in milliseconds'), null=True, blank=True,
                                           help_text=_("Jquery Animation duration in milliseconds, if not set default is 300"))
    
    def __str__(self):
        return _("%s columns") % self.cmsplugin_set.all().count()

@python_2_unicode_compatible
class PresentationModel(CMSPlugin):
    
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500,  blank=True, null=True)
    
    icon = models.ImageField(upload_to='icons')
    photo = models.ImageField(upload_to='photos')
    
    color = ColorPickerField()
    
    page_link = models.ForeignKey(Page, verbose_name=_("page"), 
        help_text=_("If present image will be clickable"), blank=True,
        null=True, limit_choices_to={'publisher_is_draft': True})
       
    search_fields = ('short_description',)

    def __str__(self):
         return self.title

@python_2_unicode_compatible     
class FieldPresentation(CMSPlugin):
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='icons')
    color = ColorPickerField()
    align = models.CharField(max_length=1, default='h',
                              choices=(('v', _('Vertical')), ('h', _('Horizontal')) ) 
                             )    
    
    search_fields = ('title',)
    
    def __str__(self):
        return self.title
