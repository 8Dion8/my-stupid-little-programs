import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

scores_ = [20,10,9,8,4,12]
max_scores = [32,12,11,8,4,12]
scores = [scores_[i]/max_scores[i] for i in range(len(scores_))]

plt.plot(scores)

print('\n\n\n\n')
print("Mean:", np.mean(scores))
print("Mode:", stats.mode(scores)[0][0])
print('Median:', np.median(scores))
print('Range:',max(scores)-min(scores))
print('\n\n\n\n')

plt.show()