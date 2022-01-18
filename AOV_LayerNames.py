import nuke as nuke

n = nuke.thisNode()

layerNameMerge = nuke.toNode("AOV_Contactsheet")

text_merge = nuke.toNode("Text_merge")

bbox = n.bbox()

layers = set([i.split('.')[0] for i in n.channels()])

removeNode = nuke.nodes.Remove()

removeNode.setInput(0, n)

inNode = removeNode

# create text per layer

for layer in layers:
    textNode = nuke.nodes.Text2()
    textNode['box'].setValue((bbox.x(), bbox.y(), bbox.x() + bbox.w(), bbox.y() + bbox.h()))
    textNode['output'].setValue(layer)
    textNode['message'].setValue(layer)
    textNode['font_size'].setValue(100)
    textNode['global_font_scale'].setValue(2)
    textNode['xjustify'].setValue("left")
    textNode['yjustify'].setValue("bottom")
    textNode.setInput(0, inNode)

    inNode = textNode

# create contact sheet for text

layerCC2 = nuke.nodes.LayerContactSheet()
layerCC2.knob('showLayerNames').setExpression('parent.nukelayernames')
layerCC2.knob('width').setExpression('parent.AOV_Contactsheet.knob.width')
layerCC2.knob('height').setExpression('parent.AOV_Contactsheet.knob.height')
layerCC2.setInput(0, inNode)

# use Saturation node to show text in all channels

satNode = nuke.nodes.Saturation(channels='all', saturation=0, mode='Maximum')

satNode.setInput(0, layerCC2)

mergeNode = nuke.nodes.Merge()

mergeNode.setInput(0, layerNameMerge)

mergeNode.setInput(1, satNode)

text_merge.setInput(0, mergeNode)
