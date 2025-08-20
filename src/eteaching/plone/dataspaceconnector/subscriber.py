
from eteaching.plone.dataspaceconnector.utils import is_published
from eteaching.plone.dataspaceconnector import tasks


def transition_event(context, event):
    """Listens to internal 'transition' events of plone cms"""

    if is_published(context):
        tasks.create_node(context)

    if not is_published(context):
        tasks.delete_node(context)

    return


def modified(context, event):
    """Listens to internal 'modified' and 'deleted' events of plone cms"""
    
    if is_published(context):
        tasks.modify_node(context)

    if not is_published(context):
        tasks.delete_node(context)

    return
