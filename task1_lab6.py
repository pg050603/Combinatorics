from module_lab6 import *

ti_pw1, yi_pw1 = np.genfromtxt('PW1.dat', delimiter=',', skip_header=1).T
ti_pw2, yi_pw2 = np.genfromtxt('PW2.dat', delimiter=',', skip_header=1).T
ti_iw1, yi_iw1 = np.genfromtxt('IW1.dat', delimiter=',', skip_header=1).T

tj = np.arange(1980, 2014, 0.5)

# TODO - your code here
# Call interpolate_linear to interpolate data for IW1, PW1, & PW2
yj_iw1 = interpolate_linear(ti_iw1, yi_iw1, tj, default=0)
yj_pw1 = interpolate_linear(ti_pw1, yi_pw1, tj, default=0)
yj_pw2 = interpolate_linear(ti_pw2, yi_pw2, tj, default=0)

# Initialise net mass change list
net_mass_change = []

# Calculate the net mass change for each tj
# Convert kg/s to kg/year (factor of 3.154*10^6)
for i in range(len(yj_iw1)):
    change = (yj_iw1[i] - yj_pw1[i] - yj_pw2[i]) * (3.154 * 10 ** 6)
    net_mass_change.append(change)

# Initialise dictionary mapping for cumulative net mass change and time
cmc_tj_map = {tj[0]: 0.0}

# n - 1 intervals for times (tj) and corresponding net mass change elements to 2014.5
# Start shifted forward by 0.5year each cycle forward
# Associate the times and the relevant cumulative net mass change in dictionary mapping
for i in range(len(yj_iw1)):
    tj_NMC = tj[0:i + 2]
    yj_NMC = net_mass_change[0:i + 2]
    integral = integrate_composite_trapezoid(tj_NMC, yj_NMC)
    cmc_tj_map[tj_NMC[-1]] = integral

# From dict, get a list of years and a list of the cumulative net mass change corresponding to each year
Year = list(cmc_tj_map.keys())
Cumulative_mass_change = list(cmc_tj_map.values())
# Create figure
plt.figure(figsize=(5, 2.7), layout='constrained')
# Plot the cumulative net mass change against year
plt.plot(Year, Cumulative_mass_change, label='Cumulative Net Mass Change')
# Plot the earthquakes onto chart
earthquakes = [2003.5, 2004.5, 2005]
for p in earthquakes:
    plt.axvline(p,  label=f'Earthquake {p}', color='red')
# Axis labels, title, and legend
plt.xlabel('Year')
plt.ylabel('Cumulative Net Mass Change (kg)')
plt.title("Yearly Cumulative Net Mass Change (1980 - 2014.5)")
plt.legend()
plt.show()
