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


class ManagedRuleSet(Model):
    """Defines a managed rule set.

    All required parameters must be populated in order to send to Azure.

    :param rule_set_type: Required. Defines the rule set type to use.
    :type rule_set_type: str
    :param rule_set_version: Required. Defines the version of the rule set to
     use.
    :type rule_set_version: str
    :param anomaly_score: Verizon only : If the rule set supports anomaly
     detection mode, this describes the threshold for blocking requests.
    :type anomaly_score: int
    :param rule_group_overrides: Defines the rule overrides to apply to the
     rule set.
    :type rule_group_overrides:
     list[~azure.mgmt.cdn.models.ManagedRuleGroupOverride]
    """

    _validation = {
        'rule_set_type': {'required': True},
        'rule_set_version': {'required': True},
        'anomaly_score': {'maximum': 20, 'minimum': 0},
    }

    _attribute_map = {
        'rule_set_type': {'key': 'ruleSetType', 'type': 'str'},
        'rule_set_version': {'key': 'ruleSetVersion', 'type': 'str'},
        'anomaly_score': {'key': 'anomalyScore', 'type': 'int'},
        'rule_group_overrides': {'key': 'ruleGroupOverrides', 'type': '[ManagedRuleGroupOverride]'},
    }

    def __init__(self, *, rule_set_type: str, rule_set_version: str, anomaly_score: int=None, rule_group_overrides=None, **kwargs) -> None:
        super(ManagedRuleSet, self).__init__(**kwargs)
        self.rule_set_type = rule_set_type
        self.rule_set_version = rule_set_version
        self.anomaly_score = anomaly_score
        self.rule_group_overrides = rule_group_overrides