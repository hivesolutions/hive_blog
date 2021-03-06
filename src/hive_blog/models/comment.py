#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Solutions Blog
# Copyright (c) 2008-2020 Hive Solutions Lda.
#
# This file is part of Hive Solutions Blog.
#
# Hive Solutions Blog is confidential and property of Hive Solutions Lda.,
# its usage is constrained by the terms of the Hive Solutions
# Confidential Usage License.
#
# Hive Solutions Blog should not be distributed under any circumstances,
# violation of this may imply legal action.
#
# If you have any questions regarding the terms of this license please
# refer to <http://www.hive.pt/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt> & Tiago Silva <tsilva@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2020 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Hive Solutions Confidential Usage License (HSCUL)"
""" The license for the module """

import datetime

import colony

from .root_entity import RootEntity

MONTH_NUMBER_MAP = {
    1 : "Jan",
    2 : "Feb",
    3 : "Mar",
    4 : "Apr",
    5 : "May",
    6 : "Jun",
    7 : "Jul",
    8: "Aug",
    9 : "Sep",
    10 : "Oct",
    11 : "Nov",
    12 : "Dec"
}
""" The map relating the month number with the "mini" month name """

models = colony.__import__("models")
mvc_utils = colony.__import__("mvc_utils")

class Comment(RootEntity):
    """
    The comment class, representing the comment entity.
    """

    date = dict(
        type = "date",
        mandatory = True,
        secure = True
    )
    """ The date of the comment """

    contents = dict(
        type = "text",
        mandatory = True
    )
    """ The contents of the comment """

    author = dict(
        type = "relation",
        fetch_type = "lazy",
        mandatory = True,
        persist_type = mvc_utils.PERSIST_SAVE | mvc_utils.PERSIST_ASSOCIATE
    )
    """ The author of the comment """

    post = dict(
        type = "relation",
        fetch_type = "lazy",
        mandatory = True,
        persist_type = mvc_utils.PERSIST_ASSOCIATE
    )
    """ The post that contains the comment """

    in_reply_to = dict(
        type = "relation",
        fetch_type = "lazy",
        secure = True,
        persist_type = mvc_utils.PERSIST_ASSOCIATE
    )
    """ The comment for which this comment is a reply
    this is not required for the top level comments """

    replies = dict(
        type = "relation",
        fetch_type = "lazy",
        secure = True,
        persist_type = mvc_utils.PERSIST_NONE
    )
    """ The comment replies to the comment """

    def __init__(self):
        """
        Constructor of the class.
        """

        RootEntity.__init__(self)
        self.date = datetime.datetime.utcnow()

    @staticmethod
    def _relation_author():
        return dict(
            type = "to-one",
            target = models.User,
            reverse = "comments",
            is_mapper = True
        )

    @staticmethod
    def _relation_post():
        return dict(
            type = "to-one",
            target = models.Post,
            reverse = "posts",
            is_mapper = True
        )

    @staticmethod
    def _relation_in_reply_to():
        return dict(
            type = "to-one",
            target = models.Comment,
            reverse = "replies",
            is_mapper = True
        )

    @staticmethod
    def _relation_replies():
        return dict(
            type = "to-many",
            target = models.Comment,
            reverse = "in_reply_to"
        )

    def set_validation(self):
        """
        Sets the validation structures for the current structure.
        """

        # adds the inherited validations
        RootEntity.set_validation(self)

        # adds the validation methods to the date attribute
        self.add_validation("date", "not_none", True)

        # adds the validation methods to the contents attribute
        self.add_validation("contents", "not_none", True)
        self.add_validation("contents", "not_empty")

    def get_day(self):
        """
        Retrieves the day when the comment was made.

        :rtype: int
        :return: The day when the comment was made.
        """

        # in case there is no date set, must return
        # an invalid value indicating the problem
        if not self.date: return None

        # returns the date day
        return self.date.day

    def get_month(self):
        """
        Retrieves the month when the comment was made
        (represented in abbreviated text, eg: "January"
        is represented as "Jan").

        :rtype: String
        :return: The month when the comment was made.
        """

        # in case there is no date set, must return
        # an invalid value indicating the problem
        if not self.date: return None

        # returns the data month abbreviated
        return MONTH_NUMBER_MAP[self.date.month]
