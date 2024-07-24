#!/usr/bin/env python3.11

import gi
import logging
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from update_logic import UpdateSettings

logging.basicConfig(level=logging.INFO)

class UpdateSettingsWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Update Station")
        self.set_border_width(10)
        self.set_default_size(400, 200)

        self.settings = UpdateSettings()

        grid = Gtk.Grid()
        grid.set_row_spacing(10)
        grid.set_column_spacing(10)
        grid.set_column_homogeneous(True)
        self.add(grid)

        # System updates label
        system_label = Gtk.Label(label="System updates are checked routinely and installed automatically.")
        system_label.set_halign(Gtk.Align.START)
        grid.attach(system_label, 0, 0, 2, 1)

        # Security maintenance label
        security_label = Gtk.Label(label="For other packages, this system has: Basic Security Maintenance")
        security_label.set_halign(Gtk.Align.START)
        grid.attach(security_label, 0, 1, 2, 1)

        # Automatically check for updates
        self.create_combo(grid, "Automatically check for updates:", self.settings.auto_check_options, self.settings.auto_check, self.on_auto_check_combo_changed, 2)

        # Revert and Close buttons
        button_box = Gtk.Box(spacing=10)
        button_box.set_halign(Gtk.Align.END)
        grid.attach(button_box, 0, 3, 2, 1)

        self.revert_button = Gtk.Button(label="Revert")
        self.revert_button.connect("clicked", self.on_revert_clicked)
        button_box.pack_start(self.revert_button, False, False, 0)

        self.close_button = Gtk.Button(label="Close")
        self.close_button.connect("clicked", self.on_close_clicked)
        button_box.pack_start(self.close_button, False, False, 0)

    def create_combo(self, grid, label_text, options, active_option, callback, row):
        label = Gtk.Label(label=label_text)
        label.set_halign(Gtk.Align.START)
        grid.attach(label, 0, row, 1, 1)

        combo = Gtk.ComboBoxText()
        for option in options:
            combo.append_text(option)
        combo.set_active(options.index(active_option))
        combo.set_tooltip_text(label_text)
        combo.connect("changed", callback)
        grid.attach(combo, 1, row, 1, 1)

    def on_auto_check_combo_changed(self, combo):
        self.settings.set_auto_check(combo.get_active())
        logging.info(f"Auto check: {self.settings.auto_check}")

    def on_revert_clicked(self, widget):
        self.settings.reset_settings()
        self.update_ui()
        logging.info("Settings reverted to default")

    def update_ui(self):
        self.auto_check_combo.set_active(self.settings.auto_check_options.index(self.settings.auto_check))

    def on_close_clicked(self, widget):
        self.settings.save_settings()
        Gtk.main_quit()

win = UpdateSettingsWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

