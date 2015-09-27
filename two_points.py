import sys
import math

class Solver(object):

    '''
    class Solver with necessary methods for solving the task.
    '''

    def __init__(self, coords):
        '''
        Take a list of lists(tuples) which represents a set of coordinates.
        '''
        super(Solver, self).__init__()
        self.coords = coords

    def _get_distance(self, coord1, coord2):
        '''
        Return distance in euclidean metrics. Math.sqrt returns result in float.
        '''
        return math.sqrt(sum(((coord2[i] - coord1[i]) ** 2 for i in xrange(len(coord1)))))

    def get_result(self):
        '''
        Solving method with naive algorithm. O(N^2) complexity where N = len(coords).
        '''
        if len(self.coords) < 2:
            return 0

        res_dist = -1
        for i in xrange(len(self.coords) - 1):
            for j in xrange(i + 1, len(self.coords)):
                dist = self._get_distance(self.coords[i], self.coords[j])
                if res_dist == -1 or dist < res_dist:
                    res_dist = dist

        return dist

def usage():

    script_name = sys.argv[0]
    print "Usage:"
    print "python %s <filename>" % (script_name)
    print "For example:"
    print "python %s test_set_1.txt" % (script_name)

if __name__ == "__main__":

    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    filename = sys.argv[1]
    coords = []
    with open(filename) as fd:
        coords = map(lambda x: (int(x[0]), int(x[1])), (line.split() for line in fd if line.strip() != ""))

    '''
    Print result as is, without precision set, as it was not mentioned in the task.
    '''
    print Solver(coords).get_result()
