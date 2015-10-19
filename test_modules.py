import unittest
import getSearchString, scrapeSites

class TestGetSearchString(unittest.TestCase):
	def runTest(self):
		self.assertTrue(isinstance(getSearchString.getSearchString(), str))
