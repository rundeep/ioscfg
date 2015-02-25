# Suppose we need to find interfaces with the QOS_1 service-policy applied outvound...
# Method 3: find_objects_w_child()

from ciscoconfparse import CiscoConfParse
parse = CiscoConfParse('bucksnort.conf')
qos_intfs = parse.find_objects_w_child(parentspec = r'^interf', \
    childspec = r'service-policy\soutput\sQOS_1')

print qos_intfs
