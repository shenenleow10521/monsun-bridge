"""Check one possible reading of the pilot gate "At least 43 of 100 placed".

Hypothesis (to confirm with the team): 43 is the smallest count, out of 100 pilot
participants, whose one-sided 95% Wilson lower bound exceeds the services-and-sales
break-even placement rate. Inputs are the figures published in web.html section 07 and
dashboard.html (WageAnchor table and the default cost settings). Standard library only.
"""
from math import sqrt
from statistics import NormalDist

N = 100
Z = NormalDist().inv_cdf(0.95)  # one-sided 95%

# Default scenario: (1 x 1,100 + 2 x 1,100 x 0.60) x 1.10 = RM 2,662 per participant, over 3 months.
cost_per_participant = (1 * 1100 + 2 * 1100 * 0.60) * 1.10
cost_per_worker_month = cost_per_participant / 3
wages = {"Clerical support": 2931, "Services and sales": 2561, "Craft and trades": 2510}


def wilson_lower(k, n, z=Z):
    p = k / n
    centre = p + z * z / (2 * n)
    margin = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (centre - margin) / (1 + z * z / n)


print("cost per participant RM %.0f, per worker-month RM %.2f, z = %.4f" % (cost_per_participant, cost_per_worker_month, Z))
for group, wage in wages.items():
    rate = cost_per_worker_month / wage
    k = next(k for k in range(N + 1) if wilson_lower(k, N) > rate)
    print("%-18s break-even %.1f%%  smallest k with Wilson lower bound above it: %d (lower bound %.4f; k-1 gives %.4f)"
          % (group, 100 * rate, k, wilson_lower(k, N), wilson_lower(k - 1, N)))
