from ciscoconfparse import CiscoConfParse
parse = CiscoConfParse('bucksnort.conf')
serial_objs = parse.find_objects('^interface Serial')

for obj in serial_objs:
    print obj.text
