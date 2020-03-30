import numpy as np
import pandas as pd
from collections import defaultdict


class Log:
    def __init__(self, fname=None):
        self.data = pd.DataFrame()
        self.runInfo = defaultdict(dict)
        self.logFiles = []
        self.run = 0
        if fname:
            self.parseLog(fname)

    def __getitem__(self, arg):
        if isinstance(arg, str):
            if arg.lower() == 'index':
                return self.data.index
            elif arg.lower() == 'n':
                return self.getN()
            else:
                try:
                    return self.data[arg]
                except KeyError:
                    err = 'Key {} not found! Valid keys are: {}'.format(
                        arg, ' '.join(self.keys()))
                    raise KeyError(err)
        elif isinstance(arg, int):
            if arg in self.runInfo:
                return self.runInfo[arg]
            elif arg == -1:
                return self.runInfo[self.run-1]
            else:
                raise KeyError(
                    'Key {} not found! Valid numeric keys are:'.format(arg),
                    ' '.join([str(k) for k in self.runInfo.keys()]))
        else:
            raise KeyError('Key {} not found!'.format(arg))

    def getN(self):
        N = np.array([self.runInfo[i]['N'] for i in range(self.run)])
        if np.all(N == N[0]):
            return N[0]
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
                    self.runInfo[self.run]['N'] = int(line.split()[-2])
                    self.runInfo[self.run]['LoopTime'] = float(line.split()[3])
                    self.run += 1
                if headerline:
                    headerline = False
                    dataline = True
                    categories = line.strip().split()
                    continue
                if (dataline) and not (headerline) and not (tailline):
                    lines = [float(v) for v in line.strip().split()]
                    newData.append({c: v for c, v in zip(categories, lines)})
                    newData[-1]['Run'] = self.run
                if 'Stopping criterion' in line:
                    sc = line.split('=')[-1].strip()
                    self.runInfo[self.run-1]['StoppingCriterion'] = sc
        self.data = self.data.append(newData, ignore_index=True)
        self.logFiles.append(fname)
