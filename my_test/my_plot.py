# Plot code
import numpy as np
import matplotlib.pyplot as plt

timings_cands = ['lambda', 'cb_nocomp', 'cb']
x_pos = np.arange(len(timings_cands))

means = []
errors = []
for cand in timings_cands:
    timings = []
    with open(f'{cand}.timing','r') as infile:
        for line in infile:
            timings.append(float(line.strip()))
    means.append(np.mean(timings))
    errors.append(np.std(timings)) 
    
fig, ax = plt.subplots()
ax.bar(x_pos, means, yerr=errors, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Time Taken (seconds)')
ax.set_xticks(x_pos)
ax.set_xticklabels(timings_cands)
ax.set_yscale('log')
ax.yaxis.grid(True)

# Save the figure and show
plt.tight_layout()
fig.set_size_inches(4, 3)
plt.savefig('my_expt.png',dpi=400)