import os
import sys


def frozen_project():
    """Return whether the project is frozen"""
    return hasattr(sys, "frozen")


def get_gui_path():
    """Get Django project directory"""
    if frozen_project():
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(__file__)