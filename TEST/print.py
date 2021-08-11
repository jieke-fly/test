from numpy.core.multiarray import packbits
from Print import Print
import numpy as np
import statistics
import os,sys

a = Print()
print(a)
b =([34,51,4],[5,2,7],[6,9,2])
print(b)
print('\n')
print('求均值',np.mean(b))
print('求中值',np.median(b))
print('\n')
print('排序\n',np.sort(b,1))
print('\n')
print('求矩阵大小',np.size(b))
print('求百分位数',np.percentile(np.sort(b),1))

print('\n')
os.mkdir('新建文件夹')
print("成功新建文件夹\n")

print("%s你好" % (a))
