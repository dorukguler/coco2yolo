import json

path = "/coco/annotations/instances_val2017.json"
f = open(path)
anns = json.load(f)

# # print(anns.keys())
# print(anns['images'])
# # print(anns['info'])
# print(anns['categories'])
print(anns['annotations'])

# for anno in anns['annotations']:
#     print(anno)

# for category in anns["categories"]:
#     print(category["name"])


