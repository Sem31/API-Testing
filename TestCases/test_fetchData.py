from unittest import TestCase
from fetchData import fetchData

class testdata(TestCase):
    def test_fetch(self):
        f = fetchData()
        data = {
            'name' : ['Luke Skywalker', 'C-3PO', 'R2-D2',
                      'Darth Vader', 'Leia Organa', 'Owen Lars',
                       'Beru Whitesun lars', 'R5-D4', 'Biggs Darklighter',
                        'Obi-Wan Kenobi'],
            'status_code' : 200,
            }

        self.assertDictEqual(data,f.data())