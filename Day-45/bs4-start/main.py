# from bs4 import BeautifulSoup
# with open('website.html') as f:
#     data = f.read()
#
# soup = BeautifulSoup(data, 'html.parser')
# all_anchor_tags= soup.find_all(name='a')
# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     # print(tag.get('href'))
#
# # heading = soup.find(name='h1', id='name').getText()
# # print(heading)
#
# # section_heading = soup.find(name='h3', class_='heading')
# # print(section_heading.getText())
#
# # company_url = soup.select_one(selector='p a')#css selector
# # print(company_url)

from bs4 import BeautifulSoup
import requests
response = requests.get(url='https://news.ycombinator.com/news')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find_all(name='a', class_='titlelink')
# print(articles)
article_texts= []
article_links= []
article_upvotes= []
for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.get('href'))

print(article_texts)
print(article_links)

article_upvote = soup.find_all(name='span', class_='score')
for upvote in article_upvote:
    article_upvotes.append(int(upvote.getText().strip('points')))
print(article_upvotes)
most_upvote = max(article_upvotes)
index_most = article_upvotes.index(most_upvote)
text_most = article_texts[index_most]
link_most = article_links[index_most]
print(text_most)
print(link_most)
