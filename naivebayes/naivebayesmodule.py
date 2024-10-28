
import math

#untuk mendapatkan list yang berisi unique value (hanya boleh 1 item each)
def getUniqueValues(column):
	return list(set(column))
	
	
#untuk menghitung probabilitas suatu item terhadap total item
def pAtotal(item,column): 
	countItem=column.count(item)
	totalItem=len(column)
	return countItem/totalItem
	
	
	
#untuk menghitung probabilitas item A terhadap B
def pAB(itemA,itemB):
	return itemA/itemB

#untuk menghitung total B pada A
def findTotalAB(A,listA,B,listB):
	indeks=0
	result=0
	for a in listA:
		if a==A and listB[indeks]==B:
			result+=1
		indeks+=1
	return result
			
#siapkan dict untuk menyimpan probabilitas tiap kolom dependent
"""
dictProb=
{
 itemA=
 				{
 					itemYA=nbm.pAB atau itemA/itemYA
 					itemYB=nbm.pAB atau itemA/itemYB
 				},
 itemB=
 				{
 					itemYA=nbm.pAB atau itemB/itemYA
 					itemYB=nbm.pAB atau itemB/itemYB
 				},
 ....	
}
"""
def dictProbXGen(uniqueSetX,uniqueSetY,Xlist,Ylist):
	dictProb={}
	for i in uniqueSetX:
		dictProb[i]={}
		for ii in uniqueSetY:
			dictProb[i][ii]=pAB(findTotalAB(i,Xlist,ii,Ylist),Ylist.count(ii))
	return dictProb
	
	
#siapkan probabilitas dari unique value item dependent dari total item
"""
dictProb=
{
	itemA=itemA/totalAB,
	itemB=itemB/totalAB,
	...
}

"""
def dictProbYGen(uniqueSetY,Ylist):
	dictProbY={}
	for i in uniqueSetY:
		dictProbY[i]=pAtotal(i,Ylist)
	return dictProbY
	


