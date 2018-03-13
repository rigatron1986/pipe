import maya.api.OpenMaya as api

selections = api.MGlobal.getActiveSelectionList()
connect_info = []
if selections.length() != 0:
    dagPath_first = selections.getDagPath(0)
    node = dagPath_first.node()
    if node.apiType() == api.MFn.kMesh:
        fnDagNode = api.MFnDagNode(dagPath_first)
        fnMesh = api.MFnMesh(node)
        howManyInsts = fnDagNode.instanceCount(False)
        for inst_id in range(howManyInsts):
            shadings, faceArray = fnMesh.getConnectedShaders(inst_id)
            connect_info.append(
                (map(lambda s: api.MFnDependencyNode(s).name(), shadings), tuple(faceArray)))
    else:
        print 'You need select a mesh!'
else:
    print 'Nothing selected!'

if connect_info:
    for idx, sg in enumerate(connect_info):
        print 'Instance {0} : {1} -> {2}'.format(idx, sg[0], sg[1])
else:
    print 'Not any shader connections'
