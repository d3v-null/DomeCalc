from domecalc import DomeCalc	


import csv

with open('out6100.csv', 'w') as outFile:
	csvwriter = csv.writer(outFile)
	#write header
	csvwriter.writerow(['', '2V', '3VK4', '3VK5', '4V'])
	for i in range( 2000, 6500, 10 ):
		print i
		row = [i]
		for j in [DomeCalc.preset_2V, DomeCalc.preset_3VK4, DomeCalc.preset_3VK5, DomeCalc.preset_4V]:
			domecalc = DomeCalc(j, i, 40, 6100)
			domecalc.solve()
			row.append(domecalc.obj)
		csvwriter.writerow(row)		
with open('out6500.csv', 'w') as outFile:
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
