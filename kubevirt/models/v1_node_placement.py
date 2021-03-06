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


class V1NodePlacement(object):
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
        'affinity': 'K8sIoApiCoreV1Affinity',
        'node_selector': 'dict(str, str)',
        'tolerations': 'list[K8sIoApiCoreV1Toleration]'
    }

    attribute_map = {
        'affinity': 'affinity',
        'node_selector': 'nodeSelector',
        'tolerations': 'tolerations'
    }

    def __init__(self, affinity=None, node_selector=None, tolerations=None):
        """
        V1NodePlacement - a model defined in Swagger
        """

        self._affinity = None
        self._node_selector = None
        self._tolerations = None

        if affinity is not None:
          self.affinity = affinity
        if node_selector is not None:
          self.node_selector = node_selector
        if tolerations is not None:
          self.tolerations = tolerations

    @property
    def affinity(self):
        """
        Gets the affinity of this V1NodePlacement.
        affinity enables pod affinity/anti-affinity placement expanding the types of constraints that can be expressed with nodeSelector. affinity is going to be applied to the relevant kind of pods in parallel with nodeSelector See https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity

        :return: The affinity of this V1NodePlacement.
        :rtype: K8sIoApiCoreV1Affinity
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        """
        Sets the affinity of this V1NodePlacement.
        affinity enables pod affinity/anti-affinity placement expanding the types of constraints that can be expressed with nodeSelector. affinity is going to be applied to the relevant kind of pods in parallel with nodeSelector See https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity

        :param affinity: The affinity of this V1NodePlacement.
        :type: K8sIoApiCoreV1Affinity
        """

        self._affinity = affinity

    @property
    def node_selector(self):
        """
        Gets the node_selector of this V1NodePlacement.
        nodeSelector is the node selector applied to the relevant kind of pods It specifies a map of key-value pairs: for the pod to be eligible to run on a node, the node must have each of the indicated key-value pairs as labels (it can have additional labels as well). See https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector

        :return: The node_selector of this V1NodePlacement.
        :rtype: dict(str, str)
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """
        Sets the node_selector of this V1NodePlacement.
        nodeSelector is the node selector applied to the relevant kind of pods It specifies a map of key-value pairs: for the pod to be eligible to run on a node, the node must have each of the indicated key-value pairs as labels (it can have additional labels as well). See https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector

        :param node_selector: The node_selector of this V1NodePlacement.
        :type: dict(str, str)
        """

        self._node_selector = node_selector

    @property
    def tolerations(self):
        """
        Gets the tolerations of this V1NodePlacement.
        tolerations is a list of tolerations applied to the relevant kind of pods See https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/ for more info. These are additional tolerations other than default ones.

        :return: The tolerations of this V1NodePlacement.
        :rtype: list[K8sIoApiCoreV1Toleration]
        """
        return self._tolerations

    @tolerations.setter
    def tolerations(self, tolerations):
        """
        Sets the tolerations of this V1NodePlacement.
        tolerations is a list of tolerations applied to the relevant kind of pods See https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/ for more info. These are additional tolerations other than default ones.

        :param tolerations: The tolerations of this V1NodePlacement.
        :type: list[K8sIoApiCoreV1Toleration]
        """

        self._tolerations = tolerations

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
        if not isinstance(other, V1NodePlacement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
