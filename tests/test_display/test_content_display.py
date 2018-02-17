import pytest
from mock import call
from mock import patch
from mock import MagicMock

from foolscap.display.content_display import _set_colour
from foolscap.display.content_display import DisplayContents


# Patch variables:
patch_NORMAL = 'foolscap.display.content_display.NORMAL_LINE_COLOUR'
patch_DIM = 'foolscap.display.content_display.DIM_LINE_COLOUR'
patch_REVERSE = 'foolscap.display.content_display.REVERSE_LINE_COLOUR'
patch_TITLE = 'foolscap.display.content_display.TITLE'
patch_DESCRIP = 'foolscap.display.content_display.DESCRIPTION'

FAKE_ITEMS = [
    {'title': "test_title", 'description': "test description"},
    {'title': "another_title", 'description': "another description"},
]


@pytest.mark.parametrize("line,cursor,expected",
    [(3,4,'NORMAL'),
     (4,4,'REVERSE'),
     (6,4,'DIM')])
def test_set_colour(line, cursor, expected):
    with patch(patch_NORMAL, 'NORMAL'),\
         patch(patch_DIM, 'DIM'),\
         patch(patch_REVERSE, 'REVERSE'):
        result = _set_colour(line, cursor)
        assert result == expected


def test_DisplayContents_init():
    mock_screen = MagicMock()
    mock_screen.getmaxyx.return_value = 50, 50
    test_DC = DisplayContents(mock_screen, FAKE_ITEMS)

    assert isinstance(test_DC, DisplayContents)
    assert hasattr(test_DC, 'menu_items')
    assert len(test_DC.menu_items) == len(FAKE_ITEMS)
    mock_screen.getmaxyx.called_once()


def test_DisplayContents_update_position():
    mock_screen = MagicMock()
    mock_screen.getmaxyx.return_value = 50, 50
    test_DC = DisplayContents(mock_screen, FAKE_ITEMS)

    test_DC.update_pointers(1, 3)
    assert hasattr(test_DC, 'cursor')
    assert hasattr(test_DC, 'first_index')
    assert test_DC.cursor == 3
    assert test_DC.first_index == 1


def test_DisplayContents_draw():
    mock_screen = MagicMock()
    mock_screen.getmaxyx.return_value = 100, 100

    test_DC = DisplayContents(mock_screen, FAKE_ITEMS)
    # display cursor on note 3.
    test_DC.update_pointers(0, 2)

    with patch(patch_NORMAL, 'NORMAL'),\
         patch(patch_DIM, 'DIM'),\
         patch(patch_REVERSE, 'REVERSE'),\
         patch(patch_TITLE, '{}'),\
         patch(patch_DESCRIP, '{}'):
        test_DC.draw()
        calls = [call.getmaxyx(),
                 call.addstr(1, 0, "test_title", "NORMAL"),
                 call.addstr(1, 48, "test description", "NORMAL"),
                 call.addstr(2, 0, "another_title", "REVERSE"),
                 call.addstr(2, 48, "another description", "REVERSE")]
        mock_screen.assert_has_calls(calls)


def test_DisplayContents_draw_small():
    mock_screen = MagicMock()
    mock_screen.getmaxyx.return_value = 50, 50

    test_DC = DisplayContents(mock_screen, FAKE_ITEMS)
    test_DC.update_pointers(0, 2)

    with patch(patch_NORMAL, 'NORMAL'),\
         patch(patch_DIM, 'DIM'),\
         patch(patch_REVERSE, 'REVERSE'),\
         patch(patch_TITLE, '{}'),\
         patch(patch_DESCRIP, '{}'):
        test_DC.draw()
        calls = [call.getmaxyx(),
                 call.addstr(1, 0, "test_title", "NORMAL"),
                 call.addstr(2, 0, "another_title", "REVERSE")]
        mock_screen.assert_has_calls(calls)


def test_DisplayContents_draw_smaller():
    fake_items = [
        {'title': "test_title", 'description': "test description"},
        {'title': "another_title_1", 'description': "another description"},
        {'title': "another_title_2", 'description': "another description"},
        {'title': "another_title_3", 'description': "another description"},
        {'title': "another_title_4", 'description': "another description"},
        {'title': "another_title_5", 'description': "another description"},
    ]
    mock_screen = MagicMock()
    mock_screen.getmaxyx.return_value = 7, 50

    test_DC = DisplayContents(mock_screen, fake_items)
    test_DC.update_pointers(0, 2)

    with patch(patch_NORMAL, 'NORMAL'),\
         patch(patch_DIM, 'DIM'),\
         patch(patch_REVERSE, 'REVERSE'),\
         patch(patch_TITLE, '{}'),\
         patch(patch_DESCRIP, '{}'):
        test_DC.draw()
        calls = [call.getmaxyx(),
                 call.addstr(1, 0, "test_title", "NORMAL"),
                 call.addstr(2, 0, "another_title_1", "REVERSE"),
                 call.addstr(3, 0, "another_title_2", "NORMAL")]
        mock_screen.assert_has_calls(calls)


