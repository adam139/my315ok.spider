
from five import grok
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
 from plone.dexterity.interfaces import IDexterityContent

class store_location(grok.View):
    grok.context(IDexterityContent)
    grok.require('zope2.View')
