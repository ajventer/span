#!/usr/bin/env python3
import unittest
from leagueTable import LeagueTable, LeagueTableEntry


class LeagueTableTest(unittest.TestCase):
    def setUp(self):
        self.LT = LeagueTable()

    def tearDown(self):
        pass

    def testComparisons(self):
        """Test that our custom comparison operators will let us order the entries correctly"""
        testLTE1 = LeagueTableEntry('test1')
        testLTE2 = LeagueTableEntry('test2')

        #Equal scores should be alphabetically ordered
        assert testLTE1 > testLTE2

        testLTE2.leagueScore = 2
        assert testLTE2 > testLTE1

    def testCustomCollection(self):
        testLTE = LeagueTableEntry('test1')
        with self.assertRaises(TypeError):
            self.LT['test1'] = '2'
        self.LT['test1'] = 2
        assert self.LT['test1'] == 2

        #Test string based contain check
        assert 'test1' in self.LT


        #Test entry based contain check
        assert testLTE in self.LT

        del self.LT['test1']
        assert testLTE not in self.LT

    def testOrdering(self):
        self.LT['test1'] = 1
        self.LT['test2'] = 2
        self.LT['test3'] = 1

        orderedList = list(self.LT)
        #Test ordering by score
        assert orderedList[0].teamName == 'test2'
        #Test subordering by name
        assert orderedList[1].teamName == 'test1'

    def testStringParse(self):
        match = self.LT._matchEntries_('test1 3, test2 1')
        assert 'test1' in match
        assert 'test2' in match
        assert match['test1'] == 3
        assert match['test2'] == 1

    def testUpdateTeam(self):
        self.LT._updateTeam_('test1', 2)
        assert self.LT['test1'] == 2
        self.LT._updateTeam_('test1', 1)
        assert self.LT['test1'] == 3

    def testMatchHandler(self):
        #Verify that adding a match works fully
        #1. test1 wins, tes2 loses
        self.LT.addMatch('test1 3, test2 1')
        assert 'test1' in self.LT
        assert 'test2' in self.LT
        assert self.LT['test1'] == 3
        assert self.LT['test2'] == 0

        #2. A draw between test1 and test 3
        self.LT.addMatch('test1 2, test3 2')
        assert self.LT['test1'] == 4
        assert self.LT['test3'] == 1

if __name__ == '__main__':
    unittest.main()