import logging
import os

import vtk

import slicer
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin
import qt


# Z Frame offset:
HORIZONTAL = -64.25 #-68.3 # Reviewed on Nov 11 2022, white board used for animal experiments, one line of lego bricks
VERTICAL = -103.5
OFFSET = 13.0 #tempalte width


TABLE = ([["(7,G)", "(7,FF)", "(7,F)", "(7,EE)", "(7,E)", "(7,DD)", "(7,D)", "(7,CC)", "(7,C)", "(7,BB)", "(7,B)", "(7,AA)",
          "(7,A)"],
          ["(66,G)", "(66,FF)", "(66,F)", "(66,EE)", "(66,E)", "(66,DD)", "(66,D)", "(66,CC)", "(66,C)", "(66,BB)", "(66,B)",
           "(66,AA)", "(66,A)"]   ,
          ["(6,G)", "(6,FF)", "(6,F)", "(6,EE)", "(6,E)", "(6,DD)", "(6,D)", "(6,CC)", "(6,C)", "(6,BB)", "(6,B)",
           "(6,AA)", "(6,A)"],
          [ "(55,G)", "(55,FF)", "(55,F)", "(55,EE)", "(55,E)", "(55,DD)", "(55,D)", "(55,CC)", "(55,C)", "(55,BB)", "(55,B)", "(55,AA)",
            "(55,A)"]  ,
          ["(5,G)", "(5,FF)", "(5,F)", "(5,EE)", "(5,E)", "(5,DD)", "(5,D)", "(5,CC)", "(5,C)", "(5,BB)", "(5,B)",
           "(5,AA)",  "(5,A)"],
          ["(44,G)", "(44,FF)", "(44,F)", "(44,EE)", "(44,E)", "(44,DD)", "(44,D)", "(44,CC)", "(44,C)", "(44,BB)", "(44,B)",
           "(44,AA)", "(44,A)"],
          ["(4,G)", "(4,FF)", "(4,F)", "(4,EE)", "(4,E)", "(4,DD)", "(4,D)", "(4,CC)", "(4,C)", "(4,BB)", "(4,B)",
           "(4,AA)", "(4,A)"],
          ["(33,G)", "(33,FF)", "(33,F)", "(33,EE)", "(33,E)", "(33,DD)", "(33,D)", "(33,CC)", "(33,C)", "(33,BB)", "(33,B)",
           "(33,AA)", "(33,A)"],
          ["(3,G)", "(3,FF)", "(3,F)", "(3,EE)", "(3,E)", "(3,DD)", "(3,D)", "(3,CC)", "(3,C)", "(3,BB)", "(3,B)",
           "(3,AA)", "(3,A)"],
          ["(22,G)", "(22,FF)", "(22,F)", "(22,EE)", "(22,E)", "(22,DD)", "(22,D)", "(2,CC)", "(22,C)", "(22,BB)", "(22,B)",
           "(22,AA)", "(22,A)"],
          ["(2,G)", "(2,FF)", "(2,F)", "(2,EE)", "(2,E)", "(2,DD)", "(2,D)", "(2,CC)", "(2,C)", "(2,BB)", "(2,B)",
           "(2,AA)", "(2,A)"],
          ["(11,G)", "(11,FF)", "(11,F)", "(11,EE)", "(11,E)", "(11,DD)", "(11,D)", "(11,CC)", "(11,C)", "(11,BB)", "(11,B)",
           "(11,AA)", "(11,A)"],
         ["(1,G)", "(1,FF)", "(1,F)", "(1,EE)", "(1,E)", "(1,DD)", "(1,D)", "(1,CC)", "(1,C)", "(1,BB)", "(1,B)", "(1,AA)",
          "(1,A)"]])

#
# ManualPlanning
#

