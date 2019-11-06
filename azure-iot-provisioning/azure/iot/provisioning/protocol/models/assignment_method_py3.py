# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AssignmentMethod(Model):
    """AssignmentMethod.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: CustomAssignmentMethod, GeoLatencyAssignmentMethod,
    HashedAssignmentMethod, StaticAssignmentMethod

    All required parameters must be populated in order to send to Azure.

    :param assignment_type: Required. Constant filled by server.
    :type assignment_type: str
    """

    _validation = {"assignment_type": {"required": True}}

    _attribute_map = {"assignment_type": {"key": "assignmentType", "type": "str"}}

    _subtype_map = {
        "assignment_type": {
            "CustomAssignmentMethod": "CustomAssignmentMethod",
            "GeoLatencyAssignmentMethod": "GeoLatencyAssignmentMethod",
            "HashedAssignmentMethod": "HashedAssignmentMethod",
            "StaticAssignmentMethod": "StaticAssignmentMethod",
        }
    }

    def __init__(self, **kwargs) -> None:
        super(AssignmentMethod, self).__init__(**kwargs)
        self.assignment_type = None