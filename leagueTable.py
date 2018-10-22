from functools import total_ordering
import copy

@total_ordering
class LeagueTableEntry(object):
    '''
    Holds a single entry for the leagueTable collection, implements comparison operators to ensure sorting follows the rules.
    '''
    def __init__(self,teamName, leagueScore=0):
        self.teamName = teamName
        self.leagueScore = leagueScore

    def __gt__(self, other):
        if self.leagueScore == other.leagueScore:
            return self.teamName < other.teamName
        return self.leagueScore > other.leagueScore

    def __eq__(self, other):
        #This can't actually happen with our data because a team cannot play itself
        #but you need at least eq and lt for total_ordering to work
        return self.leagueScore == other.leagueScore and self.teamName == other.teamName

    def __str__(self):
        return '%s, %s pts' %(self.teamName, self.leagueScore)

class LeagueTable(object):
    '''
    A custom ordered collection class for league table values. Can be accessed by team_name like a dictionary.
    Abstracts the ordering process away entirely.
    '''
    def __init__(self):
        self.league = []


    def __contains__(self, item):
        if isinstance(item, LeagueTableEntry):
            return item.teamName in [i.teamName for i in self.league]
        elif isinstance(item, str):
            return item in  [i.teamName for i in self.league]
        else:
            raise TypeError('Item must be a string or a LeagueTableEntry')

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise TypeError('League scores must be integers')
        lte = LeagueTableEntry(key, value)
        if key in self:
            del self[key]
        self.league.append(lte)

    def __delitem__(self, key):
        toDel = [i for i in self.league if i.teamName == key][0]
        del self.league[self.league.index(toDel)]

    def __getitem__(self,key):
        return [i.leagueScore for i in self.league if i.teamName == key][0]

    def __iter__(self):
        for i in reversed(sorted(self.league)):
            yield (i)

    def _matchEntries_(self, matchString):
        def __teamsplit__(teamstr):
            score = teamstr.split()[-1]
            name = ' '.join(teamstr.split()[:-1])
            return name, int(score)
        '''
        Internal function to handle the string processing on a match entry
        returns a simple to process dictionary.
        '''
        r1, r2 = matchString.split(',')
        r1 = __teamsplit__(r1)
        r2 = __teamsplit__(r2)
        return {r1[0]: r1[1], r2[0]: r2[1]}

    def _updateTeam_(self, team, score):
        if not team in self:
            self[team] = score
        else:
            self[team] += score

    def addMatch(self, matchString):
        '''
        Our input doesn't come in the form of league scores, so here we provide a convenient
        function to just add a match to the game and get/update the results accordingly
        '''
        match = self._matchEntries_(matchString)
        if list(match.values())[0] > list(match.values())[1]:
            self._updateTeam_(list(match.keys())[0], 3)
            self._updateTeam_(list(match.keys())[1], 0)
        elif list(match.values())[0] == list(match.values())[1]:
            for k in match.keys():
                self._updateTeam_(k, 1)
        else:
            self._updateTeam_(list(match.keys())[0], 0)
            self._updateTeam_(list(match.keys())[1], 3)