class ManualPlanning(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "ManualPlanning"  # TODO: make this more human readable by adding spaces
    self.parent.categories = ["Examples"]  # TODO: set categories (folders where the module shows up in the module selector)
    self.parent.dependencies = []  # TODO: add here list of module names that this module requires
    self.parent.contributors = ["John Doe (AnyWare Corp.)"]  # TODO: replace with "Firstname Lastname (Organization)"
    # TODO: update with short description of the module and a link to online module documentation
    self.parent.helpText = """
This is an example of scripted loadable module bundled in an extension.
See more information in <a href="https://github.com/organization/projectname#ManualPlanning">module documentation</a>.
"""
    # TODO: replace with organization, grant and thanks
    self.parent.acknowledgementText = """
This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc., Andras Lasso, PerkLab,
and Steve Pieper, Isomics, Inc. and was partially funded by NIH grant 3P41RR013218-12S1.
"""

    # Additional initialization step after application startup is complete
    slicer.app.connect("startupCompleted()", registerSampleData)


#
# Register sample data sets in Sample Data module
#

def registerSampleData():
  """
  Add data sets to Sample Data module.
  """
  # It is always recommended to provide sample data for users to make it easy to try the module,
  # but if no sample data is available then this method (and associated startupCompeted signal connection) can be removed.

  import SampleData
  iconsPath = os.path.join(os.path.dirname(__file__), 'Resources/Icons')

  # To ensure that the source code repository remains small (can be downloaded and installed quickly)
  # it is recommended to store data sets that are larger than a few MB in a Github release.

  # ManualPlanning1
  SampleData.SampleDataLogic.registerCustomSampleDataSource(
    # Category and sample name displayed in Sample Data module
    category='ManualPlanning',
    sampleName='ManualPlanning1',
    # Thumbnail should have size of approximately 260x280 pixels and stored in Resources/Icons folder.
    # It can be created by Screen Capture module, "Capture all views" option enabled, "Number of images" set to "Single".
    thumbnailFileName=os.path.join(iconsPath, 'ManualPlanning1.png'),
    # Download URL and target file name
    uris="https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/998cb522173839c78657f4bc0ea907cea09fd04e44601f17c82ea27927937b95",
    fileNames='ManualPlanning1.nrrd',
    # Checksum to ensure file integrity. Can be computed by this command:
    #  import hashlib; print(hashlib.sha256(open(filename, "rb").read()).hexdigest())
    checksums = 'SHA256:998cb522173839c78657f4bc0ea907cea09fd04e44601f17c82ea27927937b95',
    # This node name will be used when the data set is loaded
    nodeNames='ManualPlanning1'
  )

  # ManualPlanning2
  SampleData.SampleDataLogic.registerCustomSampleDataSource(
    # Category and sample name displayed in Sample Data module
    category='ManualPlanning',
    sampleName='ManualPlanning2',
    thumbnailFileName=os.path.join(iconsPath, 'ManualPlanning2.png'),
    # Download URL and target file name
    uris="https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/1a64f3f422eb3d1c9b093d1a18da354b13bcf307907c66317e2463ee530b7a97",
    fileNames='ManualPlanning2.nrrd',
    checksums = 'SHA256:1a64f3f422eb3d1c9b093d1a18da354b13bcf307907c66317e2463ee530b7a97',
    # This node name will be used when the data set is loaded
    nodeNames='ManualPlanning2'
  )


#
# ManualPlanningWidget
#

class ManualPlanningWidget(ScriptedLoadableModuleWidget, VTKObservationMixin):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent=None):
    """
    Called when the user opens the module the first time and the widget is initialized.
    """
    ScriptedLoadableModuleWidget.__init__(self, parent)
    VTKObservationMixin.__init__(self)  # needed for parameter node observation
    self.logic = None
    self._parameterNode = None
    self._updatingGUIFromParameterNode = False

  def setup(self):
    """
    Called when the user opens the module the first time and the widget is initialized.
    """
    ScriptedLoadableModuleWidget.setup(self)

    # Load widget from .ui file (created by Qt Designer).
    # Additional widgets can be instantiated manually and added to self.layout.
    uiWidget = slicer.util.loadUI(self.resourcePath('UI/ManualPlanning.ui'))
    self.layout.addWidget(uiWidget)
    self.ui = slicer.util.childWidgetVariables(uiWidget)

    # Set scene in MRML widgets. Make sure that in Qt designer the top-level qMRMLWidget's
    # "mrmlSceneChanged(vtkMRMLScene*)" signal in is connected to each MRML widget's.
    # "setMRMLScene(vtkMRMLScene*)" slot.
    uiWidget.setMRMLScene(slicer.mrmlScene)

    # Create logic class. Logic implements all computations that should be possible to run
    # in batch mode, without a graphical user interface.
    self.logic = ManualPlanningLogic()

    # Connections

    # These connections ensure that we update parameter node when scene is closed
    self.addObserver(slicer.mrmlScene, slicer.mrmlScene.StartCloseEvent, self.onSceneStartClose)
    self.addObserver(slicer.mrmlScene, slicer.mrmlScene.EndCloseEvent, self.onSceneEndClose)


    self.ui.MarkupsWidget.toolTip = "Select a target location"
    self.ui.MarkupsWidget.tableWidget().hide()
    self.ui.MarkupsWidget.markupsSelectorComboBox().noneEnabled = True
    self.ui.MarkupsWidget.markupsPlaceWidget().placeMultipleMarkups = (
        slicer.qSlicerMarkupsPlaceWidget.ForcePlaceSingleMarkup
    )
    self.ui.MarkupsWidget.markupsPlaceWidget().buttonsVisible = False
    self.ui.MarkupsWidget.markupsPlaceWidget().placeButton().show()
    self.ui.MarkupsWidget.setMRMLScene(slicer.mrmlScene)

