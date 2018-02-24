from mock import call
from mock import patch

from foolscap import note_content


def test_update_notes():
    pass


def test_save_note():
    pass


def test_export_note():
    with patch('foolscap.note_content.note_exists') as exists:
        exists.return_value = False
        note_content.export_note('test_note')
        exists.assert_called_once_with('test_note')


def test_view_note():
    with patch('foolscap.note_content.note_exists') as exists:
        exists.return_value = False
        note_content.view_note('test_note')
        exists.assert_called_once_with('test_note')


def test_delete_note():
    with patch('foolscap.note_content.note_exists') as exists:
        exists.return_value = False
        note_content.delete_note('test_note')
        exists.assert_called_once_with('test_note')


def test_edit_note():
    with patch('foolscap.note_content.note_exists') as exists:
        exists.return_value = False
        note_content.edit_note('test_note')
        exists.assert_called_once_with('test_note')


def test_new_note():
    pass


def test_move_lines():
    with patch('foolscap.note_content.note_exists') as exists,\
         patch('builtins.input') as input_string:
        input_string.return_value = 'second_note'
        # First one has to set as True as it is called sequentially
        exists.side_effect = [True, False]
        expected_calls = [call('second_note'),
                          call('test_note')]

        note_content.move_lines('test_note')
        exists.assert_has_calls(expected_calls)
    
