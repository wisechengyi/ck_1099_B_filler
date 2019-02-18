from real_data import total

CATEGORY = '''$('#row{} > td:nth-child(2) > label > select')[0].value={}'''
DESCRIPTION = '''$("#row{} > td:nth-child(3) > input")[0].value="{}"'''
DATE_ACQUIRED = '''$("#row{} > td:nth-child(4) > input")[0].value="{}"'''
DATE_SOLD = '''$("#row{} > td:nth-child(5) > input")[0].value="{}"'''
SALES_PRICE = '''$("#row{} > td:nth-child(6) > input")[0].value={}'''
COST = '''$("#row{} > td:nth-child(7) > input")[0].value={}'''

# <select name="capitalGains[26].reportingCategory" class="reported">
#                                         <option value="0"></option>
#
#                                             <option value="1">Short-term: You received a 1099-B and basis (Box 3) WAS reported to the IRS</option>
#
#                                             <option value="2">Short-term: You received a 1099-B and basis (Box 3) WAS NOT reported to the IRS</option>
#
#                                             <option value="3">Short-term: You did not receive a 1099-B for this transaction</option>
#
#                                             <option value="4">Long-term: You received a 1099-B and basis (Box 3) WAS reported to the IRS</option>
#
#                                             <option value="5" selected="selected">Long-term: You received a 1099-B and basis (Box 3) WAS NOT reported to the IRS</option>
#
#                                             <option value="6">Long-term: You did not receive a 1099-B for this transaction</option>
#
#                                     </select>

# From https://www.irs.gov/pub/irs-pdf/f8949.pdf
# (A) Short-term transactions reported on Form(s) 1099-B showing basis was reported to the IRS (see Note above)
# (B) Short-term transactions reported on Form(s) 1099-B showing basis wasn’t reported to the IRS
# (C) Short-term transactions not reported to you on Form 1099-B
# (D) Long-term transactions reported on Form(s) 1099-B showing basis was reported to the IRS (see Note above)
# (E) Long-term transactions reported on Form(s) 1099-B showing basis wasn’t reported to the IRS
# (F) Long-term transactions not reported to you on Form 1099-B


cat_map = {
  'A': 1,
  'B': 2,
  'C': 3,
  'D': 4,
  'E': 5,
}

row = 33
for l in total.splitlines()[1:]:
  description, date_acquired, date_sold, sales_price, cost, _, _, term, category, reported, withheld, _, _ = l.split(
    '\t')
  # print(description, date_acquired, date_sold, sales_price, cost, term, category, reported, withheld)
  print(DESCRIPTION.format(row, description) + ';')
  print(CATEGORY.format(row, cat_map[category]) + ';')
  print(DATE_ACQUIRED.format(row, date_acquired) + ';')
  print(DATE_SOLD.format(row, date_sold) + ';')
  print(SALES_PRICE.format(row, sales_price) + ';')
  print(COST.format(row, cost) + ';')

  row += 1
