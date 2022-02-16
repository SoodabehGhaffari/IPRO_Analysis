
f = open('ucd_revert_ReportFinal.txt')
fw = open('ucd_revert_Trajectory.txt','a')
f_contents=f.readlines()
totalnum=len(f_contents)
my_dic={}
InteractionList=[]
count=0
for i in range(len(f_contents)):
	string=f_contents[i]
	if ":" in string:
		num1=int(string.index(']:'))
		InteractionEnergy = (string[num1+3:]).split(",")[0]
		my_dic.update({i: InteractionEnergy})
		InteractionList.append(InteractionEnergy)
InteractionList.sort(reverse=False)
lowest=InteractionList[0:10]
#print(lowest)
for i in range(len(lowest)):
	path=[]
	for number, interaction in my_dic.items():
		if interaction==lowest[i]:
			numberline=number

	FirstNumber=f_contents[numberline].split('->')[1].index("[")
	path.append(f_contents[numberline].split('->')[1][:FirstNumber])
	path.append(f_contents[numberline].split('->')[0])
	# print(path)
	while path[-1]!="initial":
		for element in f_contents:
			if 'initial calculations' not in element:
				newString=element.split('->')[1]
				SecondNumber=newString.index("[")
				SecondElement=newString[:SecondNumber]
				if SecondElement==str(path[-1]):
					FirstElement=element.split("->")[0]
					path.append(FirstElement)
					

	print(path)			
					

	fw.write('\n\n')
	for j in range(len(path)):
		fw.write(path[j])
		if path[j]!="initial":
			fw.write(' <- ')
			

