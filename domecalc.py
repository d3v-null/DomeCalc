
from pyvpsolver import *

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
		assert(all( W>0 and isinstance(W, int) for W in self.input['W']))
		assert(all( w>0 and isinstance(w, int) for w in [wr for wr in self.input['w'] ]))
		assert(all( b>0 and isinstance(b, int) for b in self.input['b']))


	def solve(self):
		instance = VBP(self.input['W'], self.input['w'], self.input['b'])
		afg = AFG(instance, verbose=False)
		lp_model = LP(afg, verbose=False)
		out, sol = VPSolver.script("vpsolver_glpk.sh", lp_model, afg, verbose=False)
		# out, sol = VPSolver.script("vpsolver_glpk.sh", instance)
		self.obj, self.patterns = sol
		return (self.obj, self.patterns)
		# print "Objective:", obj
		# print "Solution:"
		# print '\n'.join(map(str,patterns))
		# pass

	@staticmethod
	def strut_length(radius, adjust, coefficient):
		return int(coefficient * radius + adjust)

	@staticmethod
	def preset_2V(radius, adjust, master, strut_length):
		wc 	= [.618, .546]
		b 	= [  35,   30]
		return {
			'W': [master],
			'w': [strut_length(radius, adjust, coefficient) for coefficient in wc],
			'b': b,
		}

	@staticmethod
	def preset_3V3(radius, adjust, master, strut_length):
		wc = [.348, .403, .412]
		b  = [  30,   40,   50]
		return {
			'W': [master],
			'w': [strut_length(radius, adjust, coefficient) for coefficient in wc],
			'b': b,
		}
	@staticmethod
	def preset_3V5(radius, adjust, master, strut_length):
		wc = [.348, .403, .412]
		b  = [  30,   55,   80]
		return {
			'W': [master],
			'w': [strut_length(radius, adjust, coefficient) for coefficient in wc],
			'b': b,
		}
	@staticmethod
	def preset_3VK4(radius, adjust, master, strut_length):
		wc = [.330, .382, .421]
		b  = [  30,   40,   50]
		return {
			'W': [master],
			'w': [strut_length(radius, adjust, coefficient) for coefficient in wc],
			'b': b,
		}
	@staticmethod
	def preset_3VK5(radius, adjust, master, strut_length):
		wc = [.330, .382, .421]
		b  = [  30,   55,   80]
		return {
			'W': [master],
			'w': [strut_length(radius, adjust, coefficient) for coefficient in wc],
			'b': b,
		}
	@staticmethod
	def preset_4V(radius, adjust, master, strut_length):
		wc = [.253, .295, .294, .312, .324, .298]
		b  = [  30,   30,   60,   70,   30, 30]
		return {
			'W': [master],
			'w': [strut_length(radius, adjust, coefficient) for coefficient in wc],
			'b': b,
		}



if __name__ == '__main__':
	# domecalc = DomeCalc(DomeCalc.preset_2V, 2330, -80, 6000)
	# domecalc = DomeCalc(DomeCalc.preset_2V, 4300, 40, 6100)
	# domecalc = DomeCalc(DomeCalc.preset_3VK5, 4000, 40, 6100)
	# for i in range(3500, 4500, 100):
	# 	print ""
	# 	print i
	# 	print ""
	# 	for j in [DomeCalc.preset_2V, DomeCalc.preset_3VK4, DomeCalc.preset_3VK5, DomeCalc.preset_4V]:
	# 		domecalc = DomeCalc(j, i, 40, 6100)
	# 		print domecalc.input
	# 		domecalc.solve()

	# domecalc = DomeCalc(DomeCalc.preset_4V, 4300, 40, 6100)

	import csv

	with open('out.csv', 'w') as outFile:
		csvwriter = csv.writer(outFile)
		#write header
		csvwriter.writerow(['', '2V', '3VK4', '3VK5', '4V'])
		for i in range( 2000, 6500, 10 ):
			print i
			row = [i]
			for j in [DomeCalc.preset_2V, DomeCalc.preset_3VK4, DomeCalc.preset_3VK5, DomeCalc.preset_4V]:
				domecalc = DomeCalc(j, i, 40, 6500)
				domecalc.solve()
				row.append(domecalc.obj)
			csvwriter.writerow(row)


		# domecalc = DomeCalc(DomeCalc.preset_2V, 2570, 40, 6100)
		# print domecalc.input
		# domecalc.solve()
		
		# print DomeCalc.preset_2V(4000, 40, 6100)		
