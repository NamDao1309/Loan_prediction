#Bai 4

import pandas as pd
import numpy as np
df = pd.read_excel('E:\coalpublic2013.xlsx')    
df[df["Labor_Hours"] > 20000].head()


#Bai 5
import pandas as pd
import numpy as np
df = pd.read_excel('E:\coalpublic2013.xlsx')
print("Sum: ",df["Production"].sum()) 
print("Mean: ",df["Production"].mean())
print("Maximum: ",df["Production"].max())
print("Minimum: ",df["Production"].min()) 


#Bai 6
import pandas as pd
import numpy as np
df = pd.read_excel('E:\coalpublic2013.xlsx')    
df[df["Mine_Name"].map(lambda x: x.startswith('P'))].head()


#Bai 7

import pandas as pd
import numpy as np
df = pd.read_excel('E:\coalpublic2013.xlsx')    
df.query('Mine_Name == ["Shoal Creek Mine", "Piney Woods Preparation Plant"]').head()


import pandas as pd
import numpy as np
df = pd.read_excel('E:\employee.xlsx')
df[df['hire_date'] >='20070101']

#Bai 9
import pandas as pd
import numpy as np
df = pd.read_excel('E:\employee.xlsx')
result = df[(df['hire_date'] >='Jan-2005') & (df['hire_date'] <= 'Dec-2006')].head()
result

#Bai 10

import pandas as pd
import numpy as np
df = pd.read_excel('E:\employee.xlsx')
df2 = df.set_index(['hire_date'])
result = df2["2005"]
result