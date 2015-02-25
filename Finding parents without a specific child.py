# Suppose we need to find a list of all interfaces that have CDP evabled; this
# implies a couple of things:
#   1. CDP has not been disabled globally with [no cdp run]
#   2. The interfaces in question are not configured with [no cdp enable]

from ciscoconfparse import CiscoConfParse
parse = CiscoConfParse('bucksnort.conf')
if not bool(parse.find_objects(r'no cdp run')):
    cdp_intfs = parse.find_parents_wo_child(r'^interface',
            r'no cdp enable')

print cdp_intfs
