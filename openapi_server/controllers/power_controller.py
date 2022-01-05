import connexion
import six

from openapi_server import util


def power_get():  # noqa: E501
    """Returns the power state of the layout

    Returns the power state of the layout # noqa: E501


    :rtype: bool
    """
    return 'do some magic!'


def power_train_id_get(train_id):  # noqa: E501
    """Gets the power status of a given train.

    Gets the power status of a given train  # noqa: E501

    :param train_id: Train ID
    :type train_id: int

    :rtype: bool
    """
    return 'do some magic!'
