
class Base(object):
    usages = {}

    def __init__(self):

        object.__init__(self)
        rep = str(object.__repr__(self))
        Base.usages[rep] = 1

    def __getattribute__(self, name):
        Base.usages[object.__repr__(self)] += 1

        return object.__getattribute__(self, name)

    def __del__(self):
        Base.usages.__delitem__(object.__repr__(self))


class Foo(Base):
    def __init__(self):
        Base.__init__(self)
        self.field = 5

    def foo(self):
        print "foo()"


def func():
    f = Foo()
    print "Usages in function:\n", Base.usages

    print "leve func"

class Bar(Base):

    def bar(self):
        print "bar()"

if __name__ == '__main__':
    print "Usages at start:\n", Base.usages

    f = Foo()
    print "Usages after creating Foo object:\n", Base.usages

    b = Bar()

    print "Usages after creating Bar object:\n", Base.usages

    f.foo()
    b.bar()

    print "Usages after access functions:\n", Base.usages

    print "foo field:", f.field
    print "Usages after access field:\n", Base.usages

    func()
    print "Usages after function:\n", Base.usages



