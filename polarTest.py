import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import numpy as np
from math import pi

#xs = np.linspace(0,360,5)
#xs = xs * (pi/180)
xs = [0, pi/2, pi, 3*pi/2, 2*pi]
#ys = np.linspace(1,1,5)
ys = [1, 2, 3, 4, 5]

fig = plt.figure(figsize=(5,10)) #width, height
ax = plt.subplot(1, 1, 1, projection='polar')

trans_offset = mtransforms.offset_copy(ax.transData, fig=fig, y=6, units='dots')

for x, y, in zip(xs, ys):
	plt.polar(x, y, 'ro')
	plt.text(x, y, '%d, %d' % (int(x), int(y)),
		transform=trans_offset,
		horizontalalignment='center',
		verticalalignment='bottom')

plt.show()