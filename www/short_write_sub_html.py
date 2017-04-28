def write_sub_html(name,objs):
    html_path = "sub_websites/" + name +".html"
    html = open(html_path, "w")
    html.write("<html>\n")
    html.write("<a href=\"../demo.html\"><h1>Home</h1></a>")
    html.write("\t<table>\n")
    for i in objs:
        # orig objects
        num_imgs = 2
        path = "../imgs/orig/"
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
        for r in range(5,8,1):
            for l in range(2,5,1):
                RaLb = "../imgs/" + "R" + str(r) + "L" + str(l) + "/"
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
                html.write("\t\t\t<td><h1 style=\"text-align:center\">" + str(i) + "_R" + str(r) + "L" + str(l) + "</h1>\n")
                html.write("\t\t\t</td>\n")
        html.write("\t\t</tr>\n\t\t<tr>\n\t\t\t<td>\n\t\t\t\t<br>\n\t\t\t</td>\n\t\t</tr>\n")

    html.write("\t</table>\n")
    html.write("</html>\n")
    html.close()

def write_split(split):
    obj_list_path = "/data/vision/billf/object-properties/sound/sound/exp/objects/random_selected_objects/split-"+str(split)+"/selected_list_"+str(split)+".txt"
    obj_list = open(obj_list_path, "r")
    num_split = sum(1 for line in obj_list)
    obj_list.close()
    rl2obj2vs = generate_dict(split)
    html_path = "sub_websites/split-" + str(split) +".html"
    html = open(html_path, "w")
    html.write("<html>\n")
    html.write("<a href=\"../demo.html\"><h1>Home</h1></a>")
    html.write("\t<table>\n")
    for i in range(num_split):
        # orig objects
        num_imgs = 2
        path = "../imgs/split-" + str(split) + "/orig/"
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
        for r in range(5,8,1):
            for l in range(2,5,1):
                RaLb = "../imgs/split-" +str(split) + "/R" + str(r) + "L" + str(l) + "/"
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
                try:
                    html.write("\t\t\t<td><h1 style=\"text-align:center\">" + str(i) + "_R" + str(r) + "L" + str(l) +" v:"+str(rl2obj2vs[str(r)+str(l)][i][0])+" s:"+str(rl2obj2vs[str(r)+str(l)][i][1])+ "</h1>\n")
                except:
                    html.write("\t\t\t<td><h1 style=\"text-align:center\">" + str(i) + "_R" + str(r) + "L" + str(l) +" v:???"+" s:???"+ "</h1>\n")
                    
                html.write("\t\t\t</td>\n")
        html.write("\t\t</tr>\n\t\t<tr>\n\t\t\t<td>\n\t\t\t\t<br>\n\t\t\t</td>\n\t\t</tr>\n")

    html.write("\t</table>\n")
    html.write("</html>\n")
    html.close()

def generate_dict(split):
    dic = {}
    VSRL = open("/data/vision/billf/object-properties/sound/sound/exp/objects/random_selected_objects/split-"+str(split)+"/stats.txt","r")
    currentRL = ''
    for line in VSRL:
        if line[0]=='R':
            currentRL = line[1]+line[3]
            dic[currentRL]={}
        elif len(line.split())>0:
            line=line.split()
            dic[currentRL][int(line[0])]=(line[1],line[2])
    return dic


# define class
# class category(objects=None,name,sub_category=None):
#     def __init__(self):
#         self.objects = objects
#         self.name = name
#         self.sub_category = sub_category
#         if self.objects == None:
#             self.objects=[]
#             for sub in sub_category:
#                 self.objects.append(obj for obj in sub.objects)
