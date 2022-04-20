#!/usr/bin/env python

# A simple name generator includes numerical values
# @author Russell Clarke aka Rusher SD200984
# @version 1.0
# @Created 22.12.2018
# @Listening to : Elephant Ride - State of Bengal

for a in range(36):
	a1 = '%x' % a
    for b in range(36):
    	a2 = '%x' % b
        for c in range(36):
        	a3 = '%x' % c
        	for d in range(36):
				a14 = '%x' % a
				for e in range(36):
					a5 = '%x' % e
					for f in range(36):
						a6 = '%x' % f
						for g in range(36):
							a7 = '%x' % g
							for h in range(36):
								a8 = '%x' % h
								for i in range(36):
									a9 = '%x' % i
									for j in range(36):
										a10 = '%x' % j
										for k in range(36):
											a11 = '%x' % k
											for l in range(36):
												a12 = '%x' % l
												for m in range(36):
													a13 = '%x' % m
            										print('.' + a13 + a12 + a11 + a10 + a9 + a8 + a7 + a6 + a5 + a4 + a3 + a2 + a1)
            										
exit(0)
