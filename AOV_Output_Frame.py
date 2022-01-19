import nuke

root = nuke.Root()
tn = nuke.thisNode()
last = root.lastFrame()
nodelist = []
offset = 1

with root:
    for node in nuke.allNodes('Group'):
        if "AOV_Layer_Contact_Sheet" in node.name():
            nodelist.append(node.fullName())
    nodelist.sort()

    sn = nuke.selectedNode()
    for i, node in enumerate(nodelist):
        if str(sn.name()) == nodelist[i]:
            offset = (i + 1)
            print sn.name()
            print i

l_frame = offset + last
tn.knob('frame').setValue(l_frame)

print nodelist
print offset
print l_frame
