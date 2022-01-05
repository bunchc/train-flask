# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.one_of_speed_startboolean import OneOfSpeedStartboolean  # noqa: E501
from openapi_server.models.train import Train  # noqa: E501
from openapi_server.models.unknownbasetype import UNKNOWN_BASE_TYPE  # noqa: E501
from openapi_server.test import BaseTestCase


class TestTrainController(BaseTestCase):
    """TrainController integration test stubs"""

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

    def test_train_get(self):
        """Test case for train_get

        Returns a JSON arry of configured trains.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/train',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_train_train_id_action_post(self):
        """Test case for train_train_id_action_post

        Performs an action on a given train.
        """
        unknown_base_type = openapi_server.UNKNOWN_BASE_TYPE()
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/train/{train_id}/{action}'.format(train_id=56, action='action_example'),
            method='POST',
            headers=headers,
            data=json.dumps(unknown_base_type),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_train_train_idget(self):
        """Test case for train_train_idget

        Returns the status of a specific train.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/train/{train_id}'.format(train_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
