'''Steam desktop files manipulation'''
from xdg.DesktopEntry import DesktopEntry
from .xdg import xdg_desktop_files, SteamDesktopEntry


def steam_desktop_files():
    '''Yields Steam-enabled .desktop files in the XDG data applications paths.'''
    for filepath in xdg_desktop_files():
        entry = DesktopEntry(filepath)
        if entry.getExec().startswith('steam'):
            yield filepath


def categorize_steam_applications():
    '''Ensures Steam-enabled .desktop files have the `Steam` category.'''
    for filepath in steam_desktop_files():
        entry = SteamDesktopEntry(filepath)
        if 'Steam' not in entry.getCategories():
            entry.setCategories(entry.getCategories() + ['Steam'])
            entry.write()
