#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Solutions Blog
# Copyright (C) 2010 Hive Solutions Lda.
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

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision: 421 $"
""" The revision number of the module """

__date__ = "$LastChangedDate: 2008-11-20 15:16:53 +0000 (Qui, 20 Nov 2008) $"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2010 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Hive Solutions Confidential Usage License (HSCUL)"
""" The license for the module """

import colony.base.plugin_system
import colony.base.decorators

class HiveBlogMainPlugin(colony.base.plugin_system.Plugin):
    """
    The main class for the Hive Blog Main plugin.
    """

    id = "pt.hive.hive_blog.plugins.main"
    name = "Hive Blog Main Plugin"
    short_name = "Hive Blog Main"
    description = "The plugin that offers the hive blog"
    version = "1.0.0"
    author = "Hive Solutions Lda. <development@hive.pt>"
    loading_type = colony.base.plugin_system.EAGER_LOADING_TYPE
    platforms = [
        colony.base.plugin_system.CPYTHON_ENVIRONMENT
    ]
    attributes = {
        "build_automation_file_path" : "$base{plugin_directory}/hive_blog_main/main/resources/baf.xml"
    }
    capabilities = [
        "web.mvc_service",
        "build_automation_item"
    ]
    dependencies = [
        colony.base.plugin_system.PluginDependency("pt.hive.colony.plugins.web.mvc.utils", "1.x.x"),
        colony.base.plugin_system.PluginDependency("pt.hive.colony.plugins.security.captcha", "1.x.x"),
        colony.base.plugin_system.PluginDependency("pt.hive.colony.plugins.service.openid", "1.x.x"),
        colony.base.plugin_system.PluginDependency("pt.hive.colony.plugins.service.twitter", "1.x.x"),
        colony.base.plugin_system.PluginDependency("pt.hive.colony.plugins.service.facebook", "1.x.x")
    ]
    main_modules = [
        "hive_blog_main.main.hive_blog_main_exceptions",
        "hive_blog_main.main.hive_blog_main_system"
    ]

    hive_blog_main = None
    """ The hive blog main """

    web_mvc_utils_plugin = None
    """ The web mvc utils plugin """

    security_captcha_plugin = None
    """ The security captch plugin """

    service_openid_plugin = None
    """ The service openid plugin """

    service_twitter_plugin = None
    """ The service twitter plugin """

    service_facebook_plugin = None
    """ The service facebook plugin """

    def load_plugin(self):
        colony.base.plugin_system.Plugin.load_plugin(self)
        import hive_blog_main.main.hive_blog_main_system
        self.hive_blog_main = hive_blog_main.main.hive_blog_main_system.HiveBlogMain(self)

    def end_load_plugin(self):
        colony.base.plugin_system.Plugin.end_load_plugin(self)
        self.hive_blog_main.load_components()

    def unload_plugin(self):
        colony.base.plugin_system.Plugin.unload_plugin(self)
        self.hive_blog_main.unload_components()

    def end_unload_plugin(self):
        colony.base.plugin_system.Plugin.end_unload_plugin(self)

    def load_allowed(self, plugin, capability):
        colony.base.plugin_system.Plugin.load_allowed(self, plugin, capability)

    def unload_allowed(self, plugin, capability):
        colony.base.plugin_system.Plugin.unload_allowed(self, plugin, capability)

    @colony.base.decorators.inject_dependencies
    def dependency_injected(self, plugin):
        colony.base.plugin_system.Plugin.dependency_injected(self, plugin)

    def get_patterns(self):
        """
        Retrieves the tuple of regular expressions to be used as patterns,
        to the web mvc service. The tuple should relate the route with the handler
        method/function.

        @rtype: Tuple
        @return: The tuple of regular expressions to be used as patterns,
        to the web mvc service.
        """

        return self.hive_blog_main.get_patterns()

    def get_communication_patterns(self):
        """
        Retrieves the tuple of regular expressions to be used as communication patterns,
        to the web mvc service. The tuple should relate the route with a tuple
        containing the data handler, the connection changed handler and the name
        of the connection.

        @rtype: Tuple
        @return: The tuple of regular expressions to be used as communication patterns,
        to the web mvc service.
        """

        return self.hive_blog_main.get_communication_patterns()

    def get_resource_patterns(self):
        """
        Retrieves the tuple of regular expressions to be used as resource patterns,
        to the web mvc service. The tuple should relate the route with the base
        file system path to be used.

        @rtype: Tuple
        @return: The tuple of regular expressions to be used as resource patterns,
        to the web mvc service.
        """

        return self.hive_blog_main.get_resource_patterns()

    def get_web_mvc_utils_plugin(self):
        return self.web_mvc_utils_plugin

    @colony.base.decorators.plugin_inject("pt.hive.colony.plugins.web.mvc.utils")
    def set_web_mvc_utils_plugin(self, web_mvc_utils_plugin):
        self.web_mvc_utils_plugin = web_mvc_utils_plugin

    def get_security_captcha_plugin(self):
        return self.security_captcha_plugin

    @colony.base.decorators.plugin_inject("pt.hive.colony.plugins.security.captcha")
    def set_security_captcha_plugin(self, security_captcha_plugin):
        self.security_captcha_plugin = security_captcha_plugin

    def get_service_openid_plugin(self):
        return self.service_openid_plugin

    @colony.base.decorators.plugin_inject("pt.hive.colony.plugins.service.openid")
    def set_service_openid_plugin(self, service_openid_plugin):
        self.service_openid_plugin = service_openid_plugin

    def get_service_twitter_plugin(self):
        return self.service_twitter_plugin

    @colony.base.decorators.plugin_inject("pt.hive.colony.plugins.service.twitter")
    def set_service_twitter_plugin(self, service_twitter_plugin):
        self.service_twitter_plugin = service_twitter_plugin

    def get_service_facebook_plugin(self):
        return self.service_facebook_plugin

    @colony.base.decorators.plugin_inject("pt.hive.colony.plugins.service.facebook")
    def set_service_facebook_plugin(self, service_facebook_plugin):
        self.service_facebook_plugin = service_facebook_plugin
