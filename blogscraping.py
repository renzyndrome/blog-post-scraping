import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://glr-blog.herokuapp.com/') # this is just my dummy blogging web app

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='post-entry')

# write the result on a csv file
with open('posts.csv', 'w') as csv_file: # change 'posts.csv' into your desired file name
    csv_writer = writer(csv_file)
    headers = ['Title', 'Link', 'Content']
    csv_writer.writerow(headers)

    for post in posts:
        title = post.find('h2').get_text()
        link = post.find('a')['href']
        content = post.select('p')[0].get_text()
        csv_writer.writerow([title, link, content])