import pytest
from UnitTestCode import documents, directories, get_person, add_doc, delete_doc
TEST_ADD = [
    (documents, directories, 'passport', '100-1', 'John Smith', '3',
     {'type': 'passport', 'number': '100-1', 'name': 'John Smith'}),

    (documents, directories, 'pasport', '100', 'John', '3',
     {'type': 'pasport', 'number': '100', 'name': 'John'}),

    (documents, directories, 'passport', '100-1', 'John Smith', '4',
     'Такой полки не существуйте, попробуйте снова.')
    ]
TEST_DEL = [
    (documents, directories, '2207 876234', 'OK'),
    (documents, directories, '11-2', 'OK'),
    (documents, directories, '11111', 'Документ не найден, введите заново')
]
TEST_GET = [
    (documents, '10006', 'OK'),
    (documents, '2207 876234', 'OK'),
    (documents, '1006', 'Документ не найден, введите заново.')
]
DOC = [{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}]
DIR = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


class TestRemoving:
    def setup(self):
        print('\nDeleting docs:')

    @pytest.mark.parametrize('docs, dirs, doc_num, result', TEST_DEL)
    def test_deletion(self, docs, dirs, doc_num, result):
        docs = DOC
        dirs = DIR
        assert delete_doc(docs, dirs, doc_num) == result

    def teardown(self):
        print('\nFinished deleting')


class TestGetting:
    def setup(self):
        print('\nStarting reading')

    @pytest.mark.parametrize('docs, doc_num, result', TEST_GET)
    def test_get_person(self, docs, doc_num, result):
        assert get_person(docs, doc_num) == result

    def teardown(self):
        print('\nFinished reading')


class TestAdding:

    def setup(self):
        print('\nAdding docs:')

    @pytest.mark.parametrize('docs, dirs, doct_type, doc_number, doc_name, dir_number, result', TEST_ADD)
    def test_addition(self, docs, dirs, doct_type, doc_number, doc_name, dir_number, result):
        assert add_doc(docs, dirs, doct_type, doc_number, doc_name, dir_number) == result

    def teardown(self):
        print('\nClearing added entry')
        documents.pop()
        directories['3'].clear()
