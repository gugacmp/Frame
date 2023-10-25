import pandas as pd
import numpy as np

#series = pd.Series([7, 4,2 np.nan, 6,9])
#series = pd.Series([7, 4,2, np.nan, 6,9])

#print(type(series))

datas = pd.date_range('20230601', periods=4, freq= 'M')
datas2 = pd.date_range('20231024', periods=4, freq= 'D')
#print(datas)

#df = pd.DataFrame(np.random.randn(10,4), index = datas, columns = list("ABCD")) #list({'VALOR', 'CUSTO', 'MEDIA', 'TOTAL'})

#DATAFRAMEPORDICIONARIO

df2 = pd.DataFrame({"COD":range(4),
                    #"DATA":pd.Timestamp('20231024'),
                    "COMPRA":datas,
                    "PONTOS":pd.Series(1, index=list(range(4)), dtype='float32'),
                    "QNT":np.array([3]*4, dtype='int32'),
                    "TIPO":pd.Categorical(['COMPRA','VENDA', 'COMPRA', 'DEVOLUÇÃO']),
                    "LOJA":'XBOXONE',
                    "VENDA":datas2
                    })

print(df2)