from domecalc import DomeCalc

# create DomeCalc object: 
# -> A 2V dome, 
# -> radius=2330mm, 
# -> adjustment=-80mm, maste
calc = DomeCalc(
	preset=DomeCalc.preset_4V, 
	radius=4300, 
	adjust=40, 
	master=6100
)

calc.solve()
print "Number of lengths:", calc.obj
print "solution makeup:"
for quantity, pattern in calc.patterns:
	print "%3d x %s" % (quantity, str(pattern))
