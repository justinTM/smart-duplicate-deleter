#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import json
import mutagen


def gather_all_music_files(root_path):
    print('Gathering all music files in "{0}"...'.format(root_path))
    music_filepaths = []
    ext_strings = ['.mp3', '.m4a', '.aac', '.wav', '.m4p']

    for root, dirs, files in os.walk(root_path):
        for fname in files:
            fname_lower = fname.lower()
            for ext_string in ext_strings:
                if fname_lower.endswith(ext_string):
                    fpath = os.path.join(root, fname)
                    music_filepaths.append(fpath)

    print('Found {0} total files in "{1}".'.format(len(music_filepaths), root_path))
    return music_filepaths


def get_id3_tags_for_filepaths(list_of_filepaths):
    print('Getting Mutagen id3 tags for each track...')
    for fpath in list_of_filepaths:
        try:
            audio = mutagen.File(fpath, easy=True)
        except mutagen.mp3.HeaderNotFoundError:
            pass

        if not audio: continue
        audio.pprint()
        print(audio)
        # print ('\
        # \t    title: {0}\n\
        # \t    artist: {1}\n\
        # \t    key: {4}\n\
        # \t    bpm: {3}\n\
        # '.format(
        #     audio['title'],
        #     audio['artist'],
        #     audio['key'],
        #     audio['bpm'],
        # ))


def get_pair_of_duplicate_songs(list_of_music_filepaths):
    '''
    Returns two songs based on the matching confidence interval of their titles
        Given: a list of songs, and a confidence threshold (0.00 - 1.00)
        Returns: a tuple of songs whose titles match within a specified confidence interval
    '''
    return



def mark_songs_to_delete(list_of_songs):
    '''
    Decides whether to keep or delete a song based on rules about the file metadata
        Given: a list of songs
        Returns: the modified list with deletion flags added
    '''
    # higher bitrate > lower bitrate
    # has Traktor analysis > no Traktor analysis
    # newer > older
    return

def main():
    print('Hello world!')
    root_dir = '/Users/justinmai/Music'
    list_of_music_filepaths = gather_all_music_files(root_dir)

    get_id3_tags_for_filepaths(list_of_music_filepaths)

    print(len(list_of_music_filepaths))
    print(json.dumps(list_of_music_filepaths, indent=4))

if __name__ == '__main__':
    main()
