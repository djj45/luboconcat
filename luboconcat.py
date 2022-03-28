import os
import shutil

L = []

def isflv():
    for file in os.listdir():
        if file.endswith("flv"):
            return True


def mkdir(flvflag):
    if os.path.exists("_flv_"):
        shutil.rmtree("_flv_")
    if os.path.exists("_m4a_"):
        shutil.rmtree("_m4a_")
    if os.path.exists("output.mp4"):
        os.remove("output.mp4")
    if flvflag:
        os.mkdir("_flv_")
    os.mkdir("_m4a_")





def convert():
    for file in os.listdir():
        if file.endswith("flv"):
            name = file.split(".")[0]
            mp4 = "ffmpeg -hide_banner -y -i " + '"' + file + '"' + " -an -c copy " + './_flv_/"' + name + '.mp4"'
            m4a = (
                "ffmpeg -hide_banner -y -i " + '"' + file + '"' + " -vn -c copy " + './_m4a_/"' + name + '.m4a"'
            )
            os.system(mp4)
            os.system(m4a)
            L.append(file)
        if file.endswith("mp4"):
            name = file.split(".")[0]
            m4a = (
                "ffmpeg -hide_banner -y -i " + '"' + file + '"' + " -vn -c copy " + './_m4a_/"' + name + '.m4a"'
            )
            os.system(m4a)
            L.append(file)


L.sort(key=lambda x: int(x.split("-")[3].replace(".mp4", "").replace(".flv", "")))


def writetxt(flvflag):
    if flvflag:
        with open("./_flv_/flv.txt", "w", encoding="utf-8") as flv:
            with open("./_m4a_/m4a.txt", "w", encoding="utf-8") as m4a:
                for file in L:
                    flv.write("file '.\\" + file.replace("flv", "mp4") + "'" + "\n")
                    m4a.write("file '.\\" + file.replace("flv", "m4a") + "'" + "\n")
                m4a.close()
            flv.close()
    else:
        with open("mp4.txt", "w", encoding="utf-8") as mp4:
            with open("./_m4a_/m4a.txt", "w", encoding="utf-8") as m4a:
                for file in L:
                    mp4.write("file '.\\" + file+ "'" + "\n")
                    m4a.write("file '.\\" + file.replace("mp4", "m4a") + "'" + "\n")
                m4a.close()
            mp4.close()


def concat(flvflag):
    if flvflag:
        os.system("ffmpeg -hide_banner -y -f concat -safe 0 -i ./_flv_/flv.txt -c copy ./_flv_/temp.mp4")
        os.system("ffmpeg -hide_banner -y -f concat -safe 0 -i ./_m4a_/m4a.txt -c copy ./_m4a_/temp.m4a")
        os.system("ffmpeg -hide_banner -y -i ./_flv_/temp.mp4 -i ./_m4a_/temp.m4a -map 0:0 -map 1:0 -c copy output.mp4")
    else:
        os.system("ffmpeg -hide_banner -y -f concat -safe 0 -i mp4.txt -c copy temp.mp4")
        os.system("ffmpeg -hide_banner -y -f concat -safe 0 -i ./_m4a_/m4a.txt -c copy ./_m4a_/temp.m4a")
        os.system("ffmpeg -hide_banner -y -i temp.mp4 -i ./_m4a_/temp.m4a -map 0:0 -map 1:0 -c copy output.mp4")


def delete(flvflag):
    if flvflag:
        shutil.rmtree("_flv_")
        shutil.rmtree("_m4a_")
    else:
        shutil.rmtree("_m4a_")
        os.remove("temp.mp4")
        os.remove("mp4.txt")

if __name__ == "__main__":
    flvflag = isflv()
    mkdir(flvflag)
    convert()
    writetxt(flvflag)
    concat(flvflag)
    delete(flvflag)