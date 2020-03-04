import jinja2,time 

def split_data(Ertq):
    try:
        splitted = Ertq.split("   ")
        splt = splitted[0]
        splt1 = splt.split(" ")
        splt2 = splitted[1]
        splt3 = splitted[3]
        splt4 = splitted[5]
        splt5 = splitted[6]
        tarih = splt1[0]
        saat = splt1[1]
        enlem = splt1[3]
        boylam = splt2
        derinlik = splt3.strip("  ")
        buyukluk = splt4.strip(" -.-").split(" ")[0]
        yer = splt5
        data = {
            "tarih" : tarih,
            "saat" : saat,
            "enlem" : enlem,
            "boylam" : boylam,
            "derinlik" : derinlik,
            "buyukluk" : buyukluk,
            "yer" : yer,}
        return data
    except Exception as e:
        with open("errors.txt","a") as fp:
            fp.write("Error time : " + time.asctime() + "\n")
            fp.write("Error : " + e + "\n")
            fp.write("Error File : resources.py \n")
            fp.write("--------------------- \n")
            fp.close()
def get_message(data):
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template("template.html")
    message = template.render(tarih=data["tarih"],saat=data["saat"],enlem=data["enlem"],boylam=data["boylam"],derinlik=data["derinlik"],buyukluk=data["buyukluk"],yer=data["yer"])
    return message