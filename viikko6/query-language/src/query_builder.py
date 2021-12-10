from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher = matcher

    def playsIn(self, team):
        return QueryBuilder(And(self._matcher, PlaysIn(team)))

    def hasAtLeast(self, points, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(points, attr)))

    def hasFewerThan(self, points, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(points, attr)))

    def oneOf(self, *matchers):
        return QueryBuilder(Or(*matchers))

    def build(self):
        return self._matcher 