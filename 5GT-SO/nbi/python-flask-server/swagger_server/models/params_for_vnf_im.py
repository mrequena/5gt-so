# Author: Jordi Baranda
# Copyright (C) 2019 CTTC/CERCA
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


class ParamsForVnfIm(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, vnf_profile_id: str=None, additional_param: Dict[str, str]=None):  # noqa: E501
        """ParamsForVnfIm - a model defined in Swagger

        :param vnf_profile_id: The vnf_profile_id of this ParamsForVnfIm.  # noqa: E501
        :type vnf_profile_id: str
        :param additional_param: The additional_param of this ParamsForVnfIm.  # noqa: E501
        :type additional_param: Dict[str, str]
        """
        self.swagger_types = {
            "vnf_profile_id": str,
            "additional_param": Dict[str, str]
        }

        self.attribute_map = {
            "vnf_profile_id": "vnfProfileId",
            "additional_param": "additionalParam"
        }

        self._vnf_profile_id = vnf_profile_id
        self._additional_param = additional_param

    @classmethod
    def from_dict(cls, dikt) -> "ParamsForVnfIm":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ParamsForVnf_im of this ParamsForVnfIm.  # noqa: E501
        :rtype: ParamsForVnfIm
        """
        return util.deserialize_model(dikt, cls)

    @property
    def vnf_profile_id(self) -> str:
        """Gets the vnf_profile_id of this ParamsForVnfIm.


        :return: The vnf_profile_id of this ParamsForVnfIm.
        :rtype: str
        """
        return self._vnf_profile_id

    @vnf_profile_id.setter
    def vnf_profile_id(self, vnf_profile_id: str):
        """Sets the vnf_profile_id of this ParamsForVnfIm.


        :param vnf_profile_id: The vnf_profile_id of this ParamsForVnfIm.
        :type vnf_profile_id: str
        """
        if vnf_profile_id is None:
            raise ValueError("Invalid value for `vnf_profile_id`, must not be `None`")  # noqa: E501

        self._vnf_profile_id = vnf_profile_id

    @property
    def additional_param(self) -> Dict[str, str]:
        """Gets the additional_param of this ParamsForVnfIm.


        :return: The additional_param of this ParamsForVnfIm.
        :rtype: Dict[str, str]
        """
        return self._additional_param

    @additional_param.setter
    def additional_param(self, additional_param: Dict[str, str]):
        """Sets the additional_param of this ParamsForVnfIm.


        :param additional_param: The additional_param of this ParamsForVnfIm.
        :type additional_param: Dict[str, str]
        """

        self._additional_param = additional_param
