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

from .answer import Answer


class Computation(Answer):
    """Defines an expression and its answer.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param _type: Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar follow_up_queries:
    :vartype follow_up_queries:
     list[~azure.cognitiveservices.search.websearch.models.Query]
    :param expression: The math or conversion expression. If the query
     contains a request to convert units of measure (for example, meters to
     feet), this field contains the from units and value contains the to units.
     If the query contains a mathematical expression such as 2+2, this field
     contains the expression and value contains the answer. Note that
     mathematical expressions may be normalized. For example, if the query was
     sqrt(4^2+8^2), the normalized expression may be sqrt((4^2)+(8^2)). If the
     user's query is a math question and the textDecorations query parameter is
     set to true, the expression string may include formatting markers. For
     example, if the user's query is log(2), the normalized expression includes
     the subscript markers. For more information, see Hit Highlighting.
    :type expression: str
    :param value: The expression's answer.
    :type value: str
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'web_search_url': {'readonly': True},
        'follow_up_queries': {'readonly': True},
        'expression': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'follow_up_queries': {'key': 'followUpQueries', 'type': '[Query]'},
        'expression': {'key': 'expression', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, expression, value):
        super(Computation, self).__init__()
        self.expression = expression
        self.value = value
        self._type = 'Computation'