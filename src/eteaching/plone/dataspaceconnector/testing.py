# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import eteaching.plone.dataspaceconnector


class EteachingPloneDataspaceconnectorLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=eteaching.plone.dataspaceconnector)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'eteaching.plone.dataspaceconnector:default')


ETEACHING_PLONE_DATASPACECONNECTOR_FIXTURE = EteachingPloneDataspaceconnectorLayer()


ETEACHING_PLONE_DATASPACECONNECTOR_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ETEACHING_PLONE_DATASPACECONNECTOR_FIXTURE,),
    name='EteachingPloneDataspaceconnectorLayer:IntegrationTesting',
)


ETEACHING_PLONE_DATASPACECONNECTOR_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ETEACHING_PLONE_DATASPACECONNECTOR_FIXTURE,),
    name='EteachingPloneDataspaceconnectorLayer:FunctionalTesting',
)


ETEACHING_PLONE_DATASPACECONNECTOR_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ETEACHING_PLONE_DATASPACECONNECTOR_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='EteachingPloneDataspaceconnectorLayer:AcceptanceTesting',
)
