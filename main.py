import requests
from bs4 import BeautifulSoup

def main():
    url = input()
    response = requests.get(url)
    f = open("output.txt",  "w")
    f.write(" ")
    f.close
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        if soup.find_all("title"):
            f = open("output.txt",  "a")
            f.write(soup.find("title").string)
            f.write("\n")
            f.close
        else:
            print ("\ntitle error")
        
        if soup.find_all("meta", attrs={"name": "description"}):
            f = open("output.txt",  "a")
            f.write(soup.find("meta", attrs={"name": "description"}).get("content"))
            f.write("\n")
            f.close
        else:
            print("\ndescription error")

    else:
        print("\nstatus error")

main()
