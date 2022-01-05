import connexion
import six

from openapi_server.models.one_of_speed_startboolean import OneOfSpeedStartboolean  # noqa: E501
from openapi_server.models.train import Train  # noqa: E501
from openapi_server.models.unknownbasetype import UNKNOWN_BASE_TYPE  # noqa: E501
from openapi_server import util


def power_train_id_get(train_id):  # noqa: E501
    """Gets the power status of a given train.

    Gets the power status of a given train  # noqa: E501

    :param train_id: Train ID
    :type train_id: int

    :rtype: bool
    """
    return 'do some magic!'


def train_get():  # noqa: E501
    """Returns a JSON arry of configured trains.

    Returns a JSON array of all trains currently configured.  # noqa: E501


    :rtype: Train
    """
    return 'do some magic!'


def train_train_id_action_post(train_id, action, unknown_base_type):  # noqa: E501
    """Performs an action on a given train.

    Performs an action on a train. A list of actions can be returned by sending a GET request to /train/{trainID} start  - Accelerates a train to a given speed in a given direction  # noqa: E501

    :param train_id: Train ID
    :type train_id: int
    :param action: Action to perform on a train.
    :type action: str
    :param unknown_base_type: Parameters for a given action
    :type unknown_base_type: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        unknown_base_type = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def train_train_idget(train_id):  # noqa: E501
    """Returns the status of a specific train.

    Returns the status of a specific train  # noqa: E501

    :param train_id: Train ID
    :type train_id: int

    :rtype: Train
    """
    return 'do some magic!'
