"""
Scripts module for running the scripts as flask
management commands. A sample example is shown
in this file.

Write your scripts in this folder and import as shown
below for the test scripts. Support for command line parameters
is needed. Add the imported new command in the ALL_CLI_COMMANDS
parameter.

For example:

If you create a management cli command name createuser in the file
user.py in scripts folder, the command can be run using flask createuser

scripts/user.py
--------------------------------
import click

@click.command
def createuser():
    # Create user code
    print("Creating the user")
    
    
scripts/__init__.py
---------------------------------
from .user import createuser

ALL_CLI_COMMANDS = {
    "createuser": createuser
}
"""

from .tests import test_cli_command

ALL_CLI_COMMANDS = {
    "test_command": test_cli_command
}
