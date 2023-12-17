import requests
from bs4 import BeautifulSoup

def write_headings_to_file(file_path,headings):
    

    with open(file_path,"w") as Harpaphe_haydeniana_file:
        Harpaphe_haydeniana_file.write(p)

        for heading in headings:
            Harpaphe_haydeniana_file.write(heading)
            

            #print(heading)
            #news_file.write("\n")
            #news_file.write("\n")

#url="https://www.reuters.com/world/us/"
#url="https://www.youtube.com/watch?v=ErGApg0Ef_U"
#url="https://www.reuters.com/world/japan/"
url="https://en.wikipedia.org/wiki/Harpaphe_haydeniana"
response = requests.get(url)

print(response.status_code)

if response.status_code == 200:
    content=response.content
    #print(content)

    soup=BeautifulSoup(content,'html.parser')
    #headings=soup.select('span[class="mw-headline"]')
    headings=soup.select('h2')
    #print(headings)
    
    heading_list = []
    
    
    for heading in headings:
        link=heading.select('span[class="mw-headline"]')
        #elink=link.find("span")
        #print(link.text)
        #print(link)

        if link is not None:
            text=link
            heading_list.append(text)
            #print(heading_list)
            #print(text)
            #b=str(text)
    c=str(heading_list)   
    p='HARPAPHE HAYDENIANA \n *Harpaphe haydeniana reach a length of 4–5 centimeters (1.6–2 in) when mature. \n *The upper surface of the body is black to olive green, and is distinctively marked along the sides with patches of a yellowish colour. \n *H. haydeniana has approximately twenty body segments, bearing a total of 30 (males) or 31 (females) pairs of legs. \n *The difference between males and females is due to one pair of legs on the seventh segment in males being modified to form gonopods used for sperm transfer.\n *Individuals may live for 2–3 years.[1]\n\n\n'
    #print(headings)

    write_headings_to_file('C:\\Users\\Public\\Documents\\Harpaphe_haydeniana.txt',c)
    
    


