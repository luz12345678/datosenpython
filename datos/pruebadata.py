import pandas as pd
#crear un dataframe
data ={'nombre':['Ana', 'Luis', 'Carlos', 'Luz', 'Jose Luis'], 'Edad': [23, 34, 15, 37, 14]}
df=pd.DataFrame(data)
#print(df)

import pandas as pd
df= pd.read_csv("datos/poblacion.csv")
print(df["COL"])
#print(df. describe())
#print(df.tall())
#print(df.sample())

filtro= df[df['COL']>30]
print(filtro["COL"])

#eliminar una columna
df = df.drop(columns=['paisangentina'])
print(df)