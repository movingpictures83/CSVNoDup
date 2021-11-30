class CSVNoDupPlugin:
    def input(self, infile):
       inputcsv = open(infile, 'r')
       self.lines = []
       for line in inputcsv:
           self.lines.append(line.strip().split(','))

    def run(self):
        # Find dups in first line
        names = []
        dups = []
        for element in self.lines[0]:
            if (element not in names):
                names.append(element)
            elif (element not in dups):
                dups.append(element)

        counters = dict()
        for dup in dups:
            counters[dup] = 0
        for i in range(len(self.lines[0])):
            if (self.lines[0][i] in dups):
                name = self.lines[0][i]
                self.lines[0][i] = '\"' + self.lines[0][i][1:len(self.lines[0][i])-1]+" "+str(counters[self.lines[0][i]]+1) + '\"'
                self.lines[i+1][0] = '\"' + self.lines[i+1][0][1:len(self.lines[i+1][0])-1]+" "+str(counters[self.lines[i+1][0]]+1) + '\"'
                counters[name] += 1


    def output(self, outfile):
        outputcsv = open(outfile, 'w')
        for line in self.lines:
           for i in range(0, len(line)):
               outputcsv.write(line[i])
               if (i != len(line)-1):
                   outputcsv.write(',')
               else:
                   outputcsv.write('\n')
