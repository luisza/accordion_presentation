

from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import  PresentationModel, PresentationAccordion, FieldPresentation



class AccordionPlugin(CMSPluginBase):
    model = PresentationAccordion
    name = _('Accordion presentation')
    #module = _('Accordion')
    render_template = 'accordion_presentation/accordion.html'
    allow_children = True
    child_classes = ['PresentationPlugin']
    
    def render(self, context, instance, placeholder):
        context.update({
            'accordion': instance,
            'placeholder': placeholder,
        })
        return context

class PresentationPlugin(CMSPluginBase):
    model = PresentationModel                # Model where data about this plugin is saved
    name = _("Presentation Plugin")                 # Name of the plugin
    render_template = "accordion_presentation/plugin.html"   # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({'instance':instance,
                        'placeholder': placeholder,})
        return context


class FieldPlugin(CMSPluginBase):
    model = FieldPresentation
    name = _('Field accordion presentation')
    render_template = 'accordion_presentation/field.html'
    allow_children = False
    

plugin_pool.register_plugin(AccordionPlugin)
plugin_pool.register_plugin(PresentationPlugin) # register the plugin
plugin_pool.register_plugin(FieldPlugin)
