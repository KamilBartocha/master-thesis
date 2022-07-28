import numpy as np
import matplotlib.pyplot as plt

def error(b, e):
    """For every given parameters b and e, returns value from
    (4.15)"""
    return (1 / (b + 1)) ** e * (1 / (b + 1) + 1 / e)


values = np.array([[1/error(b, e_ * 0.1) for b in range(1, 100)]
                   for e_ in (1, 3, 5, 7, 9, 10)])


plt.loglog(values.T)
plt.plot([1, 10**2], [.095, .095 * 10**(2 * .1)], ls='--', c='black',
         label='theoretical slope = 1')
plt.plot([1, 10**2], [1, 1 * 10**(2 * 1)], ls='--', c='#24C6CD',
         label='theoretical slope = 0.2')
plt.legend([f'epsilon={0.1 * e_:.1f}' for e_ in (1, 3, 5, 7, 9, 10)]
           + ['theoretical slope = 0.1', 'theoretical slope =1'])
plt.xlabel("log(b)")
plt.ylabel("-log(error)")
plt.savefig('ex2_loglog_error.png', dpi=2000)
