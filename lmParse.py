import numpy as np
import pandas as pd


class Log:
    def __init__(self, fname=None):
        self.data = pd.DataFrame()
        self.N = []
        self.logFiles = []
        self.run = 0
        if fname:
            self.parseLog(fname)

    def __getitem__(self, arg):
        if arg.lower() == 'index':
            return self.data.index
        elif arg.lower() == 'n':
            return self.getN()
        else:
            try:
                return self.data[arg]
            except:
                raise KeyError('Key {} not found! Valid keys are:'.format(arg),
                               ' '.join(self.keys()))

    def getN(self):
        N = np.array(self.N)
        if np.all(N == self.N[0]):
            return self.N[0]
        else:
            return N

    def keys(self):
        return self.data.keys()

    def fileNames(self):
        return self.logFiles

    def parseLog(self, fname):
        if fname in self.logFiles:
            raise ValueError('{} has already been parsed'.format(fname))
        newData = []
        headerline = False
        dataline = False
        tailline = False
        with open(fname, 'r') as f:
            for line in f:
                if (line[:12] == 'Memory usage') or \
                   (line[:12] == 'Per MPI rank'):
                    headerline = True
                    tailline = False
                    continue
                if line[:4] == 'Loop':
                    headerline = False
                    dataline = False
                    tailline = True
                    self.run += 1
                    self.N.append(int(line.split()[-2]))
                if headerline:
                    headerline = False
                    dataline = True
                    categories = line.strip().split()
                    continue
                if (dataline) and not (headerline) and not (tailline):
                    l = [float(v) for v in line.strip().split()]
                    newData.append({c: v for c, v in zip(categories, l)})
                    newData[-1]['Run'] = self.run
        self.data = self.data.append(newData, ignore_index=True)
        self.logFiles.append(fname)
