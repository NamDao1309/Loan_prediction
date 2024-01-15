from numpy import asarray
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder

# define data
data = asarray([['red'], ['green'], ['blue'],['yellow']])
print(data)

# define ordinal encoding
encoder = OrdinalEncoder()
encoder_onehot = OneHotEncoder(sparse=False)
encoder_dummy = OneHotEncoder(drop='first', sparse=False)

# transform data
# result = encoder.fit_transform(data)
# print(result)

result_onehot = encoder_onehot.fit_transform(data)
print(result_onehot)

result_dummy = encoder_dummy.fit_transform(data)
print(result_dummy)