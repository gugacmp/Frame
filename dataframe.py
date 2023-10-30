import pandas as pd
import numpy as np
import random
#series = pd.Series([7, 4,2 np.nan, 6,9])
#series = pd.Series([7, 4,2, np.nan, 6,9])

#print(type(series))

datas = pd.date_range('20230605', periods=4, freq= 'M')
datas2 = pd.date_range('20231024', periods=4, freq= 'D')
#print(datas)

#df = pd.DataFrame(np.random.randn(10,4), index = datas, columns = list("ABCD")) #list({'VALOR', 'CUSTO', 'MEDIA', 'TOTAL'})

#DATAFRAMEPORDICIONARIO

df2 = pd.DataFrame({" CODIGO":range(4),
                    #"DATA":pd.Timestamp('20231024'),
                    "COMPRA":datas,
                    "PARCELAS":pd.Series(random.randint(2, 8) , index=list(range(4)), dtype='float32'),
                    "QNT":np.array([3]*4, dtype='int32'),
                    "PAGAMENTO":pd.Categorical(['PIX','CREDITO', 'CREDITO', 'PIX']),
                    "LOJA":'VEST PE CALÇADOS',
                    "VENDA":datas2,
                    "TOTAL" : pd.Series(random.randint(2,8) * np.array([3]*4)),
                    })

df3 = pd.DataFrame({" CODIGO":range(4),
                    #"DATA":pd.Timestamp('20231024'),
                    "COMPRA":datas,
                    "PARCELAS":pd.Series(random.randint(3, 9) , index=list(range(4)), dtype='float32'),
                    "QNT":np.array([3]*4, dtype='int32'),
                    "PAGAMENTO":pd.Categorical(['PIX','CREDITO', 'CREDITO', 'PIX']),
                    "LOJA":'VEST PE CALÇADOS',
                    "VENDA":datas2,
                    "TOTAL" : pd.Series(random.randint(2,8) * np.array([3]*4)),
                    })

df4 = pd.DataFrame({" CODIGO":range(4),
                    #"DATA":pd.Timestamp('20231024'),
                    "COMPRA":datas,
                    "PARCELAS":pd.Series(random.randint(1, 1) , index=list(range(4)), dtype='float32'),
                    "QNT":np.array([3]*4, dtype='int32'),
                    "PAGAMENTO":pd.Categorical(['DEBITO','DEBITO', 'DEBITO', 'PIX']),
                    "LOJA":'VEST PE CALÇADOS',
                    "VENDA":datas2,
                    "TOTAL" : pd.Series(random.randint(8,16) * np.array([3]*4)),
                    })

df5 = pd.DataFrame({" CODIGO":range(4),
                    #"DATA":pd.Timestamp('20231024'),
                    "COMPRA":datas,
                    "PARCELAS":pd.Series(random.randint(2, 8) , index=list(range(4)), dtype='float32'),
                    "QNT":np.array([3]*4, dtype='int32'),
                    "PAGAMENTO":pd.Categorical(['PIX','CREDITO', 'CREDITO', 'PIX']),
                    "LOJA":'VEST PE CALÇADOS',
                    "VENDA":datas2,
                    "TOTAL" : pd.Series(random.randint(2,8) * np.array([3]*4)),
                    })

#print(df2)

grupo = pd.concat([df2, df3])
grupo2 = pd.concat([df4, df5])

juntar = pd.concat([grupo, grupo2])

print(juntar.describe())
#print(juntar.T)
