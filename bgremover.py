#Python program for bgremover

import pixellib
from pixellib.tune_bg import alter_bg

change_bg=alter_bg()
change_bg.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
change_bg.color_bg("Dybala.png",colors=(0,128,0),output_image_name="bg.jpg")