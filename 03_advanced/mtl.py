import maya.cmds as cmds

#FUNCTION to assign mtl name
def assign_material_name():
    # ACCESS created text field
    material_name  = cmds.textField('Material Name', query=True, text=True) # Not working right now :( # Error: RuntimeError: file <maya console> line 6: Object 'Material Name' not found. # 
    
    selection = cmds.ls(sl = True, dag = True, s = True)

    for obj in selection:
        shadeEng = cmds.listConnections(obj, type= "shadingEngine")
        materials = cmds.ls(cmds.listConnections(shadeEng ), materials = True)
        cmds.setAttr(materials, material_name)


class Window(object):
    def __init__(self):
    self.ui_title = "material_organizer"
    if cmds.window(ui_title, exists=True):
        print('CLOSE duplicate window')
        cmds.deleteUI(ui_title)
        
    self.window = cmds.window(ui_title, title="Material Organizer")
    
    cmds.columnLayout(adjustableColumn=True)
    
    
    cmds.rowLayout(numberOfColumns=2)

    cmds.text(label='Material Name', width=530, height=30)
    cmds.text(label='Tags', width=530, height=30)

    cmds.setParent('..')    # this "closes" the current layout

    # CREATE string field
    cmds.textField('Material Name', height=30, text='Name')
    cmds.textField('Material Tags', height=30, text='Tags')

    cmds.button(label='Save',command=("assign_material_name()"))
    #cmds.button(label='Cancel',
                #command=("deleteUI(window, window=True)"))

    cmds.showWindow(window)
material_organizer()