###
import pandas as pd
import numpy as np



df = pd.DataFrame(np.random.rand(10, 5))
df['mean'] = df.mean(1)
print(df)
print('\n\n')
df = df[list(('mean',0,'mean' , 2,3,4))]
print(df)
