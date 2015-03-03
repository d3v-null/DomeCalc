from domecalc import DomeCalc	

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
