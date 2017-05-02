
from pyvpsolver import VBP, AFG, LP, VPSolver
import shutil
import os

class DomeCalc(object):
    """docstring for DomeCalc"""

    def __init__(self, preset, radius, adjust, master ):
        super(DomeCalc, self).__init__()
        if preset:
            self.input = preset(radius, adjust, master, self.strut_length)
            self.check_input()

    def check_input(self):
        assert(all( k in self.input.keys() for k in ['W', 'w', 'b']))
        # assert(len(self.input['w'] == len(self.input['b'])))
        # assert(all( W>0 and isinstance(W, int) for W in self.input['W']))
        assert isinstance(self.input['W'], tuple)
        for W in self.input['W']:
            assert W>0
            assert isinstance(W, int)
        assert isinstance(self.input['w'], list)
        for wr in self.input['w']:
            assert isinstance(wr, tuple)
            for item in wr:
                assert isinstance(item, int)
                assert item > 0
        # assert(all( w>0 and isinstance(w, int) for w in [wr for wr in self.input['w'] ]))
        assert isinstance(self.input['b'], list)
        for b in self.input['b']:
            assert isinstance(b, int)
            assert b>0
        # assert(all( b>0 and isinstance(b, int) for b in self.input['b']))


    def solve(self):
        print "solving for %s" % self.input
        instance = VBP(self.input['W'], self.input['w'], self.input['b'])
        afg = AFG(instance, verbose=True)
        lp_model = LP(afg, verbose=True)
        new_afg = os.path.expanduser('~/graph.afg')
        # shutil.copyfile(afg.filename, new_afg)
        # print "afg: %s -> %s" % (afg.filename, new_afg)
        new_lp = os.path.expanduser('~/model.lp')
        # shutil.copyfile(lp_model.filename, new_lp)
        # print "lp_model: %s -> %s" % (lp_model.filename, new_lp)
        out, sol = VPSolver.script("/usr/local/bin/vpsolver_glpk.sh", lp_model, afg, verbose=False)
        # out, sol = VPSolver.script("vpsolver_glpk.sh", instance)
        self.obj, self.patterns = sol
        return (self.obj, self.patterns)
        # print "Objective:", obj
        # print "Solution:"
        # print '\n'.join(map(str,patterns))
        # pass

    @property
    def pattern_str(self):
        try:
            patterns = self.patterns
        except:
            return ""
        # print "resolving patterns: %s" % patterns
        out_str = ""
        for solution in patterns:
            for pattern in solution:
                # print "-> resolving pattern: %s" % str(pattern)
                out_str += "%d x %s, " % (
                    pattern[0],
                    "".join(map(
                        lambda x: chr(x[0]+97),
                        pattern[1]
                    ))
                )
        return out_str


    @staticmethod
    def strut_length(radius, adjust, coefficient):
        return int(coefficient * radius + adjust)

    @staticmethod
    def preset_2V(radius, adjust, master, strut_length):
        wc     = [.618, .546]
        b     = [  35,   30]
        return {
            'W': (master, ),
            'w': [(strut_length(radius, adjust, coefficient), ) for coefficient in wc],
            'b': b,
        }

    @staticmethod
    def preset_3V3(radius, adjust, master, strut_length):
        wc = [.348, .403, .412]
        b  = [  30,   40,   50]
        return {
            'W': (master, ),
            'w': [(strut_length(radius, adjust, coefficient), ) for coefficient in wc],
            'b': b,
        }
    @staticmethod
    def preset_3V5(radius, adjust, master, strut_length):
        wc = [.348, .403, .412]
        b  = [  30,   55,   80]
        return {
            'W': (master, ),
            'w': [(strut_length(radius, adjust, coefficient), ) for coefficient in wc],
            'b': b,
        }
    @staticmethod
    def preset_3VK4(radius, adjust, master, strut_length):
        wc = [.330, .382, .421]
        b  = [  30,   40,   50]
        return {
            'W': (master, ),
            'w': [(strut_length(radius, adjust, coefficient), ) for coefficient in wc],
            'b': b,
        }
    @staticmethod
    def preset_3VK5(radius, adjust, master, strut_length):
        wc = [.330, .382, .421]
        b  = [  30,   55,   80]
        return {
            'W': (master, ),
            'w': [(strut_length(radius, adjust, coefficient), ) for coefficient in wc],
            'b': b,
        }
    @staticmethod
    def preset_4V(radius, adjust, master, strut_length):
        wc = [.253, .295, .294, .312, .324, .298]
        b  = [  30,   30,   60,   70,   30, 30]
        return {
            'W': (master, ),
            'w': [(strut_length(radius, adjust, coefficient), ) for coefficient in wc],
            'b': b,
        }
