import nuke

root = nuke.Root()
tn = nuke.thisNode()
last = root.lastFrame()
nodelist = []
offset = 0

tn['selected'].setValue(False)
with root:
    for node in nuke.allNodes('Group'):
        if "AOV_Layer_Contact_Sheet" in node.name():
            nodelist.append(node.fullName())
    nodelist.sort()

    sn = nuke.selectedNode()
    for i, node in enumerate(nodelist):
        if str(sn.name()) == nodelist[i]:
            offset = (i + 1)
            print '[Info]Selected Node {sn}'.format(sn=sn.name())
            print '[Info]Index {i}'.format(i=i)
    with nuke.toNode(sn.name()):
        n = nuke.toNode('Retime1')
        n.showControlPanel()
        n.knob('before').setValue('black')
        n.knob('after').setValue('black')
        n.hideControlPanel()


l_frame = offset + last
tn.knob('frame').setValue(l_frame)

print '[Info]Nodelist {nodelist}'.format(nodelist=nodelist)
print '[Info]Offset {offset}'.format(offset=offset)
print '[Info]Output Frame {l_frame}'.format(l_frame=l_frame)

