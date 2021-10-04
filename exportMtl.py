import os
from maya import cmds


def exportMtl(path='', shader_list=[]):
    f = open(path, 'a')

    for i in shader_list:
        rgb = cmds.getAttr('%s.baseColor' % i)[0]
        sg = cmds.listConnections('%s.outColor' % i, s=False, d=True)[0]
        f.write('newmtl %s\n' %(sg))
        f.write('illum 4\n')
        f.write('Kd %s %s %s\n' %(rgb[0], rgb[1], rgb[2]))
        f.write('Ka %s %s %s\n' %(rgb[0], rgb[1], rgb[2]))
        f.write('Tf %s %s %s\n' %(rgb[0], rgb[1], rgb[2]))
        f.write('Ni 0.00\n')
        
    f.write('newmtl initialShadingGroup\n')
    f.write('illum 4\n')
    f.write('Kd 0.50 0.50 0.50\n')
    f.write('Ka 0.00 0.00 0.00\n')
    f.write('Tf 1.00 1.00 1.00\n')
    f.write('Ni 1.00\n')

    f.close()


exportMtl(path='dir_path\hoge.mtl', shader_list=cmds.ls(type='aiStandardSurface'))
