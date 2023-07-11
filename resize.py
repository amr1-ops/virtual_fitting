# -*- coding: utf-8 -*-
"""
Created on Sat May 20 21:14:01 2023

@author: aamr6
"""

import os
import cv2
imgctr=0

shirtFolderPath = "assets"
ShirtName = "mentgreen.png"
imgShirt = cv2.imread(os.path.join(shirtFolderPath, ShirtName), cv2.IMREAD_UNCHANGED)
imgShirt = cv2.resize(imgShirt, (270, 270))
img_name = "mentgreen.png"
cv2.imwrite(img_name, imgShirt)