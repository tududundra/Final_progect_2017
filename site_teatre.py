# coding: utf8
from flask import Flask
from flask import render_template, url_for, request, redirect
import os
from datetime import datetime, date, time
import time
import requests
import json
import re

app = Flask(__name__)

@app.route('/')
def main_page():
    main_url = url_for('main_page')
    if request.args:
        variant = request.args['variant']
        if variant == 'театр':
            return redirect(url_for('theatre'))
        elif variant == 'сцена':
            return redirect(url_for('scene'))
        elif variant == 'билет':
            return redirect(url_for('ticket'))
        elif variant == 'премьера':
            return redirect(url_for('prem'))
        elif variant == 'актер':
            return redirect(url_for('actor'))
        elif variant == 'зритель':
            return redirect(url_for('zrit'))
        elif variant == 'спектакль':
            return redirect(url_for('play'))
        elif variant == 'театральный':
            return redirect(url_for('teatral'))
    return render_template('main_page.html', main_url=main_url)

@app.route('/theatre')
def theatre():
    main_url = url_for('main_page')
    today_date_full = time.time()
    week_before = float(today_date_full) - 604800
    group_data = ''
    groups_arr = ['ТЕАТРЫ МОСКВЫ', 'ТЕАТР КВАРТЕТ И', 'Театр НИУ ВШЭ', 'Театр балета Бориса Эйфмана',
                  'Bolshoi Theatre of Russia / Большой театр России', 'Михайловский театр',
                  'Молодежный ТЕАТР НА БУЛАКЕ Казань', 'Пермский театр У Моста',
                  'Театральная Вешалка', 'ОДИН ТЕАТР', 'ВОЛКОВСКИЙ ТЕАТР', 'Театр Красный факел',
                  'Московский театр мюзикла',
                  'Санкт-Петербургский театр Мастерская']
    group_arr = ['moscowtheatres', 'kvartet_i', 'hsetheatre',
                 'eifmanballet', 'bolshoitheatre', 'mikhailovsky_theatre', 'teatrnabulake',
                 'teatrumosta', 'teatrpeterburg', 'odin_teatr', 'volkov_teatr',
                 'krasnii_fakel', 'teamuz',  'teatrkozlova']
    for off in group_arr:
        req = 'https://api.vk.com/method/wall.get?domain=' \
              + str(off) \
              + '&count=100&access_token=13438ccb13438ccb13438ccbcd131f4d1b1134313438ccb4a0aecff06982089e052b5e6'
        response = requests.get(req).text
        data = json.loads(response)
        i = 1
        key_teatr = 0
        while i <= 100:
            post_date = data["response"][i]["date"]
            if post_date > float(week_before):
                text = data["response"][i]["text"]
                key_teatr_finder = re.findall('((Т|т)еатр(а|у|ом|ами|ам|е|ы|ах|ов))', text)
                key_teatr += len(key_teatr_finder)
                i += 1
            else:
                group_data += '{"country": "' + groups_arr[group_arr.index(off)] + '","visits": ' + \
                              str(key_teatr) + ',"color": "#468ccf"},'
                break
    graph_teatr = '/**тут инфа*/' + group_data + '/**тут инфа кончилась*/'
    f = open('./static/graph1.js', 'r', encoding='UTF-8')
    js_text = f.read()
    f.close()
    js_text_new_1 = re.sub('\n', '', js_text)
    js_text_new = re.sub('/\*\*тут инфа\*/(.+)/\*\*тут инфа кончилась\*/', str(graph_teatr), js_text_new_1)
    fl = open('./static/graph1.js', 'w', encoding='UTF-8')
    fl.write(js_text_new)
    fl.close()
    return render_template('teatre_graph.html', main_url=main_url)

