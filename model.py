
import re

########################################
#
#  Model class
#
########################################

# define distribution to map value tuples to probabilities (or frequencies or scores, if not normalized)
class Model(dict):
    # define as promiscuous dictionary: populate with default values when queried on missing keys
    def __missing__(self,k):
        self[k]=0.0
        return self[k]
    # define get wihtout promiscuity
    def get(self,k):
        return dict.get(self,k,0.0)
    # init with model id
    def __init__(self,i=''):
        self.id = i
    # normalize to make consistent probability distribution
    def normalize(self):
        tot = 0.0
        for v in self: tot += self[v]
        for v in self: self[v] /= tot
    # read model
    def read(self,s):
        m = re.search('^ *'+self.id+' +: +(.*?) += +(.*) *$',s)
        if m is not None:
            v = tuple(re.split(' +',m.group(1)))
            if len(v)==1: v = v[0]
            self[v] = float(m.group(2))
    # write model
    def write(self):
        for v in sorted(self):
            print self.id,
            print ':',
            if type(v) is tuple:
                for f in v:
                    print f,
            else: print v,
            print '=',self[v]


########################################
#
#  CondModel class
#
########################################

# define model to map condition tuples to distributions
class CondModel(dict):
    # define as promiscuous dictionary: populate with default values when queried on missing keys
    def __missing__(self,k):
        self[k]=Model()
        return self[k]
    # define get without promiscuity
    def get(self,k):
        return dict.get(self,k,Model())
    # init with model id
    def __init__(self,i):
        self.id = i
    # normalize to make consistent probability distribution
    def normalize(self):
        for c in self:
            tot = 0.0
            for v in self[c]: tot += self[c][v]
            for v in self[c]: self[c][v] /= tot
    # read model
    def read(self,s):
        m = re.search('^ *'+self.id+' +(.*?) +: +(.*?) += +(.*) *$',s)
        if m is not None:
            c = tuple(re.split(' +',m.group(1)))
            if len(c)==1: c = c[0]
            v = tuple(re.split(' +',m.group(2)))
            if len(v)==1: v = v[0]
            self[c][v] = float(m.group(3))
    # write model
    def write(self):
        for c in sorted(self):
            for v in sorted(self[c]):
                print self.id,
                if type(c) is tuple:
                    for f in c:
                        print f,
                else: print c,
                print ':',
                if type(v) is tuple:
                    for f in v:
                        print f,
                else: print v,
                print '=',self[c][v]
