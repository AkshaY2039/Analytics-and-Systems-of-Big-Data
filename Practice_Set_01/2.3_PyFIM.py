# PyMining - Item Mining

from fim import apriori, eclat, fpgrowth, fim
tracts = [	[ 1, 2, 3 ],
			[ 1, 4, 5 ],
			[ 2, 3, 4 ],
			[ 1, 2, 3, 4 ],
			[ 2, 3 ],
			[ 1, 2, 4 ],
			[ 4, 5 ],
			[ 1, 2, 3, 4 ],
			[ 3, 4, 5 ],
			[ 1, 2, 3 ] ]

print('transactions:')
for t in tracts:
	print(t)

print ('\nEclat supp=3, min_items_per_set=2')
for r in eclat(tracts, supp=-3, zmin=2):
	print(r)

print ('\nApriori supp=3, min_items_per_set=2')
for r in apriori(tracts, supp=-3, zmin=2):
	print(r)

print ('\nFP Growth supp=3, min_items_per_set=2')
for r in fpgrowth(tracts, supp=-3, zmin=2):
	print(r)