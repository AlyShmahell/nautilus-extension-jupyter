from gi import require_version
require_version('Gtk', '3.0')
require_version('Nautilus', '3.0')
from gi.repository import Nautilus, GObject
from subprocess import call
import os

class nautilusExtensionJupyter(GObject.GObject, Nautilus.MenuProvider):

    def launch_jupyter(self, _, files):
        filepath = ''
        for file in files:
            filepath += '"' + file.get_location().get_path() + '" '
        call('jupyter notebook ' + filepath + '&', shell=True)

    def get_file_items(self, _, files):
        item = Nautilus.MenuItem(
            name='OpenFileWithJupyter',
            label='Open with Jupyter',
            tip='Opens the selected files with Jupyter'
        )
        item.connect('activate', self.launch_jupyter, files)
        return [item]

    def get_background_items(self, _, files):
        item = Nautilus.MenuItem(
            name='LaunchJupyterInDirectory',
            label='Launch Jupyter Here',
            tip='Launches Jupyter in the current directory'
        )
        item.connect('activate', self.launch_jupyter, [files])
        return [item]

