from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories
from lark import Token


"""
S3DisableForceDestroy external check will ensure that the S3 bucket has the force_destroy 
argument disabled. This check is created to ensure the objects within the S3 bucket are
 protected from accidental deletion since the objects cannot be recovered.
"""

# https://www.checkov.io/2.Concepts/Custom%20Policies.html


class EnforcePurposeTags(BaseResourceCheck):
    def __init__(self):
        name = 'Ensure the resource is tagged with Purpose = "checkov" tag.'
        id = "CKV_AWS_002"
        supported_resources = ["aws_s3_bucket"]
        # CheckCategories are defined in models/enums.py
        categories = [CheckCategories.BACKUP_AND_RECOVERY]
        super().__init__(
            name=name,
            id=id,
            categories=categories,
            supported_resources=supported_resources,
        )

    def scan_resource_conf(self, conf):
        """
        Looks for force destroy configuration in aws_s3_bucket argument reference:
        https://www.terraform.io/docs/providers/aws/r/s3_bucket.html
        :param conf: aws_s3_bucket configuration
        :return: <CheckResult>
        """
        if "tags" in conf.keys():
            environment_tag = "Purpose"
            if environment_tag in conf["tags"][0].keys():
                if conf["tags"][0][environment_tag] == "checkov":
                    return CheckResult.PASSED
        return CheckResult.FAILED


scanner = EnforcePurposeTags()
