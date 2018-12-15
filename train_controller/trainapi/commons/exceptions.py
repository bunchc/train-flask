# -*- coding: utf-8 -*-

"""
    trainapi.commons.exceptions
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Wrapper logic around the Adafruit MotorHAT

    :license: BSD, see LICENSE for more details.
"""

error = ({
    3: {
        'errorID': '3',
        'name': 'Missing JSON',
        'description': 'Missing JSON in request.',
        'response': 400
    },
    4: {
        'errorID': '4',
        'name': 'Missing locomotive_id',
        'description': 'Request must specify a locomotive with ``locomotive_id``',
        'response': 400
    },
    5: {
        'errorID': '5',
        'name': 'Missing action',
        'description': 'Request must specify an action.',
        'response': 400
    },
    6: {
        'errorID': '5',
        'name': 'Missing parameter',
        'description': 'Request is missing parameters.',
        'response': 400        
    }
})