@app.route('/scene')
def scene():
    main_url = url_for('main_page')
    today_date_full = time.time()
    week_before = float(today_date_full) - 604800
    group_data = ''
    groups_arr = ['ТЕАТРЫ МОСКВЫ', 'ТЕАТР КВАРТЕТ И', 'Театр НИУ ВШЭ', 'Театр балета Бориса Эйфмана',
                  'Bolshoi Theatre of Russia / Большой театр России', 'Михайловский театр',
                  'Молодежный ТЕАТР НА БУЛАКЕ Казань', 'Пермский театр У Моста',
                  'Театральная Вешалка', 'ОДИН ТЕАТР', 'ВОЛКОВСКИЙ ТЕАТР', 'Театр Красный факел',
                  'Московский театр мюзикла',
                  'Санкт-Петербургский театр Мастерская']
    group_arr = ['moscowtheatres', 'kvartet_i', 'hsetheatre',
                 'eifmanballet', 'bolshoitheatre', 'mikhailovsky_theatre', 'teatrnabulake',
                 'teatrumosta', 'teatrpeterburg', 'odin_teatr', 'volkov_teatr',
                 'krasnii_fakel', 'teamuz',  'teatrkozlova']
    for off in group_arr:
        req = 'https://api.vk.com/method/wall.get?domain=' \
              + str(off) \
              + '&count=100&access_token=13438ccb13438ccb13438ccbcd131f4d1b1134313438ccb4a0aecff06982089e052b5e6'
        response = requests.get(req).text
        data = json.loads(response)
        i = 1
        key_teatr = 0
        while i <= 100:
            post_date = data["response"][i]["date"]
            if post_date > float(week_before):
                text = data["response"][i]["text"]
                key_teatr_finder = re.findall('((С|с)цен(а|у|ой|ами|ам|е|ы|ах))', text)
                key_teatr += len(key_teatr_finder)
                i += 1
            else:
                group_data += '{"country": "' + groups_arr[group_arr.index(off)] + '","visits": ' + \
                              str(key_teatr) + ',"color": "#468ccf"},'
                break
    graph_teatr = '/**тут инфа*/' + group_data + '/**тут инфа кончилась*/'
    f = open('./static/graph_scene.js', 'r', encoding='UTF-8')
    js_text = f.read()
    f.close()
    js_text_new_1 = re.sub('\n', '', js_text)
    js_text_new = re.sub('/\*\*тут инфа\*/(.+)/\*\*тут инфа кончилась\*/', str(graph_teatr), js_text_new_1)
    fl = open('./static/graph_scene.js', 'w', encoding='UTF-8')
    fl.write(js_text_new)
    fl.close()
    return render_template('scene_page.html', main_url=main_url)

@app.route('/ticket')
def ticket():
    main_url = url_for('main_page')
    today_date_full = time.time()
    week_before = float(today_date_full) - 604800
    group_data = ''
    groups_arr = ['ТЕАТРЫ МОСКВЫ', 'ТЕАТР КВАРТЕТ И', 'Театр НИУ ВШЭ', 'Театр балета Бориса Эйфмана',
                  'Bolshoi Theatre of Russia / Большой театр России', 'Михайловский театр',
                  'Молодежный ТЕАТР НА БУЛАКЕ Казань', 'Пермский театр У Моста',
                  'Театральная Вешалка', 'ОДИН ТЕАТР', 'ВОЛКОВСКИЙ ТЕАТР', 'Театр Красный факел',
                  'Московский театр мюзикла',
                  'Санкт-Петербургский театр Мастерская']
    group_arr = ['moscowtheatres', 'kvartet_i', 'hsetheatre',
                 'eifmanballet', 'bolshoitheatre', 'mikhailovsky_theatre', 'teatrnabulake',
                 'teatrumosta', 'teatrpeterburg', 'odin_teatr', 'volkov_teatr',
                 'krasnii_fakel', 'teamuz', 'teatrkozlova']
    for off in group_arr:
        req = 'https://api.vk.com/method/wall.get?domain=' \
              + str(off) \
              + '&count=100&access_token=13438ccb13438ccb13438ccbcd131f4d1b1134313438ccb4a0aecff06982089e052b5e6'
        response = requests.get(req).text
        data = json.loads(response)
        i = 1
        key_teatr = 0
        while i <= 100:
            post_date = data["response"][i]["date"]
            if post_date > float(week_before):
                text = data["response"][i]["text"]
                key_teatr_finder = re.findall('((Б|б)илет(а|у|ом|ами|ам|е|ы|ах|ов))', text)
                key_teatr += len(key_teatr_finder)
                i += 1
            else:
                group_data += '{"country": "' + groups_arr[group_arr.index(off)] + '","visits": ' + \
                              str(key_teatr) + ',"color": "#468ccf"},'
                break
    graph_teatr = '/**тут инфа*/' + group_data + '/**тут инфа кончилась*/'
    f = open('./static/graph_ticket.js', 'r', encoding='UTF-8')
    js_text = f.read()
    f.close()
    js_text_new_1 = re.sub('\n', '', js_text)
    js_text_new = re.sub('/\*\*тут инфа\*/(.+)/\*\*тут инфа кончилась\*/', str(graph_teatr), js_text_new_1)
    fl = open('./static/graph_ticket.js', 'w', encoding='UTF-8')
    fl.write(js_text_new)
    fl.close()
    return render_template('ticket_page.html', main_url=main_url)

