# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 17:27:38 2015

@author: thomas.douenne
"""

import pandas as pd

from ipp_macro_series_parser.agregats_transports.transports_cleaner import *


def tidy_melt_categorie_index(data_frame):
    annees = list(data_frame)
    data_frame = pd.melt(data_frame, id_vars = ['categorie', 'index'], value_vars = annees[2:],
        value_name = 'unite', var_name = 'annee')
    return data_frame

g_3a = tidy_melt_categorie_index(g_3a)
g_3a.rename(columns = {'unite': 'conso_millier_m3'}, inplace = True)
g2_1 = tidy_melt_categorie_index(g2_1)
g2_1.rename(columns = {'unite': 'parc_millier_veh'}, inplace = True)
