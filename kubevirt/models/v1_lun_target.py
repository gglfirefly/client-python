# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1LunTarget(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bus': 'str',
        'readonly': 'bool'
    }

    attribute_map = {
        'bus': 'bus',
        'readonly': 'readonly'
    }

    def __init__(self, bus=None, readonly=None):
        """
        V1LunTarget - a model defined in Swagger
        """

        self._bus = None
        self._readonly = None

        if bus is not None:
          self.bus = bus
        if readonly is not None:
          self.readonly = readonly

    @property
    def bus(self):
        """
        Gets the bus of this V1LunTarget.
        Bus indicates the type of disk device to emulate. supported values: virtio, sata, scsi, ide.

        :return: The bus of this V1LunTarget.
        :rtype: str
        """
        return self._bus

    @bus.setter
    def bus(self, bus):
        """
        Sets the bus of this V1LunTarget.
        Bus indicates the type of disk device to emulate. supported values: virtio, sata, scsi, ide.

        :param bus: The bus of this V1LunTarget.
        :type: str
        """

        self._bus = bus

    @property
    def readonly(self):
        """
        Gets the readonly of this V1LunTarget.
        ReadOnly. Defaults to false.

        :return: The readonly of this V1LunTarget.
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        """
        Sets the readonly of this V1LunTarget.
        ReadOnly. Defaults to false.

        :param readonly: The readonly of this V1LunTarget.
        :type: bool
        """

        self._readonly = readonly

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1LunTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
