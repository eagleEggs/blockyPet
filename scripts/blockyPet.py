from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create() #set create function to mc

blockType = 3

pos =mc.player.getPos()
mc.setBlock(pos.x+2,pos.y,pos.z, blockType)
while (amount >= 0):

    
    pos2 = mc.player.getPos()
    if pos2.x > pos.x:
        #mc.setBlock(x+2,y+jump,z, 0)
        mc.setBlock(pos.x+1,pos.y,pos.z, blockType)
        time.sleep(0.3)
        mc.setBlock(pos.x+1,pos.y,pos.z, 0)
        pos.x = pos.x+1
    if pos2.y > pos.y:
        mc.setBlock(pos.x,pos.y+1,pos.z, blockType)
        time.sleep(0.3)
        mc.setBlock(pos.x,pos.y+1,pos.z, 0)
        pos.y = pos.y+1
    if pos2.z > pos.z:
        mc.setBlock(pos.x,pos.y,pos.z+1, blockType)
        time.sleep(0.3)
        mc.setBlock(pos.x,pos.y,pos.z+1, 0)
        pos.z = pos.z+1
    if pos2.x < pos.x:
        mc.setBlock(pos.x-1,pos.y,pos.z, blockType)
        time.sleep(0.3)
        mc.setBlock(pos.x-1,pos.y,pos.z, 0)
        pos.x = pos.x -1
    if pos2.y < pos.y:
        mc.setBlock(pos.x,pos.y-1,pos.z, blockType)
        time.sleep(0.3)
        mc.setBlock(pos.x,pos.y-1,pos.z, 0)
        pos.y = pos.y -1
    if pos2.z < pos.z:
        mc.setBlock(pos.x,pos.y,pos.z-1, blockType)
        time.sleep(0.3)
        mc.setBlock(pos.x,pos.y,pos.z-1, 0)
        pos.z = pos.z -1
