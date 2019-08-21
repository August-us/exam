result={
    'a':lambda x:x*5,
    'b':lambda x:x+7,
    'c':lambda x:x-2,
}
print (result['a'](8))


def a(x):
    print ('a'+x)
def b(x):
    print ('b'+x)

values={
    'a':a,
    'b':b
}
values.get('a')('8')


class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False
    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False


v = 'ten'
for case in switch(v):
    if case('one'):
        print(1)
        break
    if case('two'):
        print( 2)
        break
    if case('ten'):
        print (10)
        break
    if case('eleven'):
        print (11)
        break
    if case(): # default, could also just omit condition or 'if True'
        print ("something else!")