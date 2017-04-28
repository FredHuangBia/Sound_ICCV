from short_write_sub_html import *
'''
classes = []
name_classes = []
class_path = "shortlist.txt"
class_file = open(class_path, "r")
index=-1
for line in class_file.readlines():
    line = line.split()
    if len(line)==0:
        continue
    if line[0] == '#':
        name_classes.append(str(line[1]))
        classes.append([])
        index+=1
        continue
    classes[index].append(int(line[0]))

t=0
for cla in classes:
    t+=len(cla)
print(t)
'''

html_path = "demo.html"
# home page
html = open(html_path, "w")
html.write("<html>\n")
glob2loc={}
loc2glob={}
loc2glob_file = open("/data/vision/billf/object-properties/sound/sound/exp/objects/final100/index2glob_index.txt","r")
for line in loc2glob_file:
    line = line.split()
    loc2glob[int(line[0])] = int(line[1])
    glob2loc[int(line[1])] = int(line[0])
loc2glob_file.close()


'''
# write links
for index in range(len(classes)):
    write_sub_html(name_classes[index],classes[index])
    html.write("<a href=\"sub_websites/" + name_classes[index] + ".html" + "\"><h1>" + name_classes[index] + "</h1></a>")
'''
for index in range(41):
    write_split(index)
    html.write("<a href=\"sub_websites/split-" + str(index) + ".html" + "\"><h1>" + "split-" + str(index) + "</h1></a>")


# The main body
html.write("\t<table>\n")
for i in range(164):
    # orig objects
    num_imgs = 2
    path = "imgs/orig/"
    html.write("\t\t<tr>\n")
    html.write("\t\t\t<td>\n")
#    html.write("<h1>"+str(i)+":" + str(loc2glob[i]) + "</h1>\n")
    html.write("<h1>"+str(i)+ "</h1>\n")
    html.write("\t\t\t</td>\n")
    for j in range(num_imgs):
        img_path = path+str(i)+"_"+str(j)+str(".png")
        html.write("\t\t\t<td>\n")
        html.write("\t\t\t\t<img src=\"%s\" alt=\"%s\" width=\"580\" height=\"270\"/>\n" % (img_path,img_path))
        html.write("\t\t\t</td>\n")

    # isostuffer outputs
    for r in range(5,8,1):
        for l in range(2,5,1):
            RaLb = "imgs/" + "R" + str(r) + "L" + str(l) + "/"
            RaLb_path = RaLb+str(i)+"_R" + str(r) + "L" + str(l) + ".png"
            html.write("\t\t\t<td>\n")
            html.write("\t\t\t\t<img src=\"%s\" alt=\"%s\" width=\"580\" height=\"270\"/>\n" % (RaLb_path,RaLb_path))
            html.write("\t\t\t</td>\n")
    html.write("\t\t</tr>\n")

    # write annotations for every obj
    html.write("\t\t<tr>\n")
    html.write("\t\t\t<td><h1 style=\"text-align:center\"></h1>\n")
    html.write("\t\t\t</td>\n")
    html.write("\t\t\t<td><h1 style=\"text-align:center\">" + str(i) + "_orig1</h1>\n")
    html.write("\t\t\t</td>\n")
    html.write("\t\t\t<td><h1 style=\"text-align:center\">" + str(i) + "_orig2</h1>\n")
    html.write("\t\t\t</td>\n")
    for r in range(5,8,1):
        for l in range(2,5,1):
            html.write("\t\t\t<td><h1 style=\"text-align:center\">" + str(i) + "_R" + str(r) + "L" + str(l) + "  v:"+str(10)+"  s:"+str(10)  +"</h1>\n")
            html.write("\t\t\t</td>\n")
    html.write("\t\t</tr>\n\t\t<tr>\n\t\t\t<td>\n\t\t\t\t<br>\n\t\t\t</td>\n\t\t</tr>\n")

html.write("\t</table>\n")

html.write("</html>\n")
html.close()
