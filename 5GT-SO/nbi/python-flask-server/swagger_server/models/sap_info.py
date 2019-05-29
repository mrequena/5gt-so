# Copyright (C) 2018 CTTC/CERCA
# License: To be defined. Currently use is restricted to partners of the 5G-Transformer project,
#          http://5g-transformer.eu/, no use or redistribution of any kind outside the 5G-Transformer project is
#          allowed.
# Disclaimer: this software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied.

# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SapInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, sap_instance_id: str=None, sap_name: str=None, description: str=None, address: str=None):  # noqa: E501
        """SapInfo - a model defined in Swagger

        :param sap_instance_id: The sap_instance_id of this SapInfo.  # noqa: E501
        :type sap_instance_id: str
        :param sap_name: The sap_name of this SapInfo.  # noqa: E501
        :type sap_name: str
        :param description: The description of this SapInfo.  # noqa: E501
        :type description: str
        :param address: The address of this SapInfo.  # noqa: E501
        :type address: str
        """
        self.swagger_types = {
            'sap_instance_id': str,
            'sap_name': str,
            'description': str,
            'address': str
        }

        self.attribute_map = {
            'sap_instance_id': 'sapInstanceId',
            'sap_name': 'sapName',
            'description': 'description',
            'address': 'address'
        }

        self._sap_instance_id = sap_instance_id
        self._sap_name = sap_name
        self._description = description
        self._address = address

    @classmethod
    def from_dict(cls, dikt) -> 'SapInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SapInfo of this SapInfo.  # noqa: E501
        :rtype: SapInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sap_instance_id(self) -> str:
        """Gets the sap_instance_id of this SapInfo.


        :return: The sap_instance_id of this SapInfo.
        :rtype: str
        """
        return self._sap_instance_id

    @sap_instance_id.setter
    def sap_instance_id(self, sap_instance_id: str):
        """Sets the sap_instance_id of this SapInfo.


        :param sap_instance_id: The sap_instance_id of this SapInfo.
        :type sap_instance_id: str
        """

        self._sap_instance_id = sap_instance_id

    @property
    def sap_name(self) -> str:
        """Gets the sap_name of this SapInfo.


        :return: The sap_name of this SapInfo.
        :rtype: str
        """
        return self._sap_name

    @sap_name.setter
    def sap_name(self, sap_name: str):
        """Sets the sap_name of this SapInfo.


        :param sap_name: The sap_name of this SapInfo.
        :type sap_name: str
        """

        self._sap_name = sap_name

    @property
    def description(self) -> str:
        """Gets the description of this SapInfo.


        :return: The description of this SapInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this SapInfo.


        :param description: The description of this SapInfo.
        :type description: str
        """

        self._description = description

    @property
    def address(self) -> str:
        """Gets the address of this SapInfo.


        :return: The address of this SapInfo.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """Sets the address of this SapInfo.


        :param address: The address of this SapInfo.
        :type address: str
        """

        self._address = address
