# import requests
# from bs4 import BeautifulSoup
#
# s = []
#
#
# def get_data(url, x):
#     headers = {
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
#                       " (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
#     }
#     global s
#     req = requests.get(url, headers)
#     with open(f'project_{x}.html', 'w', encoding='UTF-8') as a:
#         a.write(req.text)
#     with open(f'project_{x}.html', 'r', encoding='UTF-8') as f:
#         src = f.read()
#     soup = BeautifulSoup(src, 'lxml')
#     div = [str(x).strip('<div class="position_title">').strip('</div>').strip('\n').strip(' ').rstrip('\n') for x in
#            soup.find_all('div', class_="position_title")]
#     s += div
#
#
# abc = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
#        'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я']
# for x in abc:
#     get_data(f'https://kupidonia.ru/spisok/spisok-suschestvitelnyh-russkogo-jazyka/bukva/{x}', x)
# with open('noun_Russian.txt', 'w', encoding='UTF-8') as file:
#     file.write('\n'.join(s))





