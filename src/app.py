from flask import Flask
from apis.urls import all_urls
import os
import logging.config


application = Flask(os.environ.get("APPLICATION_NAME"))
SETTINGS_FILE = os.environ.get("SETTINGS_FILE", "settings.local_settings")

application.config.from_object(SETTINGS_FILE)

# Adding all the url rules in the api application
for url, view, methods, _ in all_urls:
    application.add_url_rule(url, view_func=view, methods=methods)


logging.config.dictConfig(application.config["LOGGING"])
