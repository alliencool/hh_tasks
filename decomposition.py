import sys

class Solver(object):

    '''
    class Solver with necessary methods for solving the task.
    '''
    
    def __init__(self, n, k):
        '''
        Take a number to decomposite and amount of addendums.
        '''
        super(Solver, self).__init__()
        self.number = n
        self.addendums = k

    def get_result(self):
        '''
        Solving the problem by building a 2-dimensional array of numbers and amount of addendums.
        Complexity of the algorithm is O(N^2 * K).
        '''

        if self.number <= 0 or self.addendums <= 0 or self.number < self.addendums:
            return 0
        
        cache = [[0 for j in xrange(self.addendums + 1)] for i in xrange(self.number + 1)]
        for i in xrange(1, self.number + 1):
            cache[i][1] = 1
            for j in xrange(1, self.number - i + 1):
                for ind in xrange(1, self.addendums):
                    if cache[j][ind] == 0:
                        continue
                    next_num = j + i
                    next_ind = ind + 1
                    if next_num > self.number or next_ind > self.addendums:
                        break
                    cache[next_num][next_ind] += cache[next_num - i][next_ind - 1]

        return cache[self.number][self.addendums]

def usage():

    script_name = sys.argv[0]
    print "Usage:"
    print "python %s <number> <amount of addendums>" % (script_name)
    print "For example:"
    print "python %s 150 50" % (script_name)

if __name__ == "__main__":
    
    if len(sys.argv) < 3:
        usage()
        sys.exit(1)

    print Solver(int(sys.argv[1]), int(sys.argv[2])).get_result()
    
