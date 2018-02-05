"""
Scripts module for running the scripts as flask
management commands. A sample example is shown
in this file.
"""

from .tests import test_cli_command

ALL_CLI_COMMANDS = {
    "test_command": test_cli_command
}
