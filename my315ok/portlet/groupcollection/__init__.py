from zope.i18nmessageid import MessageFactory
groupcollectionMessageFactory = MessageFactory('my315ok.portlet.groupcollection')
ploneMessageFactory = MessageFactory('plone')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
