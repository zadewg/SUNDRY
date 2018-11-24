#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np


nox_df = pd.read_csv('AEI_OTHER_28102018185121363.csv')
hdi_df = pd.read_csv('HDI2.csv')

nox_df = nox_df[nox_df.INDICATOR == 'NOX'] # Eliminar informacion irreleante.
nox_df['Value'] = nox_df['Value'].astype('int64') # Suprimir notacion cientifica para hacerlo mas legible.
nox_df = nox_df[['Country','Time','Value']]



# Encontrar colisiones de paises.

nox_df_PList = nox_df['Country'].tolist()
hdi_df_PList = hdi_df['Country'].tolist()

Pmatches = list(set(nox_df_PList) & set(hdi_df_PList))

hdi_df = hdi_df.loc[hdi_df['Country'].isin(Pmatches)]
nox_df = nox_df.loc[nox_df['Country'].isin(Pmatches)].reset_index(drop=True)



# Juntar bases de datos

blacklist = ['HDI Rank (2017)', '2015', '2016', '2017', 'United States', 'United Kingdom']
df2 = hdi_df
df2 = pd.melt(df2, id_vars=["Country"], var_name="Time", value_name="HDI")
df2 = (df2.sort_values(["Country", "Time"]))
hdi_df = df2[~df2.Time.isin(blacklist)].reset_index(drop=True)
nox_df = nox_df.sort_values(["Country", "Time"])


DATABASE = pd.DataFrame()
DATABASE['COUNTRY'] = hdi_df['Country']
DATABASE['TIME'] = hdi_df['Time']
DATABASE['HDI'] = hdi_df['HDI']
DATABASE['NOX'] = nox_df['Value']
DATABASE = DATABASE[~DATABASE.COUNTRY.isin(blacklist)].reset_index(drop=True)


countries = list(OrderedDict.fromkeys(DATABASE['COUNTRY']))
print(countries, len(countries))
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
	#print(DATABASE)
	pass


""" #Codigo utilizado para identificar errores.
POOR =  ['Bulgaria', 'Cyprus', 'Estonia', 'Poland', 'Portugal', 'Romania', 'Slovenia', 'Spain', 'Turkey', 'Greece', 'Ireland']

RICH = ['Austria','Canada', 'Netherlands', 'Sweden', 'Switzerland',  'Finland', 'France', 'Germany', 'Iceland', 'Israel', 'Luxembourg']

#YEARS = ['2002','2003']

WL = ['Austria', 'Bulgaria', 'Canada', 'Cyprus', 'Estonia',  'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Finland', 'France', 'Germany', 'Greece', 'Iceland', 'Ireland', 'Israel', 'Luxembourg'] #22		#'Mexico', 'Hungary', 'Malta', 'Croatia',  'Latvia', 'Lithuania',            'Finland', 'France', 'Germany', 'Greece', 'Iceland', 'Ireland', 'Israel', 'Italy', 'Latvia',  'Luxembourg', (~ 'Italy', 'Latvia',)           'Chile', 'Belgium',


DATABASE = DATABASE[DATABASE.COUNTRY.isin(WL)]
P_DB = DATABASE[DATABASE.TIME.isin(YEARS)]
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(P_DB)


#DATABASE  = DATABASE[DATABASE.COUNTRY.isin(RICH)]
"""


POOR =  ['Bulgaria', 'Cyprus', 'Estonia', 'Poland', 'Portugal', 'Romania', 'Slovenia', 'Spain', 'Turkey', 'Greece', 'Ireland']

RICH = ['Austria','Canada', 'Netherlands', 'Sweden', 'Switzerland',  'Finland', 'France', 'Germany', 'Iceland', 'Israel', 'Luxembourg']

YEARS = ['2002','2003']

