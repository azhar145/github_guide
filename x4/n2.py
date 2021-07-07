import pandas as pd
import numpy as np
import pandas.io.formats.style
np.random.seed(24)
df = pd.DataFrame({'A': np.linspace(1, 10, 10)})
df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), columns=list('BCDE'))],
                       axis=1)
df.iloc[0, 2] = np.nan
print(df)
df.style.format("{:.2%}")
def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return 'color: %s' % color

s = df.style.applymap(color_negative_red)

s.style.setproperties(color="blue",align="right")

print(s)
