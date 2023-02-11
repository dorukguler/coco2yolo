import json
import os
import shutil


input_path = "/coco/annotations/instances_val2017.json"
output_path = "/Users/doruk/PycharmProjects/coco2yolo/yolo_format"




f = open(input_path)
anns = json.load(f)

file_names = []

def load_images_from_folder(folder):
    count = 0
    for filename in os.listdir(folder):
            source = os.path.join(folder,filename)
            destination = f"{output_path}/images/img{count}.jpg"

            try:
                shutil.copy(source, destination)
                print("File copied successfully.")
        # If source and destination are same
            except shutil.SameFileError:
                print("Source and destination represents the same file.")

            file_names.append(filename)
            count += 1
    return file_names


# load_images_from_folder('/Users/doruk/PycharmProjects/coco2yolo/coco/images')




def get_img_ann(image_id):
    img_ann = []
    isFound = False
    for ann in anns['annotations']:
        if ann['image_id'] == image_id:
            img_ann.append(ann)
            isFound = True
    if isFound:
        return img_ann
    else:
        return None
get_img_ann(289343)