import cv2

import os

mainFolder = 'Image'
myFolders = os.listdir(mainFolder)
print(myFolders)

for folder in myFolders:
    path = mainFolder + '/' +folder
    #print(path)
    images = []
    myList = os.listdir(path)
    print(f'Total number of image detected  {len(myList)}')
    for imgN in myList:
        curImg = cv2.imread(f'{path}/{imgN}')
        curImg = cv2.resize(curImg,(0,0),None,0.2, 0.2)
        images.append(curImg)
    #print(len(images))
    stitcher = cv2.Stitcher.create()
    (status,result) = stitcher.stitch(images)
    if (status == cv2.Stitcher_OK):
        print ('Generation success')
        cv2.imshow(folder, result)
        cv2.waitKey(1)
    else:
        print('Generation Error')
cv2.waitKey(0)








