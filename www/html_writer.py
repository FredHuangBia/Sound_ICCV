from write_sub_html import *

classes = []
name_classes = []
class_path = "classes.txt"
class_file = open(class_path, "r")
for line in class_file.readlines():
    line = line.split()
    name_classes.append(str(line[0]))
    current_class = []
    for i in range(1,len(line),1):
        current_class.append(int(line[i]))
    classes.append(current_class)


html_path = "demo.html"
# home page
html = open(html_path, "w")
html.write("<html>\n")


# write links
for index in range(len(classes)):
    write_sub_html(name_classes[index],classes[index])
    html.write("<a href=\"sub_websites/" + name_classes[index] + ".html" + "\"><h1>" + name_classes[index] + "</h1></a>")

# The main body
html.write("\t<table>\n")
for i in range(100):
    # orig objects
    num_imgs = 2
    path = "imgs/orig/"
    html.write("\t\t<tr>\n")
    html.write("\t\t\t<td>\n")
    html.write("<h1>"+str(i)+"</h3>\n")
    html.write("\t\t\t</td>\n")
    for j in range(num_imgs):
        img_path = path+str(i)+"_"+str(j)+str(".png")
        html.write("\t\t\t<td>\n")
        html.write("\t\t\t\t<img src=\"%s\" alt=\"%s\" width=\"580\" height=\"270\"/>\n" % (img_path,img_path))
        html.write("\t\t\t</td>\n")

    # isostuffer outputs
    for r in range(9,8,1):
        r = 12-r
        for l in range(1,7,1):
            RaLb = "imgs/" + "R" + str(r) + "L" + str(l) + "/"
            RaLb_path = RaLb+str(i)+"_R" + str(r) + "L" + str(l) + ".png"
            html.write("\t\t\t<td>\n")
            html.write("\t\t\t\t<img src=\"%s\" alt=\"%s\" width=\"580\" height=\"270\"/>\n" % (RaLb_path,RaLb_path))
            html.write("\t\t\t</td>\n")
    html.write("\t\t</tr>\n")

    # start a new line
    # write annotations for every obj
    html.write("\t\t<tr>\n")
    html.write("\t\t\t<td><h1 style=\"text-align:center\"></h1>\n")
    html.write("\t\t\t</td>\n")
    html.write("\t\t\t<td><h1 style=\"text-align:center\">" + str(i) + "_orig1</h1>\n")
    html.write("\t\t\t</td>\n")
    html.write("\t\t\t<td><h1 style=\"text-align:center\">" + str(i) + "_orig2</h1>\n")
    html.write("\t\t\t</td>\n")
    for r in range(9,8,1):
        r = 12-r
        for l in range(1,7,1):
            html.write("\t\t\t<td><h1 style=\"text-align:center\">" + str(i) + "_R" + str(r) + "L" + str(l) + "  v:"+str(10)+"  s:"+str(10)  +"</h1>\n")
            html.write("\t\t\t</td>\n")
    html.write("\t\t</tr>\n\t\t<tr>\n\t\t\t<td>\n\t\t\t\t<br>\n\t\t\t</td>\n\t\t</tr>\n")

html.write("\t</table>\n")

html.write("</html>\n")
html.close()
