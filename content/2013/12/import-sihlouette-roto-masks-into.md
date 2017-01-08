Title: Import Sihlouette roto masks into several Nuke shapes
Author: SergeM
Date: 2013-12-10 12:03:00
Slug: import-sihlouette-roto-masks-into
Tags: nuke,python,roto

Today kids, I tell you how to split imported Sihlouette shapes into Nuke RotoPaint nodes.

In SihlouetteFX select several nodes.
Go _File->Export->nuke 6.2+ Shapes_ &nbsp;and save Nuke project

I tried to use also&nbsp;_File->Export->Nuke Shapes_ but in Nuke 7.0 it wasn't opened properly

Open saved project in Nuke. There is a single RotoPaint node. It contains several layers with several shapes in each.
I need separate layers into many nodes to use them separately.

To do this I wrote following script:




    ::::
    import nuke, nuke.rotopaint as rp
    
    def rptsw_walker(obj, list):
        # loop wor each subitem in Rotopaint
        for i in obj:
            # if there is a layer
            if isinstance(i, nuke.rotopaint.Layer):
                # create new RotoPaint object
                paintNode = nuke.createNode('RotoPaint')
                curvesKnob = paintNode['curves']
                rotoRoot = curvesKnob.rootLayer
    
                list1 = []
    
                # for each bezier shape we add it to the list. I don't know why
                # adding it to a list causes deleting shape from origin
                # if adding directly to the new roto object some shapes were not copied
                for j in i:
                    if isinstance(j, nuke.rotopaint.Shape):
                        list1.append(j)
    
                # copy all shapes from list to new roto node
                for j in list1:
                   rotoRoot.append(j)
    
    # find selected node
    rotoNode = nuke.selectedNode()
    rptsw_shapeList = []
    rotoCurve = rotoNode['curves']
    rotoRoot = rotoCurve.rootLayer
    # run
    rptsw_walker(rotoRoot, rptsw_shapeList)       
    
    
    
**Don't forget to select &nbsp;source RotoPaint node !!**
**Attention! This script deletes shapes from original RotoPaint!**

Does anybody know why copying shape to another node causes deleting it from original one?


