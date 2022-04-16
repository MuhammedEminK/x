
import argparse
import time

parser = argparse.ArgumentParser(description="nabersiniz")


parser.add_argument("-f","--file", help="file")
parser.add_argument("-k","--keywords", help="keyword")
parser.add_argument("-c","--capitalize", action='store_true', help="capitalize")
parser.add_argument("-p", "--phone", help="phone")
parser.add_argument("-punc","--punctuation",help="special arguman")
parser.add_argument("-num","--numeric",help="numeric")

arg = parser.parse_args()

keywords = []
start = time.time()
if arg.file:
    with open(f"{arg.file}",mode="a",encoding="utf-8") as file:
        if arg.keywords:
            spl = (arg.keywords).split(";")
            for keyword in spl:
                file.write("%s \n" %keyword)
            if arg.capitalize:
                for keyword in spl:
                    file.write("%s \n" %str(keyword).capitalize())
            if arg.phone:
                for phone in arg.phone.split(";"):
                    if str(phone).startswith("0"):file.write("%s\n"%phone),file.write("%s\n"%phone[1:])
                    if not(phone.startswith("0")): file.write("%s\n"%phone),file.write("0%s\n"%phone)
            if arg.numeric: 
                for keyword in spl:
                    for numeric in arg.numeric.split(";"):
                        file.write(f"{keyword}{numeric}\n")
                        file.write(f"{numeric}{keyword}\n")
                        file.write(f"{numeric}{keyword}{numeric}\n")
                        if arg.capitalize:
                            file.write(f"{keyword.capitalize()}{numeric}\n")
                            file.write(f"{numeric}{keyword.capitalize()}\n")
                            file.write(f"{numeric}{keyword.capitalize()}{numeric}\n")

                        if arg.punctuation:
                            x = ['!', "'", '^', '+', '%', '&', '/', '(', ')', '=', '?', '_', '>', '£', '#', '$', '½', '{', '[', ']', '}', '\\', '|', '@', '€', '₺', '¨', '~', '`', '´', 'ß', 'æ', '|', '>', '<', '`', '"', "'"]

                            if arg.punctuation.casefold() == "all" or arg.punctuation.casefold() == "*":
                                for keyword in spl:
                                    for noktalama in x:
                                        file.write(f"{keyword}{noktalama}\n")
                                        file.write(f"{keyword}{numeric}{noktalama}\n")
                                        file.write(f"{noktalama}{keyword}{noktalama}\n")
                                if arg.capitalize:
                                    for keyword in spl:
                                        for noktalama in x:
                                            file.write(f"{keyword.capitalize()}{noktalama}\n")
                                            file.write(f"{keyword.capitalize()}{numeric}{noktalama}\n")
                                            file.write(f"{noktalama}{keyword.capitalize()}{noktalama}\n")

                            else:
                                for i in arg.punctuation.split(";"):
                                    for keyword in spl:
                                        for noktalama in i:
                                            file.write(f"{keyword}{noktalama}\n")
                                            file.write(f"{keyword}{numeric}{noktalama}\n")
                                            file.write(f"{noktalama}{keyword}{noktalama}\n")
                                if arg.capitalize:
                                    for keyword in spl:
                                        for noktalama in i:
                                            file.write(f"{keyword.capitalize()}{noktalama}\n")
                                            file.write(f"{keyword.capitalize()}{numeric}{noktalama}\n")
                                            file.write(f"{noktalama}{keyword.capitalize()}{noktalama}\n")

print(f"Total Time:{time.time()-start}")
                    
