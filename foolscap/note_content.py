import os

from meta_data import save_data
from fuzzy_note import fuzzy_guess
from file_paths import NOTE_FOLDERS
from parse_text import (
    load_text,
    edit_text,
    unique_heading,
    shift_lines,
    note_component,
    update_component,
)


not_found = '\n\tNot found, did you mean "{}"?\n'


def save_note(new_note, saved_notes, temp_file=False):
    """ Convert note.txt to dict components and save.

    :param new_note: (string) name of .txt file.
    :param saved_notes: (dict) of notes in data.
    """

    # Used for parsing '.txt' notes.
    if not temp_file:
        new_note = load_text(new_note)

    new_component = note_component(new_note)

    saved_notes.update(new_component)
    save_data(saved_notes)
    if temp_file:
        title = list(new_component.keys())[0]
        print("\n\tSaved note: '{}'.\n".format(title))
    else:
        for title in new_component.keys():
            print("\n\tAdded: '{}'.\n".format(title))


def export_note(note, stored_data):
    stored_notes = stored_data.keys()
    name_note = NOTE_FOLDERS['GET_NOTE']

    if note in stored_notes:
        note_text = load_text(name_note.format(note_name=note))
        with open(note + '.txt', 'w') as write_file:
            for line in note_text:
                write_file.write(line + '\n')

        stored_data = update_component(note, stored_data)
        save_data(stored_data)

        print("\n\tExported: '{}'.\n".format(note))

    else:
        guess = fuzzy_guess(note, stored_notes)
        print(not_found.format(guess))


def view_note(note, stored_data):
    """ Print the note to console if found.

    :param new_note: (string) name of .txt file.
    :param saved_notes: (dict) of notes in data.
    """
    stored_notes = stored_data.keys()
    name_note = NOTE_FOLDERS['GET_NOTE']

    if note in stored_notes:
        note_text = load_text(name_note.format(note_name=note))

        for line in note_text:
            print(line)

        stored_data = update_component(note, stored_data)
        save_data(stored_data)

    else:
        guess = fuzzy_guess(note, stored_notes)
        print(not_found.format(guess))


def delete_note(note, stored_data):
    """ Delete a note stored in foolscap

    :param new_note: (string) name of .txt file.
    :param saved_notes: (dict) of notes in data.
    """
    stored_notes = stored_data.keys()

    if note in stored_notes:
        folders = NOTE_FOLDERS

        delete_file = folders['GET_NOTE'].format(note_name=note)

        recycle_bin = unique_heading(note, folder='IN_BIN')
        bin_note = folders['BIN_NOTE'].format(note_name=recycle_bin)

        os.rename(delete_file, bin_note)

        stored_data.pop(note, None)
        save_data(stored_data)
        print("\n\tDeleted: '{}'.\n".format(note))

    else:
        guess = fuzzy_guess(note, stored_notes)
        print(not_found.format(guess))


def edit_note(note, stored_data):
    """ Edit the note from data in vim.

    :param note: (string) name of .txt file.
    :param stored_data: (dict) of notes in data.
    """
    stored_notes = stored_data.keys()

    if note in stored_notes:
        edited_note = NOTE_FOLDERS['GET_NOTE'].format(note_name=note)
        edit_text(editing=edited_note)

        stored_data = update_component(note, stored_data)
        save_data(stored_data)

        print("\n\tUpdated: '{}'.\n".format(note))

    else:
        guess = fuzzy_guess(note, stored_notes)
        print(not_found.format(guess))


def new_note(stored_notes):
    """ Create a new note in vim from template.

    :param stored_notes: (dict) of notes in data.
    """
    new_text = edit_text()

    # don't write unchanged notes.
    if '# title' == new_text[0]:
        print('\n\tAborted Note.\n')

    else:
        save_note(new_text, stored_notes, temp_file=True)


def move_lines(note, stored_data):
    """ Move selected lines from a note to another note.

    :param note: (string) title of note to move lines to.
    :param stored_data: (dict) of notes in data.
    """
    from_note = input('Move lines from? ')

    stored_notes = stored_data.keys()
    if note not in stored_notes:
        guess = fuzzy_guess(note, stored_notes)
        print(not_found.format(guess))

    if from_note in stored_notes:
        edited_note = NOTE_FOLDERS['GET_NOTE'].format(note_name=from_note)
        edit_text(editing=edited_note)

        stored_data = shift_lines(from_note, note)
    else:
        guess = fuzzy_guess(note, stored_notes)
        print(not_found.format(guess))