#TODO:
    # Save the angles in a text node, then CryoControl can get it
    # Actually, it is better to start the text node in the cryocontrol and this code just grab and update
    
    self.ui.MarkupsWidget.connect("activeMarkupsPlaceModeChanged(bool)", self.updateMarkupFiducial)

    try:
      targetList = slicer.util.getNode('target')
      targetList.RemoveAllMarkups()
    except:
      target_points = slicer.vtkMRMLMarkupsFiducialNode()
      target_points.SetName('target')
      slicer.mrmlScene.AddNode(target_points)
    
    self.loadTemplate()
    self.setEllipsoids()
    self.loadNeedleModel()

    self.ui.horizontalSlider.valueChanged.connect(self.onSliderChange)
    self.ui.horizontalSlider_2.valueChanged.connect(self.onSliderChange)
    self.ui.calculateButton.connect('clicked(bool)', self.onCalcButton)


    self.ui.IceballcheckBox.connect("toggled(bool)", self.showIceball)

    # These connections ensure that whenever user changes some settings on the GUI, that is saved in the MRML scene
    # (in the selected parameter node).
    #self.ui.inputSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.updateParameterNodeFromGUI)
    #self.ui.outputSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.updateParameterNodeFromGUI)
    #self.ui.imageThresholdSliderWidget.connect("valueChanged(double)", self.updateParameterNodeFromGUI)
    #self.ui.invertOutputCheckBox.connect("toggled(bool)", self.updateParameterNodeFromGUI)
    #self.ui.invertedOutputSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.updateParameterNodeFromGUI)


    # Buttons
    #self.ui.applyButton.connect('clicked(bool)', self.onApplyButton)

    # Make sure parameter node is initialized (needed for module reload)
    self.initializeParameterNode()



  def loadNeedleModel(self):
    try:
      needle1 = slicer.util.getNode('needle_1')
      needle1.RemoveAllMarkups()
      needle2 = slicer.util.getNode('needle_2')
      needle2.RemoveAllMarkups()
      needle3 = slicer.util.getNode('needle_3')
      needle3.RemoveAllMarkups()
      self.holes = slicer.util.getNode('holes')
    except:
      needle1 = slicer.vtkMRMLMarkupsFiducialNode()
      needle1.SetName('needle_1')
      slicer.mrmlScene.AddNode(needle1)
      needle2 = slicer.vtkMRMLMarkupsFiducialNode()
      needle2.SetName('needle_2')
      slicer.mrmlScene.AddNode(needle2)
      needle3 = slicer.vtkMRMLMarkupsFiducialNode()
      needle3.SetName('needle_3')
      slicer.mrmlScene.AddNode(needle3)

      self.holes = slicer.vtkMRMLTextNode()
      self.holes.SetName('holes')
      slicer.mrmlScene.AddNode(self.holes)

  def cleanup(self):
    """
    Called when the application closes and the module widget is destroyed.
    """
    self.removeObservers()

  def enter(self):
    """
    Called each time the user opens this module.
    """
    # Make sure parameter node exists and observed
    self.initializeParameterNode()

  def exit(self):
    """
    Called each time the user opens a different module.
    """
    # Do not react to parameter node changes (GUI wlil be updated when the user enters into the module)
    self.removeObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)

  def onSceneStartClose(self, caller, event):
    """
    Called just before the scene is closed.
    """
    # Parameter node will be reset, do not use it anymore
    self.setParameterNode(None)

  def onSliderChange(self):
    angle1 = self.ui.horizontalSlider.value
    angle2 = self.ui.horizontalSlider_2.value
    self.ang1 = slicer.util.getNode('ang1')
    self.ang2 = slicer.util.getNode('ang2')

    self.ang2.SetText(str(angle2))
    self.ang1.SetText(str(angle1))

    targetList = slicer.util.getNode('target')
    nOfPoint = targetList.GetNumberOfMarkups()
    if (nOfPoint != 0):
      for n in range(0,nOfPoint):
        pos = [0,0,0]
        targetList.GetNthFiducialPosition(n,pos)
        self.logic.updateIceballPose(n,angle1,angle2,pos)
    else:
      print("no iceballs yet")
      
    #try:
    transform = vtk.vtkTransform()
    transform.RotateX(angle1)
    transform.RotateY(angle2)
    #TemplateTrans.SetMatrixTransformToParent(transform.GetMatrix())s
  
    newTransform = vtk.vtkTransform()
    mtx = vtk.vtkMatrix4x4()
    mtx = self.transformZframe(mtx)

    mtx2 = vtk.vtkMatrix4x4()
    self.zFrame.GetMatrixTransformToParent(mtx2)

    newTransform = vtk.vtkMatrix4x4()
    vtk.vtkMatrix4x4.Multiply4x4(mtx2,mtx,newTransform)

    vtk.vtkMatrix4x4.Multiply4x4(newTransform,transform.GetMatrix(),newTransform)
    self.TemplateTrans.SetMatrixTransformToParent(newTransform)

    #except:
    #  print("no zFrame Registration")
        
  def onCalcButton(self):
    targetList = slicer.util.getNode('target')
    nOfPoint = targetList.GetNumberOfMarkups()
    transform = vtk.vtkMatrix4x4()
    self.TemplateTrans.GetMatrixTransformToParent(transform)
    transform.Invert()
    temp_str = " "
    for n in range(0,nOfPoint):
      pos = [0, 0, 0]
      targetList.GetNthFiducialPosition(n, pos)
      temp_in = [pos[0], pos[1], pos[2], 1]
      temp_out = [pos[0], pos[1], 0, 1]
      print(temp_out)
      transform.MultiplyPoint(temp_in,temp_out)
      print(temp_out)
      index_a = round((temp_out[0])/5.0)

      index_b = round((temp_out[1])/5.0)

      temp_str = temp_str+str(TABLE[index_b+6][index_a+6])+";"+str(int(-temp_out[2])+OFFSET)+" mm"+";"

      self.ui.tableWidget.setItem(n, 1, qt.QTableWidgetItem(TABLE[index_b+6][index_a+6]))
      self.ui.tableWidget.setItem(n, 2, qt.QTableWidgetItem(str(int(-temp_out[2])+OFFSET)+" mm"))



      temp_needle = "needle_"+str(n+1)
      # print(temp_needle)
      needle1 = slicer.util.getNode(temp_needle)
      needle1.RemoveAllMarkups()
      tip_pos = [index_a*5,index_b*5,temp_out[2],1.0]
      base_pos = [index_a*5, index_b*5, 0, 1.0]
      tip_out = [0 ,0, 0, 1]
      base_out = [0, 0, 0, 1]
      transform.Invert()
      transform.MultiplyPoint(tip_pos, tip_out)
      transform.MultiplyPoint(base_pos, base_out)
      #
      needle1.AddFiducial(tip_out[0], tip_out[1], tip_out[2])
      needle1.AddFiducial(base_out[0], base_out[1], base_out[2])
      transform.Invert()

      #print expected error based on the hole definition:
      errorR = f'{(tip_out[0]-pos[0]):.1f}'
      errorA = f'{(tip_out[1]-pos[1]):.1f}'
      self.ui.expError.setText("  R: "+str(errorR)+" A:"+str(errorA))

    self.holes.SetText(temp_str)

  def showIceball(self):
    targetList = slicer.util.getNode('target')
    nOfPoint = targetList.GetNumberOfMarkups()
    for n in range(0,nOfPoint):
    #rowPosition = self.ui.tableWidget.rowCount()

      string_temp = ("ellipse_%s") % (n+1)
      model = slicer.util.getNode(string_temp)
      if self.ui.IceballcheckBox.isChecked():
        model.SetDisplayVisibility(1)
      else:
        model.SetDisplayVisibility(0)

  def transformZframe(self, zFrame):
    _rotation = vtk.vtkMatrix4x4()
    _translation = vtk.vtkMatrix4x4()

    _translation.Identity()
    _translation.SetElement(1, 3, HORIZONTAL)
    _translation.SetElement(2, 3, VERTICAL)

    _rotation.Identity()
    _rotation.SetElement(1, 1, 0.0)
    _rotation.SetElement(1, 2, -1.0)
    _rotation.SetElement(2, 1, 1.0)
    _rotation.SetElement(2, 2, 0.0)

    _temp = vtk.vtkMatrix4x4()
    rotatedZframe = vtk.vtkMatrix4x4()

    vtk.vtkMatrix4x4.Multiply4x4(zFrame, _rotation, _temp)
    vtk.vtkMatrix4x4.Multiply4x4(_translation, _temp, rotatedZframe)

    return rotatedZframe



  def loadTemplate(self):
    
    try:
      self.TemplateTrans = slicer.util.getNode('TemplateTrans')
    except:
      self.TemplateTrans = slicer.vtkMRMLLinearTransformNode()
      self.TemplateTrans.SetName("TemplateTrans")
      slicer.mrmlScene.AddNode(self.TemplateTrans)
    try:
      self.zFrame = slicer.util.getNode('*ZFrameTransform')
      #_translation = vtk.vtkMatrix4x4()
      #_translation.Identity()
      #self.zFrame.SetMatrixTransformToParent(_translation)
    except:
      self.zFrame = slicer.vtkMRMLLinearTransformNode()
      self.zFrame.SetName("zFrame")
      slicer.mrmlScene.AddNode(self.zFrame)

    newTransform = vtk.vtkTransform()
    mtx = vtk.vtkMatrix4x4()
    mtx = self.transformZframe(mtx)

    mtx2 = vtk.vtkMatrix4x4()
    self.zFrame.GetMatrixTransformToParent(mtx2)

    newTransform = vtk.vtkMatrix4x4()
    vtk.vtkMatrix4x4.Multiply4x4(mtx2,mtx,newTransform)

    #self.zFrame.SetMatrixTransformToParent(newTransform)
    self.TemplateTrans.SetMatrixTransformToParent(newTransform)


    try:
      self.zFrameModelNode = slicer.util.getNode('Template')
      self.zFrameModelNode.GetDisplayNode().SetVisibility(True)
    except:
      dirname = slicer.modules.manualplanning.path
      #55 and 58
      filename = os.path.join(dirname[0:55], 'Resources/New_template.stl')
      _, self.zFrameModelNode = slicer.util.loadModel(filename, returnNode=True)
      slicer.mrmlScene.AddNode(self.zFrameModelNode)
      self.zFrameModelNode.SetName("Template")
      self.zFrameModelNode.GetDisplayNode().SetSliceIntersectionVisibility(False)
      self.zFrameModelNode.GetDisplayNode().SetSliceIntersectionThickness(3)
      self.zFrameModelNode.GetDisplayNode().SetColor(1,1,0)
      self.zFrameModelNode.GetDisplayNode().SetVisibility(True)
    
    #self.zFrameModelNode.SetAndObserveTransformNodeID(self.zFrame.GetID())
    #self.TemplateTrans.SetMatrixTransformToParent(self.zFrame)
    #mtx = vtk.vtkMatrix4x4()
    #self.zFrame.GetMatrixTransformToParent(mtx)
    #self.TemplateTrans.SetMatrixTransformToParent(mtx)
    
    
    zFrame = slicer.util.getNode('ZFrameModel')
    zFrame.GetDisplayNode().SetVisibility(False)
    
    self.templatePose()



  def templatePose(self):
    zFrameTrans = slicer.util.getNode('TemplateTrans')
    self.zFrameModelNode.SetAndObserveTransformNodeID(zFrameTrans.GetID())


