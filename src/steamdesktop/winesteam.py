'''Steam desktop files manipulation'''
from xdg.DesktopEntry import DesktopEntry
from .xdg import xdg_desktop_files, SteamDesktopEntry


def winesteam_desktop_files():
    '''Yields Steam-enabled .desktop files in the XDG data applications paths.'''
    for filepath in xdg_desktop_files():
        entry_exec_parts = DesktopEntry(filepath).getExec().split(' ')
        if 'wine' in entry_exec_parts and entry_exec_parts[-1].startswith('steam://rungameid/'):
            yield filepath


def categorize_winesteam_applications():
    '''Ensures Steam-enabled .desktop files have the `Steam` category.'''
    for filepath in winesteam_desktop_files():
        entry = SteamDesktopEntry(filepath)
        if 'Steam' not in entry.getCategories():
            entry.setCategories(entry.getCategories() + ['WineSteam'])
            entry.write()
