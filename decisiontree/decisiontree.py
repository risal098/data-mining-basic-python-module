from sklearn.tree import DecisionTreeClassifier, plot_tree
import pandas as pd
import matplotlib.pyplot as mplt
file = 'contoh.xlsx'
sheet = pd.read_excel(file, sheet_name =1)
#observasi	income	ukuran lot	pemilik atau bukan
income=list(sheet["income"])
ukuran_lot=list(sheet["ukuran lot"])
pemilik=list(sheet["pemilik atau bukan"])
data={
	"income $1000":income,
	"ukuran lot(1000 ft)":ukuran_lot,
	"pemilik atau bukan":pemilik
}
df = pd.DataFrame(data)
features=["income $1000","ukuran lot(1000 ft)"]
dependent=df[features]
independent=df["pemilik atau bukan"]
decTree=DecisionTreeClassifier()
decTree.fit(dependent,independent)
mplt.figure(figsize=(10,6))
plot_tree(decTree,feature_names=features,class_names=["bukan pemilk","pemilik"],filled=True,rounded=True)
mplt.title("soal nomer 2")
mplt.show()
