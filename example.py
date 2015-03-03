from domecalc import DomeCalc

# create DomeCalc object: 
# -> A 2V dome, 
# -> radius=2330mm, 
# -> adjustment=-80mm, maste
calc = DomeCalc(
	preset=DomeCalc.preset_2V, 
	radius=2330, 
	adjust=-80, 
	master=6000
)

calc.solve()
print "Number of lengths:", calc.obj
print "solution makeup"
