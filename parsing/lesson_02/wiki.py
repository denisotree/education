from requests import get
import re


def get_link(topic):
    link = "https://ru.wikipedia.org/wiki/" + topic.capitalize()
    return link


def get_topic_page(topic='', external_link=False):
    if not external_link:
        link = get_link(topic)
        html = get(link).text
    else:
        html = get(external_link).text
    return html


def get_next_link_page(topic):
    topic_html = get_topic_page(topic)
    links = re.findall(r"<a rel=[\"\'][\S]*[\"\'][^>]*href=[\'\"](http[s]*:[a-zа-я/.-]*)[\'\"]>", topic_html)
    link = links[0]
    external_page = get_topic_page(external_link=link)
    return external_page


def get_topic_text(topic):
    html_content = get_next_link_page(topic)
    words = re.findall("[а-яА-Я]{3,}", html_content)
    return words


def get_common_words(topic):
    words_list = get_topic_text(topic)
    rate = {}
    for word in words_list:
        if word in rate:
            rate[word] += 1
        else:
            rate[word] = 1
    rate_list = list(rate.items())
    rate_list.sort(key=lambda x: -x[1])

    return rate_list


def visualize_common_words(topic):
    words = get_common_words(topic)
    f = open(f'top_words_for_{topic}.txt', 'w')
    for w in words[0:10]:
        f.write(f'{w[0]} встречается {w[1]} раз\n')


topic = 'Батайск'

visualize_common_words(topic)