#TODO
# fazer aqui uma funcao que envia os dois valores e o ponto para o logic e rotaciona os iceball tudo.


  def onSceneEndClose(self, caller, event):
    """
    Called just after the scene is closed.
    """
    # If this module is shown while the scene is closed then recreate a new parameter node immediately
    if self.parent.isEntered:
      self.initializeParameterNode()

  def initializeParameterNode(self):
    """
    Ensure parameter node exists and observed.
    """
    # Parameter node stores all user choices in parameter values, node selections, etc.
    # so that when the scene is saved and reloaded, these settings are restored.

    self.setParameterNode(self.logic.getParameterNode())

    # Select default input nodes if nothing is selected yet to save a few clicks for the user
    if not self._parameterNode.GetNodeReference("InputVolume"):
      firstVolumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
      if firstVolumeNode:
        self._parameterNode.SetNodeReferenceID("InputVolume", firstVolumeNode.GetID())

  def setEllipsoids(self):
    affectedBallArea = vtk.vtkParametricEllipsoid()
    affectedBallArea.SetXRadius(float(10))
    affectedBallArea.SetYRadius(float(10))
    affectedBallArea.SetZRadius(float(16))
    affectedBallAreaSource = vtk.vtkParametricFunctionSource()
    affectedBallAreaSource.SetParametricFunction(affectedBallArea)
    affectedBallAreaSource.SetScalarModeToV()
    affectedBallAreaSource.Update()
    modelsLogic = slicer.modules.models.logic()
    
    try:
      model = slicer.util.getNode('ellipse_1')
    except:   
      model = modelsLogic.AddModel(affectedBallAreaSource.GetOutput())
      model.SetName("ellipse_1")
    
    try:
      model2 = slicer.util.getNode('ellipse_2')
    except:   
      model2 = modelsLogic.AddModel(affectedBallAreaSource.GetOutput())
      model2.SetName("ellipse_2")
      
    try:
      model3 = slicer.util.getNode('ellipse_3')
    except:   
      model3 = modelsLogic.AddModel(affectedBallAreaSource.GetOutput())
      model3.SetName("ellipse_3")    



    model.SetDisplayVisibility(0)
    model2.SetDisplayVisibility(0)
    model3.SetDisplayVisibility(0)


  def setParameterNode(self, inputParameterNode):
    """
    Set and observe parameter node.
    Observation is needed because when the parameter node is changed then the GUI must be updated immediately.
    """

    if inputParameterNode:
      self.logic.setDefaultParameters(inputParameterNode)

    # Unobserve previously selected parameter node and add an observer to the newly selected.
    # Changes of parameter node are observed so that whenever parameters are changed by a script or any other module
    # those are reflected immediately in the GUI.
    if self._parameterNode is not None:
      self.removeObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)
    self._parameterNode = inputParameterNode
    if self._parameterNode is not None:
      self.addObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)

    # Initial GUI update
    self.updateGUIFromParameterNode()

  def updateGUIFromParameterNode(self, caller=None, event=None):
    """
    This method is called whenever parameter node is changed.
    The module GUI is updated to show the current state of the parameter node.
    """

    if self._parameterNode is None or self._updatingGUIFromParameterNode:
      return

    # Make sure GUI changes do not call updateParameterNodeFromGUI (it could cause infinite loop)
    self._updatingGUIFromParameterNode = True

    # Update node selectors and sliders



    # All the GUI updates are done
    self._updatingGUIFromParameterNode = False

  def updateParameterNodeFromGUI(self, caller=None, event=None):
    """
    This method is called when the user makes any change in the GUI.
    The changes are saved into the parameter node (so that they are restored when the scene is saved and loaded).
    """

    if self._parameterNode is None or self._updatingGUIFromParameterNode:
      return

    wasModified = self._parameterNode.StartModify()  # Modify all properties in a single batch

    self._parameterNode.SetNodeReferenceID("InputVolume", self.ui.inputSelector.currentNodeID)
    self._parameterNode.SetNodeReferenceID("OutputVolume", self.ui.outputSelector.currentNodeID)
    self._parameterNode.SetParameter("Threshold", str(self.ui.imageThresholdSliderWidget.value))
    self._parameterNode.SetParameter("Invert", "true" if self.ui.invertOutputCheckBox.checked else "false")
    self._parameterNode.SetNodeReferenceID("OutputVolumeInverse", self.ui.invertedOutputSelector.currentNodeID)

    self._parameterNode.EndModify(wasModified)


  def updateMarkupFiducial(self):
    targetList = slicer.util.getNode('target')
    nOfPoint = targetList.GetNumberOfMarkups()
    self.ui.tableWidget.setRowCount(nOfPoint)
    transformNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTransformNode")
    
    for n in range(0,nOfPoint):
        string_temp = ("Needle #%s") % (n+1)
        self.ui.tableWidget.setItem(n , 0, qt.QTableWidgetItem(string_temp))
        string_temp = ("ellipse_%s") % (n+1)
        model = slicer.util.getNode(string_temp)
        model.GetDisplayNode().SetSliceIntersectionVisibility(True)
        
        transformNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTransformNode")
        model.SetAndObserveTransformNodeID(transformNode.GetID())
        transform = vtk.vtkTransform()
        pos = [0,0,0]
        targetList.GetNthFiducialPosition(n,pos)
        
        transform.Translate(pos[0], pos[1], pos[2]-10)
        transformNode.SetMatrixTransformToParent(transform.GetMatrix())


  def onApplyButton(self):
    """
    Run processing when user clicks "Apply" button.
    """
    with slicer.util.tryWithErrorDisplay("Failed to compute results.", waitCursor=True):

      # Compute output
      self.logic.process(self.ui.inputSelector.currentNode(), self.ui.outputSelector.currentNode(),
        self.ui.imageThresholdSliderWidget.value, self.ui.invertOutputCheckBox.checked)

      # Compute inverted output (if needed)
      if self.ui.invertedOutputSelector.currentNode():
        # If additional output volume is selected then result with inverted threshold is written there
        self.logic.process(self.ui.inputSelector.currentNode(), self.ui.invertedOutputSelector.currentNode(),
          self.ui.imageThresholdSliderWidget.value, not self.ui.invertOutputCheckBox.checked, showResult=False)


