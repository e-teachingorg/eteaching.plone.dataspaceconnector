from plone import api

from plone.uuid.interfaces import IUUID
from Products.CMFCore.WorkflowCore import WorkflowException


def is_published(obj):
    try:
        state = api.content.get_state(obj)
    except WorkflowException:
        return False
    except api.exc.CannotGetPortalError:
        return False
    except api.exc.InvalidParameterError:
        return False
    if state == "published":
        return True
    return False


def eid(obj):
    """Return external id"""
    uuid = IUUID(obj, None)
    if not uuid:
        return None
    return f"et_{uuid}"
