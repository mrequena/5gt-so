# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.ll_capacity import LLCapacity  # noqa: F401,E501
from swagger_server.models.ll_destination import LLDestination  # noqa: F401,E501
from swagger_server.models.ll_source import LLSource  # noqa: F401,E501
from swagger_server import util


class LL(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, length=None, l_lid=None, capacity=None, delay=None, source=None, destination=None):  # noqa: E501
        """LL - a model defined in Swagger

        :param length: The length of this LL.  # noqa: E501
        :type length: float
        :param l_lid: The l_lid of this LL.  # noqa: E501
        :type l_lid: str
        :param capacity: The capacity of this LL.  # noqa: E501
        :type capacity: LLCapacity
        :param delay: The delay of this LL.  # noqa: E501
        :type delay: float
        :param source: The source of this LL.  # noqa: E501
        :type source: LLSource
        :param destination: The destination of this LL.  # noqa: E501
        :type destination: LLDestination
        """
        self.swagger_types = {
            'length': float,
            'l_lid': str,
            'capacity': LLCapacity,
            'delay': float,
            'source': LLSource,
            'destination': LLDestination
        }

        self.attribute_map = {
            'length': 'length',
            'l_lid': 'LLid',
            'capacity': 'capacity',
            'delay': 'delay',
            'source': 'source',
            'destination': 'destination'
        }

        self._length = length
        self._l_lid = l_lid
        self._capacity = capacity
        self._delay = delay
        self._source = source
        self._destination = destination

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LL of this LL.  # noqa: E501
        :rtype: LL
        """
        return util.deserialize_model(dikt, cls)

    @property
    def length(self):
        """Gets the length of this LL.


        :return: The length of this LL.
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this LL.


        :param length: The length of this LL.
        :type length: float
        """

        self._length = length

    @property
    def l_lid(self):
        """Gets the l_lid of this LL.

        Logical Link identifier  # noqa: E501

        :return: The l_lid of this LL.
        :rtype: str
        """
        return self._l_lid

    @l_lid.setter
    def l_lid(self, l_lid):
        """Sets the l_lid of this LL.

        Logical Link identifier  # noqa: E501

        :param l_lid: The l_lid of this LL.
        :type l_lid: str
        """
        if l_lid is None:
            raise ValueError("Invalid value for `l_lid`, must not be `None`")  # noqa: E501

        self._l_lid = l_lid

    @property
    def capacity(self):
        """Gets the capacity of this LL.


        :return: The capacity of this LL.
        :rtype: LLCapacity
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this LL.


        :param capacity: The capacity of this LL.
        :type capacity: LLCapacity
        """
        if capacity is None:
            raise ValueError("Invalid value for `capacity`, must not be `None`")  # noqa: E501

        self._capacity = capacity

    @property
    def delay(self):
        """Gets the delay of this LL.

        Logical Link delay  # noqa: E501

        :return: The delay of this LL.
        :rtype: float
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this LL.

        Logical Link delay  # noqa: E501

        :param delay: The delay of this LL.
        :type delay: float
        """
        if delay is None:
            raise ValueError("Invalid value for `delay`, must not be `None`")  # noqa: E501

        self._delay = delay

    @property
    def source(self):
        """Gets the source of this LL.


        :return: The source of this LL.
        :rtype: LLSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this LL.


        :param source: The source of this LL.
        :type source: LLSource
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def destination(self):
        """Gets the destination of this LL.


        :return: The destination of this LL.
        :rtype: LLDestination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this LL.


        :param destination: The destination of this LL.
        :type destination: LLDestination
        """
        if destination is None:
            raise ValueError("Invalid value for `destination`, must not be `None`")  # noqa: E501

        self._destination = destination