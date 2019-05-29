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
from swagger_server.models.scale_ns_by_steps_data_im import ScaleNsByStepsDataIm  # noqa: F401,E501
from swagger_server.models.scale_ns_to_level_data_im import ScaleNsToLevelDataIm  # noqa: F401,E501
from swagger_server.models.vnf_instance_data_im import VnfInstanceDataIm  # noqa: F401,E501
from swagger_server import util


class ScaleNsDataIm(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, vnf_instance_to_be_added: List[VnfInstanceDataIm]=None, vnf_instance_to_be_removed: List[str]=None, scale_ns_by_steps_data: ScaleNsByStepsDataIm=None, scale_ns_to_level_data: ScaleNsToLevelDataIm=None, additional_param_for_ns: Dict[str, str]=None):  # noqa: E501
        """ScaleNsDataIm - a model defined in Swagger

        :param vnf_instance_to_be_added: The vnf_instance_to_be_added of this ScaleNsDataIm.  # noqa: E501
        :type vnf_instance_to_be_added: List[VnfInstanceDataIm]
        :param vnf_instance_to_be_removed: The vnf_instance_to_be_removed of this ScaleNsDataIm.  # noqa: E501
        :type vnf_instance_to_be_removed: List[str]
        :param scale_ns_by_steps_data: The scale_ns_by_steps_data of this ScaleNsDataIm.  # noqa: E501
        :type scale_ns_by_steps_data: ScaleNsByStepsDataIm
        :param scale_ns_to_level_data: The scale_ns_to_level_data of this ScaleNsDataIm.  # noqa: E501
        :type scale_ns_to_level_data: ScaleNsToLevelDataIm
        :param additional_param_for_ns: The additional_param_for_ns of this ScaleNsDataIm.  # noqa: E501
        :type additional_param_for_ns: Dict[str, str]
        """
        self.swagger_types = {
            "vnf_instance_to_be_added": List[VnfInstanceDataIm],
            "vnf_instance_to_be_removed": List[str],
            "scale_ns_by_steps_data": ScaleNsByStepsDataIm,
            "scale_ns_to_level_data": ScaleNsToLevelDataIm,
            "additional_param_for_ns": Dict[str, str]
        }

        self.attribute_map = {
            "vnf_instance_to_be_added": "vnfInstanceToBeAdded",
            "vnf_instance_to_be_removed": "vnfInstanceToBeRemoved",
            "scale_ns_by_steps_data": "scaleNsByStepsData",
            "scale_ns_to_level_data": "scaleNsToLevelData",
            "additional_param_for_ns": "additionalParamForNs"
        }

        self._vnf_instance_to_be_added = vnf_instance_to_be_added
        self._vnf_instance_to_be_removed = vnf_instance_to_be_removed
        self._scale_ns_by_steps_data = scale_ns_by_steps_data
        self._scale_ns_to_level_data = scale_ns_to_level_data
        self._additional_param_for_ns = additional_param_for_ns

    @classmethod
    def from_dict(cls, dikt) -> "ScaleNsDataIm":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ScaleNsData_im of this ScaleNsDataIm.  # noqa: E501
        :rtype: ScaleNsDataIm
        """
        return util.deserialize_model(dikt, cls)

    @property
    def vnf_instance_to_be_added(self) -> List[VnfInstanceDataIm]:
        """Gets the vnf_instance_to_be_added of this ScaleNsDataIm.


        :return: The vnf_instance_to_be_added of this ScaleNsDataIm.
        :rtype: List[VnfInstanceDataIm]
        """
        return self._vnf_instance_to_be_added

    @vnf_instance_to_be_added.setter
    def vnf_instance_to_be_added(self, vnf_instance_to_be_added: List[VnfInstanceDataIm]):
        """Sets the vnf_instance_to_be_added of this ScaleNsDataIm.


        :param vnf_instance_to_be_added: The vnf_instance_to_be_added of this ScaleNsDataIm.
        :type vnf_instance_to_be_added: List[VnfInstanceDataIm]
        """

        self._vnf_instance_to_be_added = vnf_instance_to_be_added

    @property
    def vnf_instance_to_be_removed(self) -> List[str]:
        """Gets the vnf_instance_to_be_removed of this ScaleNsDataIm.


        :return: The vnf_instance_to_be_removed of this ScaleNsDataIm.
        :rtype: List[str]
        """
        return self._vnf_instance_to_be_removed

    @vnf_instance_to_be_removed.setter
    def vnf_instance_to_be_removed(self, vnf_instance_to_be_removed: List[str]):
        """Sets the vnf_instance_to_be_removed of this ScaleNsDataIm.


        :param vnf_instance_to_be_removed: The vnf_instance_to_be_removed of this ScaleNsDataIm.
        :type vnf_instance_to_be_removed: List[str]
        """

        self._vnf_instance_to_be_removed = vnf_instance_to_be_removed

    @property
    def scale_ns_by_steps_data(self) -> ScaleNsByStepsDataIm:
        """Gets the scale_ns_by_steps_data of this ScaleNsDataIm.


        :return: The scale_ns_by_steps_data of this ScaleNsDataIm.
        :rtype: ScaleNsByStepsDataIm
        """
        return self._scale_ns_by_steps_data

    @scale_ns_by_steps_data.setter
    def scale_ns_by_steps_data(self, scale_ns_by_steps_data: ScaleNsByStepsDataIm):
        """Sets the scale_ns_by_steps_data of this ScaleNsDataIm.


        :param scale_ns_by_steps_data: The scale_ns_by_steps_data of this ScaleNsDataIm.
        :type scale_ns_by_steps_data: ScaleNsByStepsDataIm
        """

        self._scale_ns_by_steps_data = scale_ns_by_steps_data

    @property
    def scale_ns_to_level_data(self) -> ScaleNsToLevelDataIm:
        """Gets the scale_ns_to_level_data of this ScaleNsDataIm.


        :return: The scale_ns_to_level_data of this ScaleNsDataIm.
        :rtype: ScaleNsToLevelDataIm
        """
        return self._scale_ns_to_level_data

    @scale_ns_to_level_data.setter
    def scale_ns_to_level_data(self, scale_ns_to_level_data: ScaleNsToLevelDataIm):
        """Sets the scale_ns_to_level_data of this ScaleNsDataIm.


        :param scale_ns_to_level_data: The scale_ns_to_level_data of this ScaleNsDataIm.
        :type scale_ns_to_level_data: ScaleNsToLevelDataIm
        """

        self._scale_ns_to_level_data = scale_ns_to_level_data

    @property
    def additional_param_for_ns(self) -> Dict[str, str]:
        """Gets the additional_param_for_ns of this ScaleNsDataIm.


        :return: The additional_param_for_ns of this ScaleNsDataIm.
        :rtype: Dict[str, str]
        """
        return self._additional_param_for_ns

    @additional_param_for_ns.setter
    def additional_param_for_ns(self, additional_param_for_ns: Dict[str, str]):
        """Sets the additional_param_for_ns of this ScaleNsDataIm.


        :param additional_param_for_ns: The additional_param_for_ns of this ScaleNsDataIm.
        :type additional_param_for_ns: Dict[str, str]
        """

        self._additional_param_for_ns = additional_param_for_ns