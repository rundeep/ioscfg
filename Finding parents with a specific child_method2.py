# Suppose we need to find interfaces with the QOS_1 service-policy applied outvound...
# Method 2: list-comprehension to iterate over objects and search children

from ciscoconfparse import CiscoConfParse
parse = CiscoConfParse('bucksnort.conf')
qos_intfs = [obj for obj in parse.find_objects(r'^interf') \
    if obj.re_search_children(r'service-policy\soutput\sQOS_1')]

print qos_intfs
