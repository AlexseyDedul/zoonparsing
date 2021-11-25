# https://zoon.by/minsk/restaurants/

import pandas as pd
from parser import pars

# dfCatalogMinsk = pd.DataFrame(pars('https://zoon.by/minsk/'))
# dfCatalogMinsk.to_excel('./catalogMinsk.xlsx')

# dfCatalogMogilev = pd.DataFrame(pars('https://zoon.by/mogilev/'))
# dfCatalogMogilev.to_excel('./catalogMogilev.xlsx')
#
# dfCatalogBrest = pd.DataFrame(pars('https://zoon.by/brest/'))
# dfCatalogBrest.to_excel('./catalogBrest.xlsx')
#
# dfCatalogGomel = pd.DataFrame(pars('https://zoon.by/gomel/'))
# dfCatalogGomel.to_excel('./catalogGomel.xlsx')
#
# dfCatalogGrodno = pd.DataFrame(pars('https://zoon.by/grodno/'))
# dfCatalogGrodno.to_excel('./catalogGrodno.xlsx')
#
dfCatalogVitebsk = pd.DataFrame(pars('https://zoon.by/vitebsk/'))
dfCatalogVitebsk.to_excel('./catalogVitebsk.xlsx')
