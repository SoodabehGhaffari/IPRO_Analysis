f=open('copy_ucd_revert_mustard_reject_IPRO_Summary.txt', "r")
fw=open("ucd_revert_ReportFinal.txt","a")
#file_content = f.readlines()
paragraphs = f.read().split("\n\n")
#print(file_content[32])
#print(len(paragraphs))
counter=0

for i in range(len(paragraphs)):
	newMutant=[]
#for i in range(2999,3000):
	lines=paragraphs[i].split('\n')
	if i==0:
		line1=lines[2]
		b = line1[39:]
		b = b.replace("kcal / mol","")
		ComplexEnergy=b
		line2=lines[3]
		c=line2[43:]
		c= c.replace("kcal / mol","")
		InteractionEnergy=c
		fw.write('initial calculations')
		fw.write(str(InteractionEnergy))
		fw.write(str(ComplexEnergy))
		fw.write('\n')
		#print('initial calculations',ComplexEnergy,InteractionEnergy)			
	else:		

		for line in lines:
			if "The Complex Energy of Design Group 1 is" in line:
				b = line[39:]
				b = b.replace("kcal / mol","")
				ComplexEnergy=b
			if "The Interaction Energy of Design Group 1 is" in line:
				c=line[43:]
				c= c.replace("kcal / mol","")
				InteractionEnergy=c
			if 'Iteration' in line:
				IterationNum=line.index('Iteration')
				newIteration=line[IterationNum+10:]
			if 'structures' in line:
				if 'initial structures' in line:
					oldIteration= 'initial'
				else:
					iterationNum=line.index('iteration')
					oldIteration=line[iterationNum+10:]
			if "A:" in line:
				newMutant.append(line[8:])
		print(oldIteration,'->',newIteration,newMutant,InteractionEnergy,ComplexEnergy)		
		fw.write(str(oldIteration))	
		fw.write('->')	
		fw.write(str(newIteration))
		fw.write(str(newMutant))
		fw.write(":")
		fw.write(str(InteractionEnergy))
		fw.write(',')
		fw.write(str(ComplexEnergy))
		fw.write('\n')