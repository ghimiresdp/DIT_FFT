# __________________________________________________
# # 8 Point DIT-FFT Example
# __________________________________________________

import cmath
import matplotlib.pyplot as plt

sin = cmath.sin
cos = cmath.cos
pi = cmath.pi
exp = cmath.exp

disc = [0, 1, 2, 3, 4, 5, 6, 7]

# __________________________________________________
# Input Values
# __________________________________________________

x0 = [complex(1, 0),
      complex(1, 0),
      complex(3, 0),
      complex(1, 0),
      complex(-1, 0),
      complex(2, 0),
      complex(0, 0),
      complex(0, 0)]
# __________________________________________________
# Default Zero Initialization
# __________________________________________________

x = [complex(0, 0),
     complex(0, 0),
     complex(0, 0),
     complex(0, 0),
     complex(0, 0),
     complex(0, 0),
     complex(0, 0),
     complex(0, 0)]

x1 = x.copy()
x2 = x.copy()
x3 = x.copy()
# __________________________________________________
#  Finding out the twiddle Factor
# __________________________________________________

w = exp(-complex(0, 1) * 2 * pi / 8)
w0 = w ** 0
w1 = w
w2 = w * w
w3 = w1 * w2

# __________________________________________________
#  Stage 1
# __________________________________________________
"""
Splitting up the given data:

{0,1,2,3,4,5,6,7}

{odd_occurence}, {even_occurence}     
{0,2,4,6}, {1,3,5,7}

{ {odd_occurence}, {even_occurence}},   {{odd_occurence}, {even_occurence}} 
{{0,4}, {2,6}},   {{1,5}, {3,7}}

To be more clear, please look for the butterfly structure of The DIT-FFT
"""

x1[0] = x0[0] + x0[4]
x1[1] = x0[0] - x0[4]

x1[2] = x0[2] + x0[6]
x1[3] = x0[2] - x0[6]

x1[4] = x0[1] + x0[5]
x1[5] = x0[1] - x0[5]

x1[6] = x0[3] + x0[7]
x1[7] = x0[3] - x0[7]

# __________________________________________________
#  Stage 2
# __________________________________________________

x2[0] = x1[0] + w0 * x1[2]
x2[1] = x1[1] + w2 * x1[3]
x2[2] = x1[0] - w0 * x1[2]
x2[3] = x1[1] - w2 * x1[3]

x2[4] = x1[4] + w0 * x1[6]
x2[5] = x1[5] + w2 * x1[7]
x2[6] = x1[4] - w0 * x1[6]
x2[7] = x1[5] - w2 * x1[7]

# __________________________________________________
#  Stage 3
# __________________________________________________
x3[0] = x2[0] + w0 * x2[4]
x3[1] = x2[1] + w1 * x2[5]
x3[2] = x2[2] + w2 * x2[6]
x3[3] = x2[3] + w3 * x2[7]
x3[4] = x2[0] - w0 * x2[4]
x3[5] = x2[1] - w1 * x2[5]
x3[6] = x2[2] - w2 * x2[6]
x3[7] = x2[3] - w3 * x2[7]

# __________________________________________________
#  Printing out the result
# __________________________________________________
print(x0)
print(x3)

plt.subplot(2, 1, 1)
plt.plot(disc, [0, 0, 0, 0, 0, 0, 0, 0], color='black')  # Just for Reference
plt.plot(disc, x0, 'bo')
plt.tight_layout()
plt.xlabel('time[n]')
plt.ylabel('Value x[n]')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(disc, [0, 0, 0, 0, 0, 0, 0, 0], color='black')  # Just for Reference
plt.plot(disc, x3, 'ro')
plt.tight_layout()
plt.xlabel('time[n]')
plt.ylabel('Value X(n)')
plt.grid()
plt.show()
