from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import std
from numpy import percentile

# generate the random number 
seed(1)

# data is generate
data = 5 * randn(10000) + 50

# # calculate summary statics
# data_mean, data_std = mean(data), std(data)

# # define outliers data la 3*STD
# cut_off = data_std * 3
# lower,upper = data_mean - cut_off, data_mean + cut_off

# #identify outliers
# outliers = [x for x in data if x < lower or x > upper]
# print("Outlier data is : %d" % len(outliers))

# # removed  outliers
# outliers_removed = [x for x in data if x >=lower and x <= upper]
# print(' Non-outliers data : %d' % len(outliers_removed))


# XÁC ĐỊNH OUTLIE DATA BẰNG TỨ PHÂN VỊ
# calculate inter-quartile range
Q1, Q3 = percentile(data, 25), percentile(data, 75)
iqr = Q3 - Q1
print("Interquartile : Q1 = %.3f, Q3 = %.3f, IQR = %.3f" % (Q1, Q3, iqr))

# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = Q1 - cut_off, Q3 + cut_off
# identify outliers
outliers = [x for x in data if x < lower or x > upper]
print("Outlier data : %d" % len(outliers))
# remove outliers
outliers_removed = [x for x in data if x >= lower and x <= upper]
print("Non-outlier : %d " % len(outliers_removed))