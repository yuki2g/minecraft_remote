from mcje.minecraft import Minecraft
import param_MCJE as param

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat("kadai1")

mc.setBlock(5, 70, 5, param.SEA_LANTERN_BLOCK)