#
# ManualPlanningLogic
#

class ManualPlanningLogic(ScriptedLoadableModuleLogic):
  """This class should implement all the actual
  computation done by your module.  The interface
  should be such that other python code can import
  this class and make use of the functionality without
  requiring an instance of the Widget.
  Uses ScriptedLoadableModuleLogic base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self):
    """
    Called when the logic class is instantiated. Can be used for initializing member variables.
    """
    ScriptedLoadableModuleLogic.__init__(self)

  def setDefaultParameters(self, parameterNode):
    """
    Initialize parameter node with default settings.
    """
    if not parameterNode.GetParameter("Threshold"):
      parameterNode.SetParameter("Threshold", "100.0")
    if not parameterNode.GetParameter("Invert"):
      parameterNode.SetParameter("Invert", "false")

  def process(self, inputVolume, outputVolume, imageThreshold, invert=False, showResult=True):
    """
    Run the processing algorithm.
    Can be used without GUI widget.
    :param inputVolume: volume to be thresholded
    :param outputVolume: thresholding result
    :param imageThreshold: values above/below this threshold will be set to 0
    :param invert: if True then values above the threshold will be set to 0, otherwise values below are set to 0
    :param showResult: show output volume in slice viewers
    """

    if not inputVolume or not outputVolume:
      raise ValueError("Input or output volume is invalid")

    import time
    startTime = time.time()
    logging.info('Processing started')

    # Compute the thresholded output volume using the "Threshold Scalar Volume" CLI module
    cliParams = {
      'InputVolume': inputVolume.GetID(),
      'OutputVolume': outputVolume.GetID(),
      'ThresholdValue' : imageThreshold,
      'ThresholdType' : 'Above' if invert else 'Below'
      }
    cliNode = slicer.cli.run(slicer.modules.thresholdscalarvolume, None, cliParams, wait_for_completion=True, update_display=showResult)
    # We don't need the CLI module node anymore, remove it to not clutter the scene with it
    slicer.mrmlScene.RemoveNode(cliNode)

    stopTime = time.time()
    logging.info(f'Processing completed in {stopTime-startTime:.2f} seconds')



  def updateIceballPose(self,n,ang1,ang2,pos):
    string_temp = ("ellipse_%s") % (n+1)
    model = slicer.util.getNode(string_temp)
        
    transformNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTransformNode")
    model.SetAndObserveTransformNodeID(transformNode.GetID())
    transform = vtk.vtkTransform()
    transform.Translate(pos[0], pos[1], pos[2])
    transform.RotateX(ang1)
    transform.RotateY(-ang2)
    transformNode.SetMatrixTransformToParent(transform.GetMatrix())


#
# ManualPlanningTest
#

class ManualPlanningTest(ScriptedLoadableModuleTest):
  """
  This is the test case for your scripted module.
  Uses ScriptedLoadableModuleTest base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def setUp(self):
    """ Do whatever is needed to reset the state - typically a scene clear will be enough.
    """
    slicer.mrmlScene.Clear()

  def runTest(self):
    """Run as few or as many tests as needed here.
    """
    self.setUp()
    self.test_ManualPlanning1()

  def test_ManualPlanning1(self):
    """ Ideally you should have several levels of tests.  At the lowest level
    tests should exercise the functionality of the logic with different inputs
    (both valid and invalid).  At higher levels your tests should emulate the
    way the user would interact with your code and confirm that it still works
    the way you intended.
    One of the most important features of the tests is that it should alert other
    developers when their changes will have an impact on the behavior of your
    module.  For example, if a developer removes a feature that you depend on,
    your test should break so they know that the feature is needed.
    """

    self.delayDisplay("Starting the test")

    # Get/create input data

    import SampleData
    registerSampleData()
    inputVolume = SampleData.downloadSample('ManualPlanning1')
    self.delayDisplay('Loaded test data set')

    inputScalarRange = inputVolume.GetImageData().GetScalarRange()
    self.assertEqual(inputScalarRange[0], 0)
    self.assertEqual(inputScalarRange[1], 695)

    outputVolume = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
    threshold = 100

    # Test the module logic

    logic = ManualPlanningLogic()

    # Test algorithm with non-inverted threshold
    logic.process(inputVolume, outputVolume, threshold, True)
    outputScalarRange = outputVolume.GetImageData().GetScalarRange()
    self.assertEqual(outputScalarRange[0], inputScalarRange[0])
    self.assertEqual(outputScalarRange[1], threshold)

    # Test algorithm with inverted threshold
    logic.process(inputVolume, outputVolume, threshold, False)
    outputScalarRange = outputVolume.GetImageData().GetScalarRange()
    self.assertEqual(outputScalarRange[0], inputScalarRange[0])
    self.assertEqual(outputScalarRange[1], inputScalarRange[1])

    self.delayDisplay('Test passed')
