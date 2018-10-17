import json
import os

img_file = 'D:\\Humanoid\\squeezeDet\\Embedded_Object_Detection\\dataset\\images.txt'
gt_dir = 'D:\\Humanoid\\squeezeDet\\Embedded_Object_Detection\\dataset\\annotations\\ann_train_clean.json'
path = 'D:\\Humanoid\\squeezeDet\\Embedded_Object_Detection\\dataset\\training\\label_2\\'

CLASS_ID = {'1':'person','2':'bicycle','3': 'car','4':'motorcycle','5': 'airplane','6':'bus','7':'train','8':'truck','9':'boat','10':'traffic_light',
            '11':'fire_hydrant','13':'stop_sign','14':'parking_meter','15':'bench','16':'bird','17':'cat','18':'dog','19':'horse','20':'sheep',
            '21':'cow','22':'elephant','23':'bear','24':'zebra','25':'giraffe','27':'backpack','28':'umbrella','31':'handbag','32':'tie','33':'suitcase',
            '34':'frisbee','35':'skis','36':'snowboard','37':'sports_ball','38':'kite','39':'baseball_bat','40':'baseball_glove','41':'skateboard',
            '42':'surfboard','43':'tennis_racket','44':'bottle','46':'wine_glass','47':'cup','48':'fork','49':'knife','50':'spoon','51':'bowl',
            '52':'banana','53':'apple','54':'sandwich','55':'orange','56':'broccoli','57':'carrot','58':'hot_dog','59':'pizza','60':'donut','61':'cake',
            '62':'chair','63':'couch','64':'potted_plant','65':'bed','67':'dining_table','70':'toilet','72':'tv','73':'laptop','74':'mouse','75':'remote',
            '76':'keyboard','77':'cell_phone','78':'microwave','79':'oven','80':'toaster','81':'sink','82':'refrigerator','84':'book','85':'clock',
            '86':'vase','87':'scissors','88':'teddy_bear','89':'hair_drier','90':'toothbrush'}
        

with open(img_file,'r') as imgs:
    img_names = imgs.read().splitlines()
imgs.close()

with open(gt_dir,'r') as f:
    data = json.load(f)
f.close()

for img_name in img_names:
    txt = path + img_name[-16:-4] + ".txt"
    f = open(txt,"w+")     
    for ann in data[img_name]:
        x, y, w, h = ann[:4]
        xmin = x
        ymin = y
        xmax = x + w
        ymax = y + h     
        f.write(CLASS_ID[str(ann[4])] + " " + str(xmin) + " " + str(ymin)+ " " + str(xmax)+ " " + str(ymax) + "\n")
    f.close()

print("Acabou!")