import numpy as np
import matplotlib.pyplot as plt


def sum_up_b(b):
    return sum(1 / i**2 for i in range(1, b+1))


error = [np.pi**2 / 6 - sum_up_b(b) for b in range(1, 100)]

x = list(range(1, 100))

plt.xlabel("log(b)")
plt.ylabel('-log(error)')
plt.plot(np.log(x), -np.log(error), label='error')
plt.plot([0, 5], [0, 5], c='red', ls='--', label='theoretical slope = 1')
plt.legend()
plt.savefig('ex1_loglog_error.png', dpi=2000)
