
# python的多级的嵌套字典内容。


cities = {
	    'shanghai':{'country':'china','population':10000,'fact':'good'},
	    'lendon':{'country':'england','population':2348,'fact':'nice'},
	    'new york':{'country':'american','population':8650,'fact':'rich'},
    }
for city,characts in cities.items():
    print("city:"+city.title())
    print("\tcountry:"+characts['country'])
    print("\tpopulation:"+str(characts['population']))
    print("\tfact:"+characts['fact'])
    print("\n")