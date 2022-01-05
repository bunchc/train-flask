# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.test import BaseTestCase


class TestPowerController(BaseTestCase):
    """PowerController integration test stubs"""

    def test_power_get(self):
        """Test case for power_get

        Returns the power state of the layout
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/power',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_power_train_id_get(self):
        """Test case for power_train_id_get

        Gets the power status of a given train.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/power/{train_id}'.format(train_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
