from django.db import models
from cms.models import CMSPlugin, Page
from django.utils.translation import ugettext_lazy as _

from django.utils.encoding import python_2_unicode_compatible
from paintstore.fields import ColorPickerField

from django.conf import settings
from django.core.checks import Error

@python_2_unicode_compatible
class PresentationAccordion(CMSPlugin):
    FX = (('none', 'None'),
          ('fade', 'Fade'),
          ('fadeout', 'Fadeout'),
          ('scrollHorz', 'Scroll Horizontal'),
          ('tileBlind', 'Tile Blind'),
          )
    
    custom_classes = models.CharField(_('custom classes'), max_length=200, blank=True)  
    custom_height = models.IntegerField(_('custom height porcentaje'), null=True, blank=True,
                                        help_text=_("It is a number between 0 and 100"))
    custom_width = models.IntegerField(_('custom width porcentaje'), null=True, blank=True,
                                       help_text=_("It is a number between 0 and 100"))
    custom_duration = models.IntegerField(_('custom duration in milliseconds'), null=True, blank=True,
                                           help_text=_("Jquery Animation duration in milliseconds,ignore if not set"))
    background_color = ColorPickerField(null=True, blank=True)
    
    cycle_fx = models.CharField(_('Type of transition'), max_length=200, choices=FX, default="none")  
    
    def __str__(self):
        return _("%s columns") % self.cmsplugin_set.all().count()
    
    @classmethod
    def check(cls, **kwargs):
        errors = super(PresentationAccordion, cls).check(**kwargs)
        if not 'paintstore' in settings.INSTALLED_APPS:
            errors.append( Error(
                                'No paintstore in  INSTALLED_APPS ',
                                hint=None,
                                obj=None,
                                id='accordion_presentation.E001',
                              )
        )
        return errors

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
