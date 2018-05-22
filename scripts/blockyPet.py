from mcpi.minecraft import Minecraft
import time
import random

mc=Minecraft.create() #set create function to mc

blockType = 3 # set blocktype number (grass, lava, etc...)
amount = 33
steps=  0
hungry = 0

# code to have pet blocky follow you around!!!

pos =mc.player.getPos() # get player position
mc.setBlock(pos.x+2,pos.y,pos.z, blockType)
setHungry = 0
while (amount >= 0):
    
    if steps >= 1000 and setHungry == 0:
        setHungry = 1
        petFood = random.randint(2,9)
        if petFood == 2:
            food = str('grass')
        if petFood == 3:
            food = str('dirt')
        if petFood == 4:
            food = str('cobblestone')
        if petFood == 5:
            food = str('woodPlanks')
        if petFood == 6:
            food = str('sappling')
        if petFood == 7:
            food = str('water')
            petFood=8
        if petFood == 8:
            food = str('water')
        mc.postToChat('Blocky is hungry for ' +food)
        hungry = 1
    
    if hungry == 0:
        fatigue = 0.3
    else:
        if hungry ==1:
            fatigue = 1
    
    pos2 = mc.player.getPos()
    if pos2.x > pos.x +2 and pos.x -2 != pos2.x:
        #mc.setBlock(x+2,y+jump,z, 0)
        checkBlockX = mc.getBlock(pos.x+1,pos.y,pos.z)
        if checkBlockX == 0:
            #mc.postToChat('Move > x')
            mc.setBlock(pos.x+1,pos.y,pos.z, blockType)
            steps = steps + 1
            time.sleep(fatigue)
            mc.setBlock(pos.x+1,pos.y,pos.z, 0)
            pos.x = pos.x+1
        else:
            if hungry == 1 and checkBlockX == petFood:
                mc.setBlock(pos.x+1,pos.y,pos.z, 0)
                #mc.setBlock(pos.x+1,pos.y,pos.z, blockType)
                steps = 0
                hungry = 0
                setHungry = 0
                mc.postToChat('Yummy thank you!')
    if pos2.x < pos.x-2 and pos.x +2 != pos2.x:
        checkBlockX2 = mc.getBlock(pos.x-1,pos.y,pos.z)
        if checkBlockX2 == 0:
            #mc.postToChat('Move < x')
            mc.setBlock(pos.x-1,pos.y,pos.z, blockType)
            steps = steps + 1
            time.sleep(fatigue)
            mc.setBlock(pos.x-1,pos.y,pos.z, 0)
            pos.x = pos.x -1
        else:
            if hungry == 1 and checkBlockX2== petFood:
                mc.setBlock(pos.x-1,pos.y,pos.z, 0)
                #mc.setBlock(pos.x-1,pos.y,pos.z, blockType)
                steps = 0
                hungry = 0
                setHungry = 0
                mc.postToChat('Yummy thank you!')
    if pos2.y > pos.y:
        checkBlockY = mc.getBlock(pos.x,pos.y+1,pos.z)
        if checkBlockY == 0:
            #mc.postToChat('Move > y')
            mc.setBlock(pos.x,pos.y+1,pos.z, blockType)
            steps = steps + 1
            time.sleep(fatigue)
            mc.setBlock(pos.x,pos.y+1,pos.z, 0)
            pos.y = pos.y+1
        else:
            if hungry == 1 and checkBlockY == petFood:
                mc.setBlock(pos.x,pos.y+1,pos.z, 0)
                #mc.setBlock(pos.x,pos.y+1,pos.z, blockType)
                steps = 0
                hungry = 0
                setHungry = 0
                mc.postToChat('Yummy thank you!')
    if pos2.y < pos.y:
        checkBlockY2 = mc.getBlock(pos.x,pos.y-1,pos.z)
        if checkBlockY2 == 0:
            #mc.postToChat('Move < y')
            mc.setBlock(pos.x,pos.y-1,pos.z, blockType)
            steps = steps + 1
            time.sleep(fatigue)
            mc.setBlock(pos.x,pos.y-1,pos.z, 0)
            pos.y = pos.y -1
        else:
            if hungry == 1 and checkBlockY2 == petFood:
                mc.setBlock(pos.x,pos.y-1,pos.z, 0)
                #mc.setBlock(pos.x,pos.y-1,pos.z, blockType)
                steps = 0
                hungry = 0
                setHungry = 0
                mc.postToChat('Yummy thank you!')
    if pos2.z > pos.z and pos.z+1 != pos2.z:
        checkBlockZ = mc.getBlock(pos.x,pos.y,pos.z+1)
        if checkBlockZ == 0:
            #mc.postToChat('Move > z')
            mc.setBlock(pos.x,pos.y,pos.z+1, blockType)
            steps = steps + 1
            time.sleep(fatigue)
            mc.setBlock(pos.x,pos.y,pos.z+1, 0)
            pos.z = pos.z+1
        else:
            if hungry == 1 and checkBlockZ== petFood:
                mc.setBlock(pos.x,pos.y,pos.z+1, 0)
                #mc.setBlock(pos.x,pos.y,pos.z+1, blockType)
                steps = 0
                hungry = 0
                setHungry = 0
                mc.postToChat('Yummy thank you!')
    if pos2.z < pos.z and pos.z -1 != pos2.z:
        checkBlockZ2 = mc.getBlock(pos.x,pos.y,pos.z-1)
        if checkBlockZ2 ==0:
            #mc.postToChat('Move < z')
            mc.setBlock(pos.x,pos.y,pos.z-1, blockType)
            steps = steps + 1
            time.sleep(fatigue)
            mc.setBlock(pos.x,pos.y,pos.z-1, 0)
            pos.z = pos.z -1
        else:
            if hungry == 1 and checkBlockZ2 == petFood:
                mc.setBlock(pos.x,pos.y,pos.z-1, 0)
                #mc.setBlock(pos.x,pos.y,pos.z-1, blockType)
                steps = 0
                hungry = 0
                setHungry = 0
                mc.postToChat('Yummy thank you!')
