from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


"""
S3DisableForceDestroy external check will ensure that the S3 bucket has the force_destroy 
argument disabled. This check is created to ensure the objects within the S3 bucket are
 protected from accidental deletion since the objects cannot be recovered.
"""

# https://www.checkov.io/2.Concepts/Custom%20Policies.html


class S3DisableForceDestroy(BaseResourceCheck):
    def __init__(self):
        name = "Ensure bucket force destroy is disabled."
        id = "CKV_AWS_001"
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
        if "force_destroy" in conf.keys():
            if conf["force_destroy"][0]:
                return CheckResult.FAILED
        return CheckResult.PASSED


scanner = S3DisableForceDestroy()
