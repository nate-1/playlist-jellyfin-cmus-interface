import os
import sys
from xml.etree import ElementTree

def isPlaylistUpdated(cmusPlaylistFile, jellyfinMusicPathArray) :
    cmusMusicPathArray = open(cmusPlaylistFile, 'r').read().splitlines()

    if len(cmusMusicPathArray) != len(jellyfinMusicPathArray) :
        return True

    length = len(cmusMusicPathArray)

    for i in range(0, length) : 
        if cmusMusicPathArray[i] != jellyfinMusicPathArray[i].text :
            return True

    return False
    


def updateFile(cmusPlaylistFile, musicPathArray) : 
    print('updating or creating ' + cmusPlaylistFile)
    string = ''
    for path in musicPathArray : 
        string += path.text + '\n'

    with open(cmusPlaylistFile, 'w') as sw :
        sw.write(string)


JELLYFIN_PLAYLIST_PATH = sys.argv[1]
CMUS_PLAYLIST_PATH = sys.argv[2]

for playlist in os.listdir(JELLYFIN_PLAYLIST_PATH) :

    playlistFile = os.path.join(JELLYFIN_PLAYLIST_PATH, playlist)
    playlistFile = os.path.join(playlistFile, 'playlist.xml')

    if os.path.isfile(playlistFile) :
        dom = ElementTree.parse(playlistFile)
        paths = dom.findall('PlaylistItems/PlaylistItem/Path')

        cmusPlaylistFile = os.path.join(CMUS_PLAYLIST_PATH, playlist)

        if (not os.path.isfile(cmusPlaylistFile)) or isPlaylistUpdated(cmusPlaylistFile, paths) :
            updateFile(cmusPlaylistFile, paths)


# checkIfPlaylistUpdated('/home/nate/.config/cmus/playlists/test', None)