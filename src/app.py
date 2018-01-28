from flask import Flask
from apis.urls import all_urls
import os


application = Flask(os.environ.get("APPLICATION_NAME"))
SETTINGS_FILE = os.environ.get("SETTINGS_FILE", "settings.local_settings")

application.config.from_object(SETTINGS_FILE)

for url, method, _ in all_urls:
    application.add_url_rule(url, view_func=method)