@app.route('/prem')
def prem():
    main_url = url_for('main_page')
    today_date_full = time.time()
    week_before = float(today_date_full) - 604800
    group_data = ''
    groups_arr = ['ТЕАТРЫ МОСКВЫ', 'ТЕАТР КВАРТЕТ И', 'Театр НИУ ВШЭ', 'Театр балета Бориса Эйфмана',
                  'Bolshoi Theatre of Russia / Большой театр России', 'Михайловский театр',
                  'Молодежный ТЕАТР НА БУЛАКЕ Казань', 'Пермский театр У Моста',
                  'Театральная Вешалка', 'ОДИН ТЕАТР', 'ВОЛКОВСКИЙ ТЕАТР', 'Театр Красный факел',
                  'Московский театр мюзикла',
                  'Санкт-Петербургский театр Мастерская']
    group_arr = ['moscowtheatres', 'kvartet_i', 'hsetheatre',
                 'eifmanballet', 'bolshoitheatre', 'mikhailovsky_theatre', 'teatrnabulake',
                 'teatrumosta', 'teatrpeterburg', 'odin_teatr', 'volkov_teatr',
                 'krasnii_fakel', 'teamuz', 'teatrkozlova']
    for off in group_arr:
        req = 'https://api.vk.com/method/wall.get?domain=' \
              + str(off) \
              + '&count=100&access_token=13438ccb13438ccb13438ccbcd131f4d1b1134313438ccb4a0aecff06982089e052b5e6'
        response = requests.get(req).text
        data = json.loads(response)
        i = 1
        key_teatr = 0
        while i <= 100:
            post_date = data["response"][i]["date"]
            if post_date > float(week_before):
                text = data["response"][i]["text"]
                key_teatr_finder = re.findall('((П|п)ремьер(а|у|ой|ами|ам|е|ы|ах))', text)
                key_teatr += len(key_teatr_finder)
                i += 1
            else:
                group_data += '{"country": "' + groups_arr[group_arr.index(off)] + '","visits": ' + \
                              str(key_teatr) + ',"color": "#468ccf"},'
                break
    graph_teatr = '/**тут инфа*/' + group_data + '/**тут инфа кончилась*/'
    f = open('./static/graph_prem.js', 'r', encoding='UTF-8')
    js_text = f.read()
    f.close()
    js_text_new_1 = re.sub('\n', '', js_text)
    js_text_new = re.sub('/\*\*тут инфа\*/(.+)/\*\*тут инфа кончилась\*/', str(graph_teatr), js_text_new_1)
    fl = open('./static/graph_prem.js', 'w', encoding='UTF-8')
    fl.write(js_text_new)
    fl.close()
    return render_template('prem.html', main_url=main_url)

@app.route('/actor')
def actor():
    main_url = url_for('main_page')
    today_date_full = time.time()
    week_before = float(today_date_full) - 604800
    group_data = ''
    groups_arr = ['ТЕАТРЫ МОСКВЫ', 'ТЕАТР КВАРТЕТ И', 'Театр НИУ ВШЭ', 'Театр балета Бориса Эйфмана',
                  'Bolshoi Theatre of Russia / Большой театр России', 'Михайловский театр',
                  'Молодежный ТЕАТР НА БУЛАКЕ Казань', 'Пермский театр У Моста',
                  'Театральная Вешалка', 'ОДИН ТЕАТР', 'ВОЛКОВСКИЙ ТЕАТР', 'Театр Красный факел',
                  'Московский театр мюзикла',
                  'Санкт-Петербургский театр Мастерская']
    group_arr = ['moscowtheatres', 'kvartet_i', 'hsetheatre',
                 'eifmanballet', 'bolshoitheatre', 'mikhailovsky_theatre', 'teatrnabulake',
                 'teatrumosta', 'teatrpeterburg', 'odin_teatr', 'volkov_teatr',
                 'krasnii_fakel', 'teamuz', 'teatrkozlova']
    for off in group_arr:
        req = 'https://api.vk.com/method/wall.get?domain=' \
              + str(off) \
              + '&count=100&access_token=13438ccb13438ccb13438ccbcd131f4d1b1134313438ccb4a0aecff06982089e052b5e6'
        response = requests.get(req).text
        data = json.loads(response)
        i = 1
        key_teatr = 0
        while i <= 100:
            post_date = data["response"][i]["date"]
            if post_date > float(week_before):
                text = data["response"][i]["text"]
                key_teatr_finder_1 = re.findall('((А|а)ктер(а|у|ом|ами|ам|е|ы|ах|ов))', text)
                key_teatr += len(key_teatr_finder_1)
                key_teatr_finder_2 = re.findall('((А|а)ктериса(а|у|ой|ами|ам|е|ы|ах))', text)
                key_teatr += len(key_teatr_finder_2)
                i += 1
            else:
                group_data += '{"country": "' + groups_arr[group_arr.index(off)] + '","visits": ' + \
                              str(key_teatr) + ',"color": "#468ccf"},'
                break
    graph_teatr = '/**тут инфа*/' + group_data + '/**тут инфа кончилась*/'
    f = open('./static/graph_actor.js', 'r', encoding='UTF-8')
    js_text = f.read()
    f.close()
    js_text_new_1 = re.sub('\n', '', js_text)
    js_text_new = re.sub('/\*\*тут инфа\*/(.+)/\*\*тут инфа кончилась\*/', str(graph_teatr), js_text_new_1)
    fl = open('./static/graph_actor.js', 'w', encoding='UTF-8')
    fl.write(js_text_new)
    fl.close()
    return render_template('actor.html', main_url=main_url)

