#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Produce a custom twist drill plot'''

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)

# set some rcParams
mpl.rcParams['font.weight'] = 'bold'

mpl.rcParams['xtick.major.pad'] = 10
mpl.rcParams['xtick.direction'] = 'inout'
mpl.rcParams['xtick.labelsize'] = 26

mpl.rcParams['ytick.direction'] = 'inout'
mpl.rcParams['ytick.labelsize'] = 20

# define the constants for our chart
materials = [
             ('Acrylic'    , 650 , 'c'          , '-' ) ,
             ('Aluminum'   , 300 , 'b'          , '-' ) ,
             ('Brass'      , 200 , 'g'          , '-' ) ,
             ('LC Steel'   , 110 , 'k'          , '-' ) ,
             ('Wood'       , 100 , 'brown'      , '-' ) ,
             ('MC Steel'   , 80  , 'darkgray'   , '-' ) ,
             ('HC Steel'   , 60  , 'lightgray'  , '-' ) ,
             ('Stainless'  , 50  , 'purple'     , '-' ) ,
             ]
drill_speeds = [250, 340, 390, 510, 600, 650, 990, 1550, 1620, 1900, 2620, 3100] #rpm

speed_lims = (200., 4000.) # rpm

max_in = 1. # in.
incr = 1./16. # in.

im_sz = 25. # in.
ratio = 8.5/11.

fig = plt.figure(figsize=(im_sz,ratio * im_sz), dpi=600)
fig.patch.set_alpha(0)

# generate a vector of drill bit diameter
x = np.array([float(i) * incr for i in range(1,int(max_in/incr) + 1)]) # in.

# calculate the drill speed curve for each material type and plot the curve
for name, speed, color, linestyle in materials:
    plt.loglog(x, 12/np.pi/x*speed, label=name, linewidth=5, color=color, linestyle=linestyle)

ax = plt.gca()

# adjust the axis tick locators to match drill press speeds
ax.yaxis.set_major_locator(mpl.ticker.FixedLocator(drill_speeds))
ax.yaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%4d'))
ax.yaxis.set_minor_locator(mpl.ticker.NullLocator())
ax.set_ylim(speed_lims)

# set the drill diameter locators and format the ticks with LaTeX
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(base=incr))
ax.xaxis.set_minor_locator(mpl.ticker.NullLocator())
ax.set_xlim((incr, max_in))
ticks = ['0', r'$$\frac{1}{16}$$'  , r'$$\frac{1}{8}$$'  , r'$$\frac{3}{16}$$'  , r'$$\frac{1}{4}$$' ,
              r'$$\frac{5}{16}$$'  , r'$$\frac{3}{8}$$'  , r'$$\frac{7}{16}$$'  , r'$$\frac{1}{2}$$' ,
              r'$$\frac{9}{16}$$'  , r'$$\frac{5}{8}$$'  , r'$$\frac{11}{16}$$' , r'$$\frac{3}{4}$$' ,
              r'$$\frac{13}{16}$$' , r'$$\frac{7}{8}$$'  , r'$$\frac{15}{16}$$' , r'$$1$$'     ]
ax.xaxis.set_ticklabels(ticks)

# Add the Texts
plt.xlabel('Bit Diameter (in.)', fontsize=26)
plt.ylabel('Drill Speed (rpm)' , fontsize=26)
plt.title('Twist Drill Speeds' , fontsize=50)
plt.legend(ncol=2, loc=3, fontsize=40)

plt.grid('on')
plt.savefig('drill_speed_chart.png')

