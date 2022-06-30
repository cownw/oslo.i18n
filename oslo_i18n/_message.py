"""Primary Message class for lazy translation support.
"""

import copy
import gettext
import locale
import logging
import os
import warnings

from oslo_i18n import _locale
from oslo_i18n import _translate

CONTEXT_SEPARATOR = "\x04"

LOG = logging.getLogger(__name__)

class Message(str):
    """A Message object is a unicode object that can be translated.

    Translation of Message is done explicitly using the translate() method.
    For all non-translation intents and purposes, a Message is simply unicode,
    and can be treated as such.
    """

    def __new__(cls, msgid, msgtext=None, params=None,
                domain='oslo', has_contextual_form=False,
                has_plural_form=False, *args):
                