
import pandas as pd
df = pd.DataFrame({
    'subject': ['physics','chemistry','biology','math'],
    'Status': ['pass', 'pass', 'pass', 'pass'],
    'mark': [7.5, 8.5, 8.9, 9.3],
})

print (df)

#by lambda funct
df['percentage'] = df['mark'].apply(lambda x: (100 * x)/10)
print(df)

    