# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class ErrorResponse(Model):
    """Error response indicates that the service is not able to process the
    incoming request. The reason is provided in the error message.

    :param error: The details of the error.
    :type error: ~azure.mgmt.consumption.models.ErrorDetails
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetails'},
    }

    def __init__(self, error=None):
        self.error = error


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)
