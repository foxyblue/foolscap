import datetime


def mock_data(views, year=2000, tag='fake_tag', book='general'):
    modified = datetime.datetime(year, 12, 10, 15, 25, 19, 11262)
    return {
        'description': 'This is a fake note',
        'created': datetime.datetime(2000, 12, 10, 15, 25, 19, 11262),
        'modified': modified,
        'tags': [tag],
        'book': book,
        'views': views
    }


def mock_w_subheadings(views, year=2000, book='general'):
    modified = datetime.datetime(year, 12, 10, 15, 25, 19, 11262)
    return {
        'description': 'This is a fake note',
        'created': datetime.datetime(2000, 12, 10, 15, 25, 19, 11262),
        'modified': modified,
        'tags': ['fake_tag'],
        'book': book,
        'views': views,
        'length': 7,
        'sub_headings': [('First Sub:', ':A sub headings', 1, 1)],
        'num_sub': 1
    }


FAKE_SINGLE_NOTE_2 = {
    'most_viewed': mock_w_subheadings(4)
}

FAKE_FOUR_NOTES_W_SUB = {
    'B': mock_w_subheadings(4),
    'A': mock_w_subheadings(3),
    'D': mock_w_subheadings(2),
    'C': mock_w_subheadings(1),
}

FAKE_SINGLE_NOTE = {
    'most_viewed': mock_data(4)
}

FAKE_SEARCH = {
    '__note': mock_data(4),
    '_note': mock_data(4),
    'not_found': mock_data(4),
    '___note': mock_data(4),
    'note': mock_data(4),
    '____note': mock_data(4),
}

FAKE_DIFF_BOOKS = {
    'note_01': mock_data(4, book='work'),
    'note_02': mock_data(4, book='work'),
    'note_03': mock_data(4, book='work'),
    'note_04': mock_data(4, book='work'),
    'note_05': mock_data(4, book='work'),
    'note_06': mock_data(4),
    'note_07': mock_data(4),
    'note_08': mock_data(4),
    'note_09': mock_data(4),
    'note_10': mock_data(4),
    'note_11': mock_data(4),
    'note_12': mock_data(4),
    'note_13': mock_data(4),
    'note_14': mock_data(4),
}


FAKE_MANY_NOTES = {
    'most_viewed': mock_data(4),
    'second_most': mock_data(3),
    'third_most': mock_data(2),
    'recently_opened': mock_data(1, year=2018),
    'A': mock_data(1),
    'fake_note_1': mock_data(1),
    'Z': mock_data(1),
}


FOUR_FAKE_NOTES = {
    'C': mock_data(4),
    'B': mock_data(3),
    'A': mock_data(2),
    'recently_opened': mock_data(1, year=2018),
}


FOUR_FAKE_NOTES_TAGS = {
    'C': mock_data(2, tag='one'),
    'B': mock_data(2, tag='two'),
    'A': mock_data(2, tag='three'),
    'D': mock_data(2, tag='one'),
}


FAKE_NOTES_EDGE_CASE = {
    'F': mock_data(5),
    'E': mock_data(5),
    'D': mock_data(5),
    # Recent Viewed:
    'G': mock_data(5, year=2001),
    'A': mock_data(5),
    'B': mock_data(5),
    'C': mock_data(5),
}


def mock_component(views, year=2000, modified='no_change',
                   tags=['fake_tag'], length=1):
    return {
        'description': 'This is a fake note',
        'created': 'created_date',
        'modified': modified,
        'tags': tags,
        'book': 'general',
        'views': views,
        'length': length,
        'vim_cmds': [':set textwidth=60'],
    }


def MOCK_COMPONENT(views, date, length=1, tags=['fake_tag'], name='note'):
    return {
        name: mock_component(views, modified=date, tags=tags, length=length)
    }
