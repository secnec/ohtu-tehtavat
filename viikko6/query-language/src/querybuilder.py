from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder():
    def __init__(self, matchers = All()):
            self._matchers = matchers

    def playsIn(self,team):
        return QueryBuilder(And(self._matchers, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matchers, HasAtLeast(value,attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matchers, HasFewerThan(value,attr)))

    def oneOf(self, *matchers):
        return QueryBuilder(Or(*matchers))

    def build(self):
        return self._matchers