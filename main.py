# https://www.freecodecamp.org/news/automate-your-life-with-python/
import pandas as pd
import numpy as np

pd.set_option('display.width', 320)
np.set_printoptions(linewidth=320)
pd.set_option('display.max_columns', 10)

# Extract tables from websites
a = pd.read_html('https://en.wikipedia.org/wiki/The_Avengers_(2012_film)')
print(a[1])

# Extract tables from pdfs
import camelot

tables = camelot.read_pdf('Resume_NamanAgarwal_BITSP.pdf', pages='1')
print(tables)

tables.export('try.csv', f='csv', compress=True)
tables[0].to_csv('try.csv')