WL = ['Austria', 'Bulgaria', 'Cyprus', 'Estonia',  'Netherlands', 'Poland', 'Portugal', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Finland', 'France', 'Germany', 'Greece', 'Iceland', 'Ireland', 'Luxembourg'] #22		#'Mexico', 'Hungary', 'Malta', 'Croatia',  'Latvia', 'Lithuania',            'Finland', 'France', 'Germany', 'Greece', 'Iceland', 'Ireland', 'Israel', 'Italy', 'Latvia',  'Luxembourg', (~ 'Italy', 'Latvia',)           'Chile', 'Belgium',


DATABASE = DATABASE[DATABASE.COUNTRY.isin(WL)]
P_DB = DATABASE[DATABASE.TIME.isin(YEARS)]
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
     print(DATABASE)
#    print(P_DB)


print(DATABASE['NOX'].min())
#DATABASE  = DATABASE[DATABASE.COUNTRY.isin(RICH)]


# Calcular medias
A90 = list(DATABASE[DATABASE.TIME == '1990'].mean().astype('int64'))
A91 = list(DATABASE[DATABASE.TIME == '1991'].mean().astype('int64'))
A92 = list(DATABASE[DATABASE.TIME == '1992'].mean().astype('int64'))
A93 = list(DATABASE[DATABASE.TIME == '1993'].mean().astype('int64'))
A94 = list(DATABASE[DATABASE.TIME == '1994'].mean().astype('int64'))
A95 = list(DATABASE[DATABASE.TIME == '1995'].mean().astype('int64'))
A96 = list(DATABASE[DATABASE.TIME == '1996'].mean().astype('int64'))
A97 = list(DATABASE[DATABASE.TIME == '1997'].mean().astype('int64'))
A98 = list(DATABASE[DATABASE.TIME == '1998'].mean().astype('int64'))
A99 = list(DATABASE[DATABASE.TIME == '1999'].mean().astype('int64'))
A00 = list(DATABASE[DATABASE.TIME == '2000'].mean().astype('int64'))
A01 = list(DATABASE[DATABASE.TIME == '2001'].mean().astype('int64'))
A02 = list(DATABASE[DATABASE.TIME == '2002'].mean().astype('int64'))
A03 = list(DATABASE[DATABASE.TIME == '2003'].mean().astype('int64'))
A04 = list(DATABASE[DATABASE.TIME == '2004'].mean().astype('int64'))
A05 = list(DATABASE[DATABASE.TIME == '2005'].mean().astype('int64'))
A06 = list(DATABASE[DATABASE.TIME == '2006'].mean().astype('int64'))
A07 = list(DATABASE[DATABASE.TIME == '2007'].mean().astype('int64'))
A08 = list(DATABASE[DATABASE.TIME == '2008'].mean().astype('int64'))
A09 = list(DATABASE[DATABASE.TIME == '2009'].mean().astype('int64'))
A10 = list(DATABASE[DATABASE.TIME == '2010'].mean().astype('int64'))
A11 = list(DATABASE[DATABASE.TIME == '2011'].mean().astype('int64'))
A12 = list(DATABASE[DATABASE.TIME == '2012'].mean().astype('int64'))
A13 = list(DATABASE[DATABASE.TIME == '2013'].mean().astype('int64'))
A14 = list(DATABASE[DATABASE.TIME == '2014'].mean().astype('int64'))

HDI = [A90[0], A91[0], A92[0], A93[0], A94[0], A95[0], A96[0], A97[0], A98[0], A99[0], A00[0], A01[0], A02[0], A03[0], A04[0], A05[0], A06[0], A07[0], A08[0], A09[0], A10[0], A11[0], A12[0], A13[0], A14[0]]
NOX = [A90[1], A91[1], A92[1], A93[1], A94[1], A95[1], A96[1], A97[1], A98[1], A99[1], A00[1], A01[1], A02[1], A03[1], A04[1], A05[1], A06[1], A07[1], A08[1], A09[1], A10[1], A11[1], A12[1], A13[1], A14[1]]


#Normalizar datos
def min_max_norm(dataset):
    if isinstance(dataset, list):
        norm_list = list()
        min_value = min(dataset)
        max_value = max(dataset)

        for value in dataset:
            tmp = (value - min_value) / (max_value - min_value)
            norm_list.append(tmp)

    return norm_list

HDIVALS = (min_max_norm([float(i) for i in HDI]))
NOXVALS = (min_max_norm([float(i) for i in NOX]))

HDI = [i/10.0 for i in HDI]
"""
t = np.arange(1990, 2015, 1)

# Representar datos
plt.plot(t, HDIVALS, '-g', label='HDI')
plt.plot(t, NOXVALS, '-r', label='NOX')
plt.legend(loc='upper left')
plt.title('HDI vs Emisiones de NOX (G2)')
plt.xlabel('Fecha')
plt.ylabel('Cambio normalizado')
plt.show()
"""

fig, ax1 = plt.subplots()
t = np.arange(1990, 2015, 1)
s1 = HDI
ax1.plot(t, s1, 'g-')
ax1.set_xlabel('Tiempo')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('HDI (%)', color='g')
ax1.tick_params('y', colors='g')

ax2 = ax1.twinx()
s2 = NOX
ax2.plot(t, s2, 'r-')
ax2.set_ylabel('NOX (Kilotoneladas)', color='r')
ax2.tick_params('y', colors='r')

plt.title('HDI vs Emisiones de NOX')

fig.tight_layout()
plt.show()



