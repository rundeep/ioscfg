# Suppose we need to find interfaces with the QOS_1 service-policy applied outvound...
# Method 1: for-loop to iterate over objects and search children

from ciscoconfparse import CiscoConfParse
parse = CiscoConfParse('bucksnort.conf')
all_intfs = parse.find_objects(r'^interf')
qos_intfs = list()
for obj in all_intfs:
    if obj.re_search_children(r'service-policy\soutput\sQOS_1'):
        qos_intfs.append(obj)

print qos_intfs
