# coding=utf-8
"""Test for lesson models."""

from django.test import TestCase

from geocontext.models.context_service_registry import ContextServiceRegistry
from geocontext.tests.models.model_factories import ContextServiceRegistryF


class TestContextServiceRegistry(TestCase):
    """Test CSR models."""

    def test_ContextServiceRegistry_create(self):
        """Test section model creation."""

        model = ContextServiceRegistryF.create()

        # check if PK exists.
        self.assertTrue(model.pk is not None)

        # check if model name exists.
        self.assertTrue(model.name is not None)

    def test_retrieve_context_value(self):
        """Test retrieving context value from a point."""
        # 3095940,-3777677
        x = 3095940
        y = -3777677

        model = ContextServiceRegistryF.create()
        model.url = 'http://maps.kartoza.com/web/?map=/web/kartoza/kartoza.qgs'
        model.query_type = ContextServiceRegistry.WFS
        model.query_url = (
            'http://maps.kartoza.com/web/?map=/web/kartoza/kartoza.qgs&'
            'SERVICE=WFS&REQUEST=GetFeature&VERSION=1.0.0&'
            'TYPENAME=sa_provinces&SRSNAME=EPSG:3857&OUTPUTFORMAT=GML3&')
        model.result_regex = 'qgs:provname'

        model.save()

        value = model.retrieve_context_value(x, y)
        self.assertEqual('Eastern Cape', value)

        x = 31.72
        y = -27.88

        model_2 = ContextServiceRegistryF.create()
        model_2.url = (
            'http://maps.kartoza.com/web/?map=/web/kartoza/kartoza.qgs')
        model_2.query_type = ContextServiceRegistry.WFS
        model_2.query_url = (
            'http://maps.kartoza.com/web/?map=/web/kartoza/kartoza.qgs&'
            'SERVICE=WFS&REQUEST=GetFeature&VERSION=1.0.0&'
            'TYPENAME=water_management_area&'
            'SRSNAME=EPSG:4326&OUTPUTFORMAT=GML3&')
        model_2.result_regex = 'qgs:name'

        model_2.save()

        value = model_2.retrieve_context_value(x, y)
        self.assertEqual('6 - Usutu to Mhlathuze', value)
