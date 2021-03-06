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

import hashlib

import colony

models = colony.__import__("models")
mvc_utils = colony.__import__("mvc_utils")

class RootEntity(models.EntityModel):
    """
    The base root entity from which all the other
    entity models inherit.
    """

    object_id = dict(
        id = True,
        type = "integer",
        generated = True
    )
    """ The object id of the root entity """

    tags = dict(
        type = "relation",
        fetch_type = "lazy",
        persist_type = mvc_utils.PERSIST_ASSOCIATE
    )
    """ The tags for the root entity, these values
    should identify the entity through description """

    def __init__(self):
        """
        Constructor of the class.
        """

        self.object_id = None

    @staticmethod
    def _relation_tags():
        return dict(
            type = "to-many",
            target = models.Tag,
            reverse = "root_entities"
        )

    def set_validation(self):
        """
        Sets the validation structures for the
        current structure.
        """

        pass

    @staticmethod
    def encrypt(data):
        """
        Encrypts the specified data in SHA512 and returns its
        hexadecimal digest.

        :rtype: String
        :return: The encrypted data digest in hexadecimal format.
        """

        # computes the SHA 512 hash of the data and
        # retrieves its digest in hexadecimal format
        encrypted_data = hashlib.sha512(data)
        encrypted_data_digest = encrypted_data.hexdigest()

        # returns the encrypted data digest
        return encrypted_data_digest
