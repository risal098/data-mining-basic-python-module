#"original made by risal"
#"contributor=[risalah qz,]"

import naivebayesmodule as nbm
import pandas as pd
import math




#load file anda, pastikan 1 folder ygy
file = 'contoh.xlsx'
sheet1 = pd.read_excel(file, sheet_name = 0)

#masukkan variable Xn list  disini sesuai kolom yg ada  (ubah argumentnya)| (ubah variablenya)
warna=list(sheet1["warna"])
tipe=list(sheet1["tipe"])
asal=list(sheet1["asal"])

#masukkan variable Yn list disini sesuai kolom yg ada (ubah argumentnya)| (ubah variablenya)
terlaris=list(sheet1["terlaris"])

#dapatkan value unique dari tiap column value disini (ubah argumentnya)| (ubah variablenya)
uniqueSetWarna=nbm.getUniqueValues(warna)
uniqueSetTipe=nbm.getUniqueValues(tipe)
uniqueSetAsal=nbm.getUniqueValues(asal)
uniqueSetTerlaris=nbm.getUniqueValues(terlaris)
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
dictProbTerlaris=nbm.dictProbYGen(uniqueSetTerlaris,terlaris)




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
print(warna.count("kuning"),terlaris.count("ya"))
print("end debug")
dictProbWarna=nbm.dictProbXGen(uniqueSetWarna,uniqueSetTerlaris,warna,terlaris)	
dictProbTipe=nbm.dictProbXGen(uniqueSetTipe,uniqueSetTerlaris,tipe,terlaris)
dictProbAsal=nbm.dictProbXGen(uniqueSetAsal,uniqueSetTerlaris,asal,terlaris)
print(dictProbTerlaris)
print(dictProbWarna)
print(dictProbTipe)
print(dictProbAsal)

target=["kuning","suv","domestik"]
for i in dictProbTerlaris:
	Twarna=dictProbWarna["kuning"][i]
	Ttipe=dictProbTipe["suv"][i]
	Tasal=dictProbAsal["domestik"][i]
	print(i,"=",dictProbTerlaris[i]*Twarna*Ttipe*Tasal)











