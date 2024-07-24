#!/usr/bin/env python3.11

import json
import os

class UpdateSettings:
    def __init__(self, config_file='config/update_settings.json'):
        self.config_file = config_file

        self.auto_check_options = ["Daily", "Weekly", "Now"]

        self.load_settings()

    def load_settings(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                config = json.load(file)
            self.auto_check = config.get('auto_check', self.auto_check_options[0])
        else:
            self.reset_settings()

    def save_settings(self):
        config = {
            'auto_check': self.auto_check,
        }
        with open(self.config_file, 'w') as file:
            json.dump(config, file)

    def reset_settings(self):
        self.auto_check = self.auto_check_options[0]
        self.save_settings()

    def set_auto_check(self, index):
        self.auto_check = self.auto_check_options[index]

