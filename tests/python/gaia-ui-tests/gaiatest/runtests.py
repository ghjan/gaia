# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import cgi
import datetime
import json
import math
import os
import pkg_resources
import sys
import textwrap
import time
import base64

from py.xml import html
from py.xml import raw
from marionette import BaseMarionetteOptions, HTMLReportingOptionsMixin, HTMLReportingTestRunnerMixin, \
                       EnduranceOptionsMixin, HTMLReportingTestResult
from marionette import MarionetteTestResult
from marionette import MarionetteTextTestRunner
from marionette import BaseMarionetteTestRunner
from marionette.runtests import cli
from moztest.results import TestResult, relevant_line

from gaiatest import __name__
from gaiatest import GaiaTestCase, GaiaOptionsMixin, GaiaTestRunnerMixin
from version import __version__


class GaiaTestOptions(BaseMarionetteOptions, GaiaOptionsMixin, EnduranceOptionsMixin, HTMLReportingOptionsMixin):
    def __init__(self, **kwargs):
        BaseMarionetteOptions.__init__(self, **kwargs)
        GaiaOptionsMixin.__init__(self, **kwargs)
        HTMLReportingOptionsMixin.__init__(self, **kwargs)
        EnduranceOptionsMixin.__init__(self, **kwargs)

class GaiaTextTestRunner(MarionetteTextTestRunner):

    resultclass = HTMLReportingTestResult 


class GaiaTestRunner(BaseMarionetteTestRunner, GaiaTestRunnerMixin, HTMLReportingTestRunnerMixin):

    textrunnerclass = GaiaTextTestRunner

    def __init__(self, **kwargs):
        BaseMarionetteTestRunner.__init__(self, **kwargs)
        GaiaTestRunnerMixin.__init__(self, **kwargs)
        HTMLReportingTestRunnerMixin.__init__(self, name=__name__, version=__version__, **kwargs)
        self.test_handlers = [GaiaTestCase]

def main():
    cli(runner_class=GaiaTestRunner, parser_class=GaiaTestOptions)
