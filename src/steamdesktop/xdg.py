'''XDG extended support.'''
import os.path
from glob import iglob

from xdg.BaseDirectory import load_data_paths
from xdg.DesktopEntry import DesktopEntry


def xdg_desktop_files():
    '''Yields .desktop files in the XDG data applications paths.'''
    for directory in load_data_paths('applications'):
        desktop_glob = os.path.join(directory, '**/*.desktop')
        for filepath in iglob(desktop_glob, recursive=True):
            yield filepath


class SteamDesktopEntry(DesktopEntry):
    def setCategories(self, categories):
        self.set('Categories', ';'.join(categories))
