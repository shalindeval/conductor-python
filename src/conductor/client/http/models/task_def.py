import pprint
import re  # noqa: F401

import six

class TaskDef(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'owner_app': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'created_by': 'str',
        'updated_by': 'str',
        'name': 'str',
        'description': 'str',
        'retry_count': 'int',
        'timeout_seconds': 'int',
        'input_keys': 'list[str]',
        'output_keys': 'list[str]',
        'timeout_policy': 'str',
        'retry_logic': 'str',
        'retry_delay_seconds': 'int',
        'response_timeout_seconds': 'int',
        'concurrent_exec_limit': 'int',
        'input_template': 'dict(str, object)',
        'rate_limit_per_frequency': 'int',
        'rate_limit_frequency_in_seconds': 'int',
        'isolation_group_id': 'str',
        'execution_name_space': 'str',
        'owner_email': 'str',
        'poll_timeout_seconds': 'int',
        'backoff_scale_factor': 'int'
    }

    attribute_map = {
        'owner_app': 'ownerApp',
        'create_time': 'createTime',
        'update_time': 'updateTime',
        'created_by': 'createdBy',
        'updated_by': 'updatedBy',
        'name': 'name',
        'description': 'description',
        'retry_count': 'retryCount',
        'timeout_seconds': 'timeoutSeconds',
        'input_keys': 'inputKeys',
        'output_keys': 'outputKeys',
        'timeout_policy': 'timeoutPolicy',
        'retry_logic': 'retryLogic',
        'retry_delay_seconds': 'retryDelaySeconds',
        'response_timeout_seconds': 'responseTimeoutSeconds',
        'concurrent_exec_limit': 'concurrentExecLimit',
        'input_template': 'inputTemplate',
        'rate_limit_per_frequency': 'rateLimitPerFrequency',
        'rate_limit_frequency_in_seconds': 'rateLimitFrequencyInSeconds',
        'isolation_group_id': 'isolationGroupId',
        'execution_name_space': 'executionNameSpace',
        'owner_email': 'ownerEmail',
        'poll_timeout_seconds': 'pollTimeoutSeconds',
        'backoff_scale_factor': 'backoffScaleFactor'
    }

    def __init__(self, owner_app=None, create_time=None, update_time=None, created_by=None, updated_by=None, name=None, description=None, retry_count=None, timeout_seconds=None, input_keys=None, output_keys=None, timeout_policy=None, retry_logic=None, retry_delay_seconds=None, response_timeout_seconds=None, concurrent_exec_limit=None, input_template=None, rate_limit_per_frequency=None, rate_limit_frequency_in_seconds=None, isolation_group_id=None, execution_name_space=None, owner_email=None, poll_timeout_seconds=None, backoff_scale_factor=None):  # noqa: E501
        """TaskDef - a model defined in Swagger"""  # noqa: E501
        self._owner_app = None
        self._create_time = None
        self._update_time = None
        self._created_by = None
        self._updated_by = None
        self._name = None
        self._description = None
        self._retry_count = None
        self._timeout_seconds = None
        self._input_keys = None
        self._output_keys = None
        self._timeout_policy = None
        self._retry_logic = None
        self._retry_delay_seconds = None
        self._response_timeout_seconds = None
        self._concurrent_exec_limit = None
        self._input_template = None
        self._rate_limit_per_frequency = None
        self._rate_limit_frequency_in_seconds = None
        self._isolation_group_id = None
        self._execution_name_space = None
        self._owner_email = None
        self._poll_timeout_seconds = None
        self._backoff_scale_factor = None
        self.discriminator = None
        if owner_app is not None:
            self.owner_app = owner_app
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if created_by is not None:
            self.created_by = created_by
        if updated_by is not None:
            self.updated_by = updated_by
        self.name = name
        if description is not None:
            self.description = description
        if retry_count is not None:
            self.retry_count = retry_count
        self.timeout_seconds = timeout_seconds
        if input_keys is not None:
            self.input_keys = input_keys
        if output_keys is not None:
            self.output_keys = output_keys
        if timeout_policy is not None:
            self.timeout_policy = timeout_policy
        if retry_logic is not None:
            self.retry_logic = retry_logic
        if retry_delay_seconds is not None:
            self.retry_delay_seconds = retry_delay_seconds
        if response_timeout_seconds is not None:
            self.response_timeout_seconds = response_timeout_seconds
        if concurrent_exec_limit is not None:
            self.concurrent_exec_limit = concurrent_exec_limit
        if input_template is not None:
            self.input_template = input_template
        if rate_limit_per_frequency is not None:
            self.rate_limit_per_frequency = rate_limit_per_frequency
        if rate_limit_frequency_in_seconds is not None:
            self.rate_limit_frequency_in_seconds = rate_limit_frequency_in_seconds
        if isolation_group_id is not None:
            self.isolation_group_id = isolation_group_id
        if execution_name_space is not None:
            self.execution_name_space = execution_name_space
        if owner_email is not None:
            self.owner_email = owner_email
        if poll_timeout_seconds is not None:
            self.poll_timeout_seconds = poll_timeout_seconds
        if backoff_scale_factor is not None:
            self.backoff_scale_factor = backoff_scale_factor

    @property
    def owner_app(self):
        """Gets the owner_app of this TaskDef.  # noqa: E501


        :return: The owner_app of this TaskDef.  # noqa: E501
        :rtype: str
        """
        return self._owner_app

    @owner_app.setter
    def owner_app(self, owner_app):
        """Sets the owner_app of this TaskDef.


        :param owner_app: The owner_app of this TaskDef.  # noqa: E501
        :type: str
        """

        self._owner_app = owner_app

    @property
    def create_time(self):
        """Gets the create_time of this TaskDef.  # noqa: E501


        :return: The create_time of this TaskDef.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TaskDef.


        :param create_time: The create_time of this TaskDef.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this TaskDef.  # noqa: E501


        :return: The update_time of this TaskDef.  # noqa: E501
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this TaskDef.


        :param update_time: The update_time of this TaskDef.  # noqa: E501
        :type: int
        """

        self._update_time = update_time

    @property
    def created_by(self):
        """Gets the created_by of this TaskDef.  # noqa: E501


        :return: The created_by of this TaskDef.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this TaskDef.


        :param created_by: The created_by of this TaskDef.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def updated_by(self):
        """Gets the updated_by of this TaskDef.  # noqa: E501


        :return: The updated_by of this TaskDef.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this TaskDef.


        :param updated_by: The updated_by of this TaskDef.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def name(self):
        """Gets the name of this TaskDef.  # noqa: E501


        :return: The name of this TaskDef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskDef.


        :param name: The name of this TaskDef.  # noqa: E501
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this TaskDef.  # noqa: E501


        :return: The description of this TaskDef.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskDef.


        :param description: The description of this TaskDef.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def retry_count(self):
        """Gets the retry_count of this TaskDef.  # noqa: E501


        :return: The retry_count of this TaskDef.  # noqa: E501
        :rtype: int
        """
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        """Sets the retry_count of this TaskDef.


        :param retry_count: The retry_count of this TaskDef.  # noqa: E501
        :type: int
        """

        self._retry_count = retry_count

    @property
    def timeout_seconds(self):
        """Gets the timeout_seconds of this TaskDef.  # noqa: E501


        :return: The timeout_seconds of this TaskDef.  # noqa: E501
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """Sets the timeout_seconds of this TaskDef.


        :param timeout_seconds: The timeout_seconds of this TaskDef.  # noqa: E501
        :type: int
        """
        self._timeout_seconds = timeout_seconds

    @property
    def input_keys(self):
        """Gets the input_keys of this TaskDef.  # noqa: E501


        :return: The input_keys of this TaskDef.  # noqa: E501
        :rtype: list[str]
        """
        return self._input_keys

    @input_keys.setter
    def input_keys(self, input_keys):
        """Sets the input_keys of this TaskDef.


        :param input_keys: The input_keys of this TaskDef.  # noqa: E501
        :type: list[str]
        """

        self._input_keys = input_keys

    @property
    def output_keys(self):
        """Gets the output_keys of this TaskDef.  # noqa: E501


        :return: The output_keys of this TaskDef.  # noqa: E501
        :rtype: list[str]
        """
        return self._output_keys

    @output_keys.setter
    def output_keys(self, output_keys):
        """Sets the output_keys of this TaskDef.


        :param output_keys: The output_keys of this TaskDef.  # noqa: E501
        :type: list[str]
        """

        self._output_keys = output_keys

    @property
    def timeout_policy(self):
        """Gets the timeout_policy of this TaskDef.  # noqa: E501


        :return: The timeout_policy of this TaskDef.  # noqa: E501
        :rtype: str
        """
        return self._timeout_policy

    @timeout_policy.setter
    def timeout_policy(self, timeout_policy):
        """Sets the timeout_policy of this TaskDef.


        :param timeout_policy: The timeout_policy of this TaskDef.  # noqa: E501
        :type: str
        """
        allowed_values = ["RETRY", "TIME_OUT_WF", "ALERT_ONLY"]  # noqa: E501
        if timeout_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `timeout_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(timeout_policy, allowed_values)
            )

        self._timeout_policy = timeout_policy

    @property
    def retry_logic(self):
        """Gets the retry_logic of this TaskDef.  # noqa: E501


        :return: The retry_logic of this TaskDef.  # noqa: E501
        :rtype: str
        """
        return self._retry_logic

    @retry_logic.setter
    def retry_logic(self, retry_logic):
        """Sets the retry_logic of this TaskDef.


        :param retry_logic: The retry_logic of this TaskDef.  # noqa: E501
        :type: str
        """
        allowed_values = ["FIXED", "EXPONENTIAL_BACKOFF", "LINEAR_BACKOFF"]  # noqa: E501
        if retry_logic not in allowed_values:
            raise ValueError(
                "Invalid value for `retry_logic` ({0}), must be one of {1}"  # noqa: E501
                .format(retry_logic, allowed_values)
            )

        self._retry_logic = retry_logic

    @property
    def retry_delay_seconds(self):
        """Gets the retry_delay_seconds of this TaskDef.  # noqa: E501


        :return: The retry_delay_seconds of this TaskDef.  # noqa: E501
        :rtype: int
        """
        return self._retry_delay_seconds

    @retry_delay_seconds.setter
    def retry_delay_seconds(self, retry_delay_seconds):
        """Sets the retry_delay_seconds of this TaskDef.


        :param retry_delay_seconds: The retry_delay_seconds of this TaskDef.  # noqa: E501
        :type: int
        """

        self._retry_delay_seconds = retry_delay_seconds

    @property
    def response_timeout_seconds(self):
        """Gets the response_timeout_seconds of this TaskDef.  # noqa: E501


        :return: The response_timeout_seconds of this TaskDef.  # noqa: E501
        :rtype: int
        """
        return self._response_timeout_seconds

    @response_timeout_seconds.setter
    def response_timeout_seconds(self, response_timeout_seconds):
        """Sets the response_timeout_seconds of this TaskDef.


        :param response_timeout_seconds: The response_timeout_seconds of this TaskDef.  # noqa: E501
        :type: int
        """

        self._response_timeout_seconds = response_timeout_seconds

    @property
    def concurrent_exec_limit(self):
        """Gets the concurrent_exec_limit of this TaskDef.  # noqa: E501


        :return: The concurrent_exec_limit of this TaskDef.  # noqa: E501
        :rtype: int
        """
        return self._concurrent_exec_limit

    @concurrent_exec_limit.setter
    def concurrent_exec_limit(self, concurrent_exec_limit):
        """Sets the concurrent_exec_limit of this TaskDef.


        :param concurrent_exec_limit: The concurrent_exec_limit of this TaskDef.  # noqa: E501
        :type: int
        """

        self._concurrent_exec_limit = concurrent_exec_limit

    @property
    def input_template(self):
        """Gets the input_template of this TaskDef.  # noqa: E501


        :return: The input_template of this TaskDef.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._input_template

    @input_template.setter
    def input_template(self, input_template):
        """Sets the input_template of this TaskDef.


        :param input_template: The input_template of this TaskDef.  # noqa: E501
        :type: dict(str, object)
        """

        self._input_template = input_template

    @property
    def rate_limit_per_frequency(self):
        """Gets the rate_limit_per_frequency of this TaskDef.  # noqa: E501


        :return: The rate_limit_per_frequency of this TaskDef.  # noqa: E501
        :rtype: int
        """
        return self._rate_limit_per_frequency

    @rate_limit_per_frequency.setter
    def rate_limit_per_frequency(self, rate_limit_per_frequency):
        """Sets the rate_limit_per_frequency of this TaskDef.


        :param rate_limit_per_frequency: The rate_limit_per_frequency of this TaskDef.  # noqa: E501
        :type: int
        """

        self._rate_limit_per_frequency = rate_limit_per_frequency

    @property
    def rate_limit_frequency_in_seconds(self):
        """Gets the rate_limit_frequency_in_seconds of this TaskDef.  # noqa: E501


        :return: The rate_limit_frequency_in_seconds of this TaskDef.  # noqa: E501
        :rtype: int
        """
        return self._rate_limit_frequency_in_seconds

    @rate_limit_frequency_in_seconds.setter
    def rate_limit_frequency_in_seconds(self, rate_limit_frequency_in_seconds):
        """Sets the rate_limit_frequency_in_seconds of this TaskDef.


        :param rate_limit_frequency_in_seconds: The rate_limit_frequency_in_seconds of this TaskDef.  # noqa: E501
        :type: int
        """

        self._rate_limit_frequency_in_seconds = rate_limit_frequency_in_seconds

    @property
    def isolation_group_id(self):
        """Gets the isolation_group_id of this TaskDef.  # noqa: E501


        :return: The isolation_group_id of this TaskDef.  # noqa: E501
        :rtype: str
        """
        return self._isolation_group_id

    @isolation_group_id.setter
    def isolation_group_id(self, isolation_group_id):
        """Sets the isolation_group_id of this TaskDef.


        :param isolation_group_id: The isolation_group_id of this TaskDef.  # noqa: E501
        :type: str
        """

        self._isolation_group_id = isolation_group_id

    @property
    def execution_name_space(self):
        """Gets the execution_name_space of this TaskDef.  # noqa: E501


        :return: The execution_name_space of this TaskDef.  # noqa: E501
        :rtype: str
        """
        return self._execution_name_space

    @execution_name_space.setter
    def execution_name_space(self, execution_name_space):
        """Sets the execution_name_space of this TaskDef.


        :param execution_name_space: The execution_name_space of this TaskDef.  # noqa: E501
        :type: str
        """

        self._execution_name_space = execution_name_space

    @property
    def owner_email(self):
        """Gets the owner_email of this TaskDef.  # noqa: E501


        :return: The owner_email of this TaskDef.  # noqa: E501
        :rtype: str
        """
        return self._owner_email

    @owner_email.setter
    def owner_email(self, owner_email):
        """Sets the owner_email of this TaskDef.


        :param owner_email: The owner_email of this TaskDef.  # noqa: E501
        :type: str
        """

        self._owner_email = owner_email

    @property
    def poll_timeout_seconds(self):
        """Gets the poll_timeout_seconds of this TaskDef.  # noqa: E501


        :return: The poll_timeout_seconds of this TaskDef.  # noqa: E501
        :rtype: int
        """
        return self._poll_timeout_seconds

    @poll_timeout_seconds.setter
    def poll_timeout_seconds(self, poll_timeout_seconds):
        """Sets the poll_timeout_seconds of this TaskDef.


        :param poll_timeout_seconds: The poll_timeout_seconds of this TaskDef.  # noqa: E501
        :type: int
        """

        self._poll_timeout_seconds = poll_timeout_seconds

    @property
    def backoff_scale_factor(self):
        """Gets the backoff_scale_factor of this TaskDef.  # noqa: E501


        :return: The backoff_scale_factor of this TaskDef.  # noqa: E501
        :rtype: int
        """
        return self._backoff_scale_factor

    @backoff_scale_factor.setter
    def backoff_scale_factor(self, backoff_scale_factor):
        """Sets the backoff_scale_factor of this TaskDef.


        :param backoff_scale_factor: The backoff_scale_factor of this TaskDef.  # noqa: E501
        :type: int
        """

        self._backoff_scale_factor = backoff_scale_factor

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(TaskDef, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TaskDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
