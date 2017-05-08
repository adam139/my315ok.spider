from five import grok
from zope import schema

from plone.directives import form, dexterity

from my315ok.spider import _

class Istore(form.Schema):
    """
    html source files and image files saving configuration
    """