Another not working solution found in google:
Source:&nbsp;[http://www.mail-archive.com/nuke-python@support.thefoundry.co.uk/msg02905/convert_shapetostroke.py](http://www.mail-archive.com/nuke-python@support.thefoundry.co.uk/msg02905/convert_shapetostroke.py)

<pre style="white-space: pre-wrap; word-wrap: break-word;"><span style="font-size: xx-small;">#***********************************************************
#Boundary Visual Effects - Silhouette Stroke Importer
#Version 0.98
#
#Created by Magno Borgo
#For greeting, bugs, and requests email me at mborgo[at]boundaryvfx.com
#Compatibility: Nuke 6.3 and up (not tested on previous versions)
#If you like and use the script frequently, please consider a small donation via Paypal to the same email above.
#
#Legal stuff:
#This script is provided "as is," without warranty of any kind, expressed
#or implied. In no event shall the author be held liable for any damages 
#arising in any way from the use of this script.
#***********************************************************
#Changelog
#v1.0
#initial release.
#***********************************************************
# Usage: Import the shapes exported from Silhouette, select the roto node and the group, and run.
# The stroke  precision can be set on the script, increase precision if you need to subdivide the stroke further.
#silhouetteStrokeImporter(2) (default = 2) 
#silhouetteStrokeImporter(5)
#***********************************************************

import nuke, nuke.rotopaint as rp, math, re
import threading, time
import profile

def rptsw_walker(obj, list):  
    for i in obj:
        if isinstance(i, nuke.rotopaint.Shape):
            list.append([i, obj]) 
        if isinstance(i, nuke.rotopaint.Layer):
            list.append([i, obj])
            rptsw_walker(i, list)
    return list


    
def strokeMap(value):
    return 1

  
def copyTransforms(oldT,newT):
    oldT = oldT.getTransform() 
    newT = newT.getTransform()   
    for i in range(3):
        newT.setTranslationAnimCurve(i,oldT.getTranslationAnimCurve(i))
        newT.setScaleAnimCurve(i,oldT.getScaleAnimCurve(i))
        newT.setSkewXAnimCurve(i,oldT.getSkewXAnimCurve(i))
        newT.setPivotPointAnimCurve(i,oldT.getPivotPointAnimCurve(i))
        newT.setRotationAnimCurve(i,oldT.getRotationAnimCurve(i))
    for i in range(4):
        for j in range(4):
            newT.setExtraMatrixAnimCurve(i,j,oldT.getExtraMatrixAnimCurve(i,j))

def copyAttributes(oldshape, newshape):
    old = oldshape.getAttributes()
    new= newshape.getAttributes()
    for i in range(len(old)):
        new.setCurve(i, old.getCurve(i))
        
        

def createLayer(shape, rotoRoot, newRotoNode, shapeInfos, task):
    newRotoNodeCurve = newRotoNode['curves']
    newRotoRoot = newRotoNodeCurve.rootLayer
    silhouetteData = matchShapeInfo(shape[0],shapeInfos)
    newLayer = rp.Layer(newRotoNodeCurve)
    newLayer.name = silhouetteData['LABEL']
    
    
    #task related code
    task.setMessage( 'Creating Layer: ' + silhouetteData['LABEL']  )
    if task.isCancelled():
        taskCancel = True
    #end of task related code   
    

    if shape[1] == rotoRoot:
        newRotoRoot.append(newLayer)
    else:
        parentLayer = matchShapeInfo(shape[1],shapeInfos)
        newlayerList = []                
        newlayerList = rptsw_walker(newRotoRoot, newlayerList)
        for layer in newlayerList:
            if isinstance(layer[0], nuke.rotopaint.Layer):
                if layer[0].name == parentLayer['LABEL']:
                    assignParent = layer[0]
        
        assignParent.append(newLayer)
    copyTransforms(shape[0],newLayer)
    
    


def createStroke(shape, rotoRoot, newRotoNode, shapeInfos, precision, task):
    cancel = False
    silhouetteData = 1 #dummy stroke width/size
    newRotoNodeCurve = newRotoNode['curves']
    newRotoRoot = newRotoNodeCurve.rootLayer
    newlayerList = []                
    newlayerList = rptsw_walker(newRotoRoot, newlayerList)
    newstroke = rp.Stroke(newRotoNodeCurve)
    keysTimes = shape[0][0].center.getControlPointKeyTimes()
    taskcount =0
    for i in range((len(shape[0]) *precision)+1):
        #task related code
        task.setMessage( 'Creating Stroke: ' +  '\npoint ' + str(taskcount+1) + " of " + str(len(shape[0]) *precision) )
        taskcount +=1
        if task.isCancelled():
            taskCancel = True
            break           
        #end of task related code        


        newPoint = rp.AnimControlPoint(0,0,1)
        for key in keysTimes:
           
            if i == 0: # or n ==  (len(shape[0]) *precision): #extra points on begin/end

                pos = 0
                point = [shape[0][0].center.getPositionAnimCurve(0).evaluate(key),shape[0][0].center.getPositionAnimCurve(1).evaluate(key),0]
            elif i == (len(shape[0]) *precision):
                pos = 1
                point = [shape[0][-1].center.getPositionAnimCurve(0).evaluate(key),shape[0][-1].center.getPositionAnimCurve(1).evaluate(key),0]
            else:    
                pos = float((i)* 1.0/(len(shape[0])*precision))
                cubicCurve = shape[0].evaluate(0, key)
                point = cubicCurve.getPoint(pos)
            vector = nuke.math.Vector3(point[0],point[1], 1)
            newPoint.addPositionKey(key,vector)
        
        newstroke.append(newPoint)
    copyTransforms(shape[0],newstroke)
#    newstroke.name = silhouetteData['LABEL']
    newstroke.setVisible(0, shape[0].getVisible(0))
    
    if shape[1] == rotoRoot:
        newRotoRoot.append(newstroke)
    else:
        parentLayer = matchShapeInfo(shape[1],shapeInfos)
        for layer in newlayerList:
            if isinstance(layer[0], nuke.rotopaint.Layer):
                if layer[0].name == parentLayer['LABEL']:
                    assignParent = layer[0]
        assignParent.append(newstroke)

    attrs = newstroke.getAttributes()
    oldattrs = shape[0].getAttributes()
    attrs.setCurve(9,oldattrs.getCurve('opc')) #opacity
    
    if float(silhouetteData) >= 3:
        attrs.set("bs",float(silhouetteData)) 
    else:
        if float(silhouetteData) < 2:
            attrs.set("bs",2) #value of 1 created problems on stroke rendering
            
        else:
            attrs.set("bs",float(silhouetteData)) 
        keys = attrs.getNumberOfKeys('opc')
        if keys == 0:
            attrs.set("opc", strokeMap(round(float(silhouetteData),1)))
        for i in range(keys):
            t = attrs.getKeyTime(9, i)
            currentValue = attrs.getValue(t,"opc")
            attrs.set(t,"opc", currentValue*strokeMap(round(float(silhouetteData),1)))
    attrs.set("h",0.5) #hardness
    
    
        
def createShape(shape, rotoRoot, newRotoNode, shapeInfos, task):
    cancel = False
    newRotoNodeCurve = newRotoNode['curves']
    newRotoRoot = newRotoNodeCurve.rootLayer
    newlayerList = []                
    newlayerList = rptsw_walker(newRotoRoot, newlayerList)
    silhouetteData = matchShapeInfo(shape[0],shapeInfos)
    
    shapeattr = shape[0].getAttributes()
    if shapeattr.getValue(0, "tt") == 5:
        newstroke = rp.Shape(newRotoNodeCurve, type="bspline")
    else:
        newstroke = rp.Shape(newRotoNodeCurve)

    taskcount = 0
    for point in shape[0]:

        #task related code
        task.setMessage( 'Creating Shape: ' + silhouetteData['LABEL'] + '\npoint ' + str(taskcount+1) + " of " + str(len(shape[0])) )
        taskcount +=1
        if task.isCancelled():
            taskCancel = True
            break           
        #end of task related code        
        
        
        
        newPoint = rp.ShapeControlPoint()
        for i in range(2):
            newPoint.featherCenter.setPositionAnimCurve(i, point.featherCenter.getPositionAnimCurve(i))
            newPoint.featherLeftTangent.setPositionAnimCurve(i, point.featherLeftTangent.getPositionAnimCurve(i))
            newPoint.featherLeftTangent.setPositionAnimCurve(i, point.featherLeftTangent.getPositionAnimCurve(i))
            newPoint.featherRightTangent.setPositionAnimCurve(i, point.featherRightTangent.getPositionAnimCurve(i))
            newPoint.leftTangent.setPositionAnimCurve(i, point.leftTangent.getPositionAnimCurve(i))
            newPoint.rightTangent.setPositionAnimCurve(i, point.rightTangent.getPositionAnimCurve(i))
            newPoint.center.setPositionAnimCurve(i, point.center.getPositionAnimCurve(i))       
        newstroke.append(newPoint)
 
    newstroke.name = silhouetteData['LABEL']
    copyTransforms(shape[0],newstroke)
    copyAttributes(shape[0],newstroke)
    
    if shape[1] == rotoRoot:
        newRotoRoot.append(newstroke)
    else:
        parentLayer = matchShapeInfo(shape[1],shapeInfos)
        for layer in newlayerList:
            if isinstance(layer[0], nuke.rotopaint.Layer):
                if layer[0].name == parentLayer['LABEL']:
                    assignParent = layer[0]
        assignParent.append(newstroke)

    

        
 
def silhouetteStrokeImporter(precision=2):
    
    selection = nuke.selectedNodes()
    taskCancel = False
    for node in selection:
        if node.Class() not in ('Roto', 'RotoPaint','Group'):
            if nuke.GUI:
                nuke.message( 'You must select the Roto node and the Group with metadata' )
            raise TypeError, 'You must select the Roto node and the Group with metadata'
        if node.Class() in ('Roto', 'RotoPaint'):
            rotoNode = node
        else:
            groupNodes = node.nodes()
            stickyNode = groupNodes[0]
    start_time = time.time()
    rptsw_shapeList = []
    silhouetteData =[] 
    rotoCurve = rotoNode['curves']
    rotoRoot = rotoCurve.rootLayer
    newRotoNode = nuke.createNode('RotoPaint')
    newRotoNode.setName(rotoNode.name()+ "_STROKE_IMPORTER_" +  newRotoNode.name())
    newRotoNodeCurve = newRotoNode['curves']
    newRotoRoot = newRotoNodeCurve.rootLayer
    rptsw_shapeList = rptsw_walker(rotoRoot, rptsw_shapeList)
    newRotoNode.knob('format').setValue(rotoNode.knob('format').value())
    newRotoNode.knob('output').setValue(rotoNode.knob('output').value())
    start_time = time.time()
    taskCount = 0.0
    task = nuke.ProgressTask( 'Silhouette Stroke\nImporter\n' )
    for shape in rptsw_shapeList:
        #BEGIN some UI task related settings
        if task.isCancelled():
            taskCancel = True
            break                
        if taskCancel:
            break
        task.setProgress(taskCount/len(rptsw_shapeList) * 100)
        taskCount +=1
        #END UI task related settings       

        if isinstance(shape[0], nuke.rotopaint.Layer):
            createLayer(shape, rotoRoot, newRotoNode, shapeInfos, task)

    for shape in rptsw_shapeList:
        #BEGIN some UI task related settings
        if task.isCancelled():
            taskCancel = True
            break                
        if taskCancel:
            break
        task.setProgress(taskCount/len(rptsw_shapeList) * 100)
        taskCount +=1
        #END UI task related settings 
                    
        if isinstance(shape[0], nuke.rotopaint.Shape):
            shapeInfos ="dummy"
            silhouetteData = 1 #dummy stroke width/size
            if float(silhouetteData) > 0:
                threading.Thread(None, createStroke, args=(shape, rotoRoot, newRotoNode, shapeInfos, precision, task)).start()
            else:
        
                threading.Thread(None, createShape, args=(shape, rotoRoot, newRotoNode, shapeInfos, task)).start()
                

         
          
    newRotoNodeCurve.changed()
    rptsw_shapeList = []
    print "Time elapsed:",time.time() - start_time, "seconds"

#remove the line below if you are using the script with menu.py (in menus/DAG/etc)
silhouetteStrokeImporter()</span>
</pre><div>
</div>

</div>