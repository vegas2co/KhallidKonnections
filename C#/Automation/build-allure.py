import os
import json

from os import path

cwd = os.getcwd()

allure_content = {}
allure_content['allure'] = {
    'directory':'{}\\allure-results'.format(cwd),
    'links':[]
}

allure_path = "{}\\allure\\allureConfig.json".format(cwd)

if not path.exists(allure_path):
    with open(allure_path, "w") as allure_config:
        json.dump(allure_content, allure_config)