@app.route('/zrit')
def zrit():
    main_url = url_for('main_page')
    today_date_full = time.time()
    week_before = float(today_date_full) - 604800
    group_data = ''
    groups_arr = ['ТЕАТРЫ МОСКВЫ', 'ТЕАТР КВАРТЕТ И', 'Театр НИУ ВШЭ', 'Театр балета Бориса Эйфмана',
                  'Bolshoi Theatre of Russia / Большой театр России', 'Михайловский театр',
                  'Молодежный ТЕАТР НА БУЛАКЕ Казань', 'Пермский театр У Моста',
                  'Театральная Вешалка', 'ОДИН ТЕАТР', 'ВОЛКОВСКИЙ ТЕАТР', 'Театр Красный факел',
                  'Московский театр мюзикла',
                  'Санкт-Петербургский театр Мастерская']
    group_arr = ['moscowtheatres', 'kvartet_i', 'hsetheatre',
                 'eifmanballet', 'bolshoitheatre', 'mikhailovsky_theatre', 'teatrnabulake',
                 'teatrumosta', 'teatrpeterburg', 'odin_teatr', 'volkov_teatr',
                 'krasnii_fakel', 'teamuz', 'teatrkozlova']
    for off in group_arr:
        req = 'https://api.vk.com/method/wall.get?domain=' \
              + str(off) \
              + '&count=100&access_token=13438ccb13438ccb13438ccbcd131f4d1b1134313438ccb4a0aecff06982089e052b5e6'
        response = requests.get(req).text
        data = json.loads(response)
        i = 1
        key_teatr = 0
        while i <= 100:
            post_date = data["response"][i]["date"]
            if post_date > float(week_before):
                text = data["response"][i]["text"]
                key_teatr_finder = re.findall('((З|з)рител(ь|я|ю|ями|ем|е|и|ях|ей))', text)
                key_teatr += len(key_teatr_finder)
                i += 1
            else:
                group_data += '{"country": "' + groups_arr[group_arr.index(off)] + '","visits": ' + \
                              str(key_teatr) + ',"color": "#468ccf"},'
                break
    graph_teatr = '/**тут инфа*/' + group_data + '/**тут инфа кончилась*/'
    f = open('./static/graph_zrit.js', 'r', encoding='UTF-8')
    js_text = f.read()
    f.close()
    js_text_new_1 = re.sub('\n', '', js_text)
    js_text_new = re.sub('/\*\*тут инфа\*/(.+)/\*\*тут инфа кончилась\*/', str(graph_teatr), js_text_new_1)
    fl = open('./static/graph_zrit.js', 'w', encoding='UTF-8')
    fl.write(js_text_new)
    fl.close()
    return render_template('zrit.html', main_url=main_url)

