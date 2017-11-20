# coding: utf-8

"""
    KubeVirt API, 

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1OSType(object):
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
        'arch': 'str',
        'machine': 'str',
        'os': 'str'
    }

    attribute_map = {
        'arch': 'arch',
        'machine': 'machine',
        'os': 'os'
    }

    def __init__(self, arch=None, machine=None, os=None):
        """
        V1OSType - a model defined in Swagger
        """

        self._arch = None
        self._machine = None
        self._os = None

        if arch is not None:
          self.arch = arch
        if machine is not None:
          self.machine = machine
        self.os = os

    @property
    def arch(self):
        """
        Gets the arch of this V1OSType.

        :return: The arch of this V1OSType.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """
        Sets the arch of this V1OSType.

        :param arch: The arch of this V1OSType.
        :type: str
        """

        self._arch = arch

    @property
    def machine(self):
        """
        Gets the machine of this V1OSType.

        :return: The machine of this V1OSType.
        :rtype: str
        """
        return self._machine

    @machine.setter
    def machine(self, machine):
        """
        Sets the machine of this V1OSType.

        :param machine: The machine of this V1OSType.
        :type: str
        """

        self._machine = machine

    @property
    def os(self):
        """
        Gets the os of this V1OSType.

        :return: The os of this V1OSType.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """
        Sets the os of this V1OSType.

        :param os: The os of this V1OSType.
        :type: str
        """
        if os is None:
            raise ValueError("Invalid value for `os`, must not be `None`")

        self._os = os

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
        if not isinstance(other, V1OSType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other