# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DesiredState(Model):
    """DesiredState.

    :param code: Status code for the operation.
    :type code: int
    :param version: Version of the desired value received.
    :type version: long
    :param description: Description of the status.
    :type description: str
    """

    _attribute_map = {
        "code": {"key": "code", "type": "int"},
        "version": {"key": "version", "type": "long"},
        "description": {"key": "description", "type": "str"},
    }

    def __init__(
        self, *, code: int = None, version: int = None, description: str = None, **kwargs
    ) -> None:
        super(DesiredState, self).__init__(**kwargs)
        self.code = code
        self.version = version
        self.description = description