@app.route('/play')
def play():
    main_url = url_for('main_page')
    today_date_full = time.time()
    week_before = float(today_date_full) - 604800
    group_data = ''
    groups_arr = ['ТЕАТРЫ МОСКВЫ', 'ТЕАТР КВАРТЕТ И', 'Театр НИУ ВШЭ', 'Театр балета Бориса Эйфмана',
                  'Bolshoi Theatre of Russia / Большой театр России', 'Михайловский театр',
                  'Молодежный ТЕАТР НА БУЛАКЕ Казань', 'Пермский театр У Моста',
                  'Театральная Вешалка', 'ОДИН ТЕАТР', 'ВОЛКОВСКИЙ ТЕАТР', 'Театр Красный факел',
                  'Московский театр мюзикла',
                  'Санкт-Петербургский театр Мастерская']
    group_arr = ['moscowtheatres', 'kvartet_i', 'hsetheatre',
                 'eifmanballet', 'bolshoitheatre', 'mikhailovsky_theatre', 'teatrnabulake',
                 'teatrumosta', 'teatrpeterburg', 'odin_teatr', 'volkov_teatr',
                 'krasnii_fakel', 'teamuz', 'teatrkozlova']
    for off in group_arr:
        req = 'https://api.vk.com/method/wall.get?domain=' \
              + str(off) \
              + '&count=100&access_token=13438ccb13438ccb13438ccbcd131f4d1b1134313438ccb4a0aecff06982089e052b5e6'
        response = requests.get(req).text
        data = json.loads(response)
        i = 1
        key_teatr = 0
        while i <= 100:
            post_date = data["response"][i]["date"]
            if post_date > float(week_before):
                text = data["response"][i]["text"]
                key_teatr_finder = re.findall('((С|с)пектакл(ь|я|ю|ями|ем|е|и|ях|ей))', text)
                key_teatr += len(key_teatr_finder)
                i += 1
            else:
                group_data += '{"country": "' + groups_arr[group_arr.index(off)] + '","visits": ' + \
                              str(key_teatr) + ',"color": "#468ccf"},'
                break
    graph_teatr = '/**тут инфа*/' + group_data + '/**тут инфа кончилась*/'
    f = open('./static/graph_play.js', 'r', encoding='UTF-8')
    js_text = f.read()
    f.close()
    js_text_new_1 = re.sub('\n', '', js_text)
    js_text_new = re.sub('/\*\*тут инфа\*/(.+)/\*\*тут инфа кончилась\*/', str(graph_teatr), js_text_new_1)
    fl = open('./static/graph_play.js', 'w', encoding='UTF-8')
    fl.write(js_text_new)
    fl.close()
    return render_template('paly.html', main_url=main_url)

@app.route('/teatral')
def teatral():
    main_url = url_for('main_page')
    today_date_full = time.time()
    week_before = float(today_date_full) - 604800
    group_data = ''
    groups_arr = ['ТЕАТРЫ МОСКВЫ', 'ТЕАТР КВАРТЕТ И', 'Театр НИУ ВШЭ', 'Театр балета Бориса Эйфмана',
                  'Bolshoi Theatre of Russia / Большой театр России', 'Михайловский театр',
                  'Молодежный ТЕАТР НА БУЛАКЕ Казань', 'Пермский театр У Моста',
                  'Театральная Вешалка', 'ОДИН ТЕАТР', 'ВОЛКОВСКИЙ ТЕАТР', 'Театр Красный факел',
                  'Московский театр мюзикла',
                  'Санкт-Петербургский театр Мастерская']
    group_arr = ['moscowtheatres', 'kvartet_i', 'hsetheatre',
                 'eifmanballet', 'bolshoitheatre', 'mikhailovsky_theatre', 'teatrnabulake',
                 'teatrumosta', 'teatrpeterburg', 'odin_teatr', 'volkov_teatr',
                 'krasnii_fakel', 'teamuz', 'teatrkozlova']
    for off in group_arr:
        req = 'https://api.vk.com/method/wall.get?domain=' \
              + str(off) \
              + '&count=100&access_token=13438ccb13438ccb13438ccbcd131f4d1b1134313438ccb4a0aecff06982089e052b5e6'
        response = requests.get(req).text
        data = json.loads(response)
        i = 1
        key_teatr = 0
        while i <= 100:
            post_date = data["response"][i]["date"]
            if post_date > float(week_before):
                text = data["response"][i]["text"]
                key_teatr_finder = re.findall('((Т|т)еатральн(ый|ая|ую|ое|ыми|ого|ом|ому|ым|ой))', text)
                key_teatr += len(key_teatr_finder)
                i += 1
            else:
                group_data += '{"country": "' + groups_arr[group_arr.index(off)] + '","visits": ' + \
                              str(key_teatr) + ',"color": "#468ccf"},'
                break
    graph_teatr = '/**тут инфа*/' + group_data + '/**тут инфа кончилась*/'
    f = open('./static/graph_teatral.js', 'r', encoding='UTF-8')
    js_text = f.read()
    f.close()
    js_text_new_1 = re.sub('\n', '', js_text)
    js_text_new = re.sub('/\*\*тут инфа\*/(.+)/\*\*тут инфа кончилась\*/', str(graph_teatr), js_text_new_1)
    fl = open('./static/graph_teatral.js', 'w', encoding='UTF-8')
    fl.write(js_text_new)
    fl.close()
    return render_template('teatral.html', main_url=main_url)



if __name__ == '__main__':
    app.run(debug=True)




