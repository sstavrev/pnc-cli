# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from datetime import datetime
from pprint import pformat
from six import iteritems


class ArtifactRest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ArtifactRest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'identifier': 'str',
            'artifact_quality': 'str',
            'repo_type': 'str',
            'checksum': 'str',
            'filename': 'str',
            'deploy_url': 'str',
            'build_record_ids': 'list[int]',
            'dependant_build_record_ids': 'list[int]',
            'import_date': 'datetime',
            'origin_url': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'identifier': 'identifier',
            'artifact_quality': 'artifactQuality',
            'repo_type': 'repoType',
            'checksum': 'checksum',
            'filename': 'filename',
            'deploy_url': 'deployUrl',
            'build_record_ids': 'buildRecordIds',
            'dependant_build_record_ids': 'dependantBuildRecordIds',
            'import_date': 'importDate',
            'origin_url': 'originUrl',
            'status': 'status'
        }

        self._id = None
        self._identifier = None
        self._artifact_quality = None
        self._repo_type = None
        self._checksum = None
        self._filename = None
        self._deploy_url = None
        self._build_record_ids = None
        self._dependant_build_record_ids = None
        self._import_date = None
        self._origin_url = None
        self._status = None

    @property
    def id(self):
        """
        Gets the id of this ArtifactRest.


        :return: The id of this ArtifactRest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ArtifactRest.


        :param id: The id of this ArtifactRest.
        :type: int
        """
        self._id = id

    @property
    def identifier(self):
        """
        Gets the identifier of this ArtifactRest.


        :return: The identifier of this ArtifactRest.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this ArtifactRest.


        :param identifier: The identifier of this ArtifactRest.
        :type: str
        """
        self._identifier = identifier

    @property
    def artifact_quality(self):
        """
        Gets the artifact_quality of this ArtifactRest.


        :return: The artifact_quality of this ArtifactRest.
        :rtype: str
        """
        return self._artifact_quality

    @artifact_quality.setter
    def artifact_quality(self, artifact_quality):
        """
        Sets the artifact_quality of this ArtifactRest.


        :param artifact_quality: The artifact_quality of this ArtifactRest.
        :type: str
        """
        allowed_values = ["BUILT", "VERIFIED", "TESTED", "DEPRECATED", "BLACKLISTED", "IMPORTED"]
        if artifact_quality not in allowed_values:
            raise ValueError(
                "Invalid value for `artifact_quality`, must be one of {0}"
                .format(allowed_values)
            )
        self._artifact_quality = artifact_quality

    @property
    def repo_type(self):
        """
        Gets the repo_type of this ArtifactRest.


        :return: The repo_type of this ArtifactRest.
        :rtype: str
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type):
        """
        Sets the repo_type of this ArtifactRest.


        :param repo_type: The repo_type of this ArtifactRest.
        :type: str
        """
        allowed_values = ["MAVEN", "DOCKER_REGISTRY", "NPM", "COCOA_POD"]
        if repo_type not in allowed_values:
            raise ValueError(
                "Invalid value for `repo_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._repo_type = repo_type

    @property
    def checksum(self):
        """
        Gets the checksum of this ArtifactRest.


        :return: The checksum of this ArtifactRest.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """
        Sets the checksum of this ArtifactRest.


        :param checksum: The checksum of this ArtifactRest.
        :type: str
        """
        self._checksum = checksum

    @property
    def filename(self):
        """
        Gets the filename of this ArtifactRest.


        :return: The filename of this ArtifactRest.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """
        Sets the filename of this ArtifactRest.


        :param filename: The filename of this ArtifactRest.
        :type: str
        """
        self._filename = filename

    @property
    def deploy_url(self):
        """
        Gets the deploy_url of this ArtifactRest.


        :return: The deploy_url of this ArtifactRest.
        :rtype: str
        """
        return self._deploy_url

    @deploy_url.setter
    def deploy_url(self, deploy_url):
        """
        Sets the deploy_url of this ArtifactRest.


        :param deploy_url: The deploy_url of this ArtifactRest.
        :type: str
        """
        self._deploy_url = deploy_url

    @property
    def build_record_ids(self):
        """
        Gets the build_record_ids of this ArtifactRest.


        :return: The build_record_ids of this ArtifactRest.
        :rtype: list[int]
        """
        return self._build_record_ids

    @build_record_ids.setter
    def build_record_ids(self, build_record_ids):
        """
        Sets the build_record_ids of this ArtifactRest.


        :param build_record_ids: The build_record_ids of this ArtifactRest.
        :type: list[int]
        """
        self._build_record_ids = build_record_ids

    @property
    def dependant_build_record_ids(self):
        """
        Gets the dependant_build_record_ids of this ArtifactRest.


        :return: The dependant_build_record_ids of this ArtifactRest.
        :rtype: list[int]
        """
        return self._dependant_build_record_ids

    @dependant_build_record_ids.setter
    def dependant_build_record_ids(self, dependant_build_record_ids):
        """
        Sets the dependant_build_record_ids of this ArtifactRest.


        :param dependant_build_record_ids: The dependant_build_record_ids of this ArtifactRest.
        :type: list[int]
        """
        self._dependant_build_record_ids = dependant_build_record_ids

    @property
    def import_date(self):
        """
        Gets the import_date of this ArtifactRest.


        :return: The import_date of this ArtifactRest.
        :rtype: datetime
        """
        return self._import_date

    @import_date.setter
    def import_date(self, import_date):
        """
        Sets the import_date of this ArtifactRest.


        :param import_date: The import_date of this ArtifactRest.
        :type: datetime
        """
        self._import_date = import_date

    @property
    def origin_url(self):
        """
        Gets the origin_url of this ArtifactRest.


        :return: The origin_url of this ArtifactRest.
        :rtype: str
        """
        return self._origin_url

    @origin_url.setter
    def origin_url(self, origin_url):
        """
        Sets the origin_url of this ArtifactRest.


        :param origin_url: The origin_url of this ArtifactRest.
        :type: str
        """
        self._origin_url = origin_url

    @property
    def status(self):
        """
        Gets the status of this ArtifactRest.


        :return: The status of this ArtifactRest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ArtifactRest.


        :param status: The status of this ArtifactRest.
        :type: str
        """
        self._status = status

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
	    elif isinstance(value, datetime):
		result[attr] = str(value.date())
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
