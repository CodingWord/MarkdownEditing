"""
    This file contains some "distraction free" mode improvements. However they can be
    used in normal mode, too. These features can be enabled/disabled via settings files.
    In order to target "distraction free" mode, FullScreenStatus plugin must be installed:
    https://github.com/maliayas/SublimeText_FullScreenStatus
"""

import sublime
import sublime_plugin
try:
    from MarkdownEditing.mdeutils import *
except ImportError:
    from mdeutils import *


def on_distraction_free():
    return sublime.active_window().settings().get('fss_on_distraction_free')


class KeepCurrentLineCentered(sublime_plugin.EventListener):

    def on_modified_async(self, view):
        # One of the MarkdownEditing syntax files must be in use.
        if not view_is_markdown(view):
            return False

        if on_distraction_free():
            if not view.settings().get('mde.distraction_free_mode', {}) \
                                  .get('mde.keep_centered', True):
                return False
        elif not view.settings().get('mde.keep_centered', False):
            return False

        view.show_at_center(view.sel()[0].begin())
