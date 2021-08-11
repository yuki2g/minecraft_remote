from mcje.minecraft import Minecraft
import param_MCJE as param
import time

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat("kadai2")
x, z = (5, 10)
y = 70
for i in range(10):
mc.setBlock(x, y, z, GOLD_BLOCK)
time.sleep(0.3)
y = y + 1
print(y)

mc.postToChat("できた!")