import requests
from bs4 import BeautifulSoup 

with open('sample.html','r') as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
print(soup.title)
print(soup.title.string)

print(soup.find_all("div")[0])
for link in soup.find_all("a"):   
 print(link)

print(soup.select('div.italic')) 
print(soup.select('span.italic'))
print(soup.select('span#italic'))

for child in soup.find(class_='container').children:
   print(child)

for parent in soup.find(class_="container").parents:
   print(parent)

cont = soup.find(class_='container')
cont.name = 'span'
cont['class'] = 'my_class'
cont.string = 'i am a string'
print(cont.has_attr("id"))
print(cont.has_attr("class"))
print(cont)

# adding a new tag to the existing document 

ul_tag = soup.new_tag('ul')

li_tag = soup.new_tag('li')
li_tag.string = 'home'
ul_tag.append(li_tag)


li_tag = soup.new_tag('li')
li_tag.string = 'about'
ul_tag.append(li_tag)

soup.html.body.insert(0,ul_tag)
with open("modified_html.html",'w') as f:
   f.write(str(soup))

def has_class_but_not_attribute(tag):
   return(tag.has_attr('class') and not tag.has_attr('id')) 

result = soup.find_all(has_class_but_not_attribute)
for res in result:
 print (res,'\n\n') 


  