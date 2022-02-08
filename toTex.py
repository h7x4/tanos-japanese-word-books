#!/usr/bin/env python3

from lxml import etree;
from re import sub

for n in reversed(range(1,6)):
  with open(f'./data/html/n{n}.html', 'r') as file:
    doc = etree.parse(file)

  def extractCellText(col):
    a = col.xpath('a')
    if len(a) == 0: return ''
    return sub(r'(-?\d+(?:\.\d+)?\^-?\d+(?:\.\d+)?)', r'$\1$', a[0].text.replace('#', '\\#'))

  rows = (tuple(map(extractCellText, tr.xpath("td"))) for tr in doc.xpath("//tbody/tr"))

  # Skip header
  next(rows)

  # Make cell with multiple rows in latex if there's multiple meanings/readings
  def makeMultiCellIfMultipleEntries(cellText, rowtype = 'j'):
    if rowtype == 'j' and '/' in cellText:
      return '\\makecell[l]{ %s }' % cellText.replace('/', ' \\\\ ')
    elif rowtype == 'e' and ',' in cellText:
      return '\\makecell[l]{ %s }' % cellText.replace(',', ' \\\\ ')
    else:
      return cellText
      

  with open(f'./data/tex/n{n}.tex', 'w') as file:
    file.write('\\begin{longtabu} to \\textwidth {ll|l}\n')
    file.write(
      " \\\\\\hline\n".join(f'{makeMultiCellIfMultipleEntries(row[0])} & {makeMultiCellIfMultipleEntries(row[1])} & {makeMultiCellIfMultipleEntries(row[2], rowtype="e")}' for row in rows)
    )
    file.write('\n\\end{longtabu}')
