#"original made by risal"
#"contributor=[risalah qz,]"

import naivebayesmodule as nbm
import pandas as pd
import math




#load file anda, pastikan 1 folder ygy
file = 'contoh.xlsx'
sheet1 = pd.read_excel(file, sheet_name = 0)

#masukkan variable Xn list  disini sesuai kolom yg ada  (ubah argumentnya)| (ubah variablenya)
x1=list(sheet1["x1"])
x2=list(sheet1["x2"])
x3=list(sheet1["x3"])

#masukkan variable Yn list disini sesuai kolom yg ada (ubah argumentnya)| (ubah variablenya)
classy=list(sheet1["class"])

#dapatkan value unique dari tiap column value disini (ubah argumentnya)| (ubah variablenya)
uniqueSetX1=nbm.getUniqueValues(x1)
uniqueSetX2=nbm.getUniqueValues(x2)
uniqueSetX3=nbm.getUniqueValues(x3)
uniqueSetClassy=nbm.getUniqueValues(classy)
#print(uniqueSetTerlaris)

#siapkan probabilitas dari unique value item dependent dari total item
"""
dictProb=
{
	itemA=itemA/totalAB,
	itemB=itemB/totalAB,
	...
}

"""
dictProbClassy=nbm.dictProbYGen(uniqueSetClassy,classy)




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
print("debug")
#print(warna.count("kuning"),terlaris.count("ya"))
print("end debug")
dictProbX1=nbm.dictProbXGen(uniqueSetX1,uniqueSetClassy,x1,classy)	
dictProbX2=nbm.dictProbXGen(uniqueSetX2,uniqueSetClassy,x2,classy)
dictProbX3=nbm.dictProbXGen(uniqueSetX3,uniqueSetClassy,x3,classy)
print(dictProbClassy)
print(dictProbX1)
print(dictProbX2)
print(dictProbX3)

target=["no","married",120]
for i in dictProbClassy:
	TX1=dictProbX1["no"][i]
	TX2=dictProbX2["married"][i]
	TX3=dictProbX3[120][i]
	print(i,"=",dictProbClassy[i]*TX1*TX2*TX3)











