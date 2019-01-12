"""
This module contains various constants, mainly those from flatpak-builder's
manifest files (see `man flatpak-manifest` for more information).
"""

#: The branch of the application, defaults to master.
MANIFEST_BRANCH = 'branch'

#: The default value of :data:`MANIFEST_BRANCH`.
MANIFEST_BRANCH_DEFAULT = 'master'

#: A string defining the application id.
MANIFEST_ID = 'id'

#: A string defining the application id.
MANIFEST_APP_ID = 'app-id'

#: An array of objects specifying the modules to be built in order.
MANIFEST_MODULES = 'modules'

#: The name of the module, used in e.g. build logs.
MODULE_NAME = 'name'

#: An array of objects defining sources that will be downloaded and extracted.
MODULE_SOURCES = 'sources'

#: An array of commands to run during build (between make and make install
#: if those are used).
MODULE_BUILD_COMMANDS = 'build-commands'

#: An array of shell commands that are run after the install phase.
MODULE_POST_INSTALL = 'post-install'

#: The name of a custom module for initialization.
INIT_MODULE_NAME = 'init'

#: The name of a custom module for initialization.
FINISH_MODULE_NAME = 'finish'
