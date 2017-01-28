import unittest
from app import app
from flask import Flask


class MyTestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_404_status_code(self):
        status_404 = self.app.get('/aisjcweija')
        self.assertEqual(status_404.status_code, 404)

    def test_home_status_code(self):
        result = self.app.get('/')
        result_2 = self.app.get('/live')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_2.status_code, 200)

    def test_highlights_status_code(self):
        highlights = self.app.get('/highlights')
        self.assertEqual(highlights.status_code, 200)

    def test_live_streams_status_code(self):
        result = self.app.get('/livestreams')
        self.assertEqual(result.status_code, 200)

    def test_stats_status_code(self):
        stats = self.app.get('/standings')
        self.assertEqual(stats.status_code, 200)
        match_detail = self.app.get('/match-details')
        self.assertEqual(match_detail.status_code, 200)
        fixtures = self.app.get('/fixtures')
        self.assertEqual(fixtures.status_code, 200)
        topscorer = self.app.get('/topscorer')
        self.assertEqual(topscorer.status_code, 200)

    def test_highlights_post(self):
        result = self.app.post('/highlights?match_name=manchester united')      # POST Request, no data in URL
        print(result.data)
        self.assertEqual(result.status_code, 400)                               # Bad Request
