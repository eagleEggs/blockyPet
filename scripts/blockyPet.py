from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create() #set create function to mc

blockType = 3 # set blocktype number (grass, lava, etc...)
amount = 33
steps=  0
hungry = 0

pos =mc.player.getPos() # get player position
mc.setBlock(pos.x+2,pos.y,pos.z, blockType)
while (amount >= 0):
    
    if steps >= 300:
        hungry = 1
    
    pos2 = mc.player.getPos()
    if pos2.x > pos.x:
        #mc.setBlock(x+2,y+jump,z, 0)
        checkBlockX = mc.getBlock(pos.x+1,pos.y,pos.z)
        if checkBlockX == 0:
            mc.setBlock(pos.x+1,pos.y,pos.z, blockType)
            steps = steps + 1
            time.sleep(0.3)
            mc.setBlock(pos.x+1,pos.y,pos.z, 0)
            pos.x = pos.x+1
        else:
            if hungry == 1:
                mc.setBlock(pos.x+1,pos.y,pos.z, 0)
                mc.setBlock(pos.x+1,pos.y,pos.z, blockType)
                steps = 0
                hungry = 0
                mc.postToChat('Yummy thank you!')
    if pos2.x < pos.x:
        checkBlockX2 = mc.getBlock(pos.x-1,pos.y,pos.z)
        if checkBlockX2 == 0:
            mc.setBlock(pos.x-1,pos.y,pos.z, blockType)
            steps = steps + 1
            time.sleep(0.3)
            mc.setBlock(pos.x-1,pos.y,pos.z, 0)
            pos.x = pos.x -1
        else:
            if hungry == 1:
                mc.setBlock(pos.x-1,pos.y,pos.z, 0)
                mc.setBlock(pos.x-1,pos.y,pos.z, blockType)
                steps = 0
                hungry = 0
                mc.postToChat('Yummy thank you!')
    if pos2.y > pos.y:
        checkBlockY = mc.getBlock(pos.x,pos.y+1,pos.z)
        if checkBlockY == 0:
            mc.setBlock(pos.x,pos.y+1,pos.z, blockType)
            steps = steps + 1
            time.sleep(0.3)
            mc.setBlock(pos.x,pos.y+1,pos.z, 0)
            pos.y = pos.y+1
        else:
            if hungry == 1:
                mc.setBlock(pos.x,pos.y+1,pos.z, 0)
                mc.setBlock(pos.x,pos.y+1,pos.z, blockType)
                steps = 0
                hungry = 0
                mc.postToChat('Yummy thank you!')
    if pos2.y < pos.y:
        checkBlockY2 = mc.getBlock(pos.x,pos.y-1,pos.z)
        if checkBlockY2 == 0:
            mc.setBlock(pos.x,pos.y-1,pos.z, blockType)
            steps = steps + 1
            time.sleep(0.3)
            mc.setBlock(pos.x,pos.y-1,pos.z, 0)
            pos.y = pos.y -1
        else:
            if hungry == 1:
                mc.setBlock(pos.x,pos.y-1,pos.z, 0)
                mc.setBlock(pos.x,pos.y-1,pos.z, blockType)
                steps = 0
                hungry = 0
                mc.postToChat('Yummy thank you!')
    if pos2.z > pos.z:
        checkBlockZ = mc.getBlock(pos.x,pos.y,pos.z+1)
        if checkBlockZ == 0:
            mc.setBlock(pos.x,pos.y,pos.z+1, blockType)
            steps = steps + 1
            time.sleep(0.3)
            mc.setBlock(pos.x,pos.y,pos.z+1, 0)
            pos.z = pos.z+1
        else:
            if hungry == 1:
                mc.setBlock(pos.x,pos.y,pos.z+1, 0)
                mc.setBlock(pos.x,pos.y,pos.z+1, blockType)
                steps = 0
                hungry = 0
                mc.postToChat('Yummy thank you!')
    if pos2.z < pos.z:
        checkBlockZ2 = mc.getBlock(pos.x,pos.y,pos.z-1)
        if checkBlockZ2 ==0:
            mc.setBlock(pos.x,pos.y,pos.z-1, blockType)
            steps = steps + 1
            time.sleep(0.3)
            mc.setBlock(pos.x,pos.y,pos.z-1, 0)
            pos.z = pos.z -1
        else:
            if hungry == 1:
                mc.setBlock(pos.x,pos.y,pos.z-1, 0)
                mc.setBlock(pos.x,pos.y,pos.z-1, blockType)
                steps = 0
                hungry = 0
                mc.postToChat('Yummy thank you!')
