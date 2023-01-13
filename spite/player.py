import bs4
import json
import os


def convertTable(tag: bs4.element.Tag, isAllPlayer):
    return convertHtmlToJson(tag, isAllPlayer)


def convertHtmlToJson(data: bs4.element.Tag, isAllPlayer):
    keys = findKeys(data)
    values = findValues(data,isAllPlayer)

    keysStr = json.loads(keys)
    valuesStr = json.loads(values)

    jsonStr = [keysStr['key'], valuesStr['values']]
    return jsonStr


def findKeys(data: bs4.element.Tag):
    key = []
    allTh = data.find('tr')
    for i in allTh:
        if i != '\n' and i != ' ':
            key.append(i.string)

    # 转换为json
    keyJson = {'key': key}
    return json.dumps(keyJson)


def findValues(data: bs4.element.Tag,isAllPlayer):
    players = []

    tbody = data.find('tbody')
    line = tbody.find_all('tr')
    for tr in line:
        player = []
        th = tr.find('th')
        if th is None:
            continue
        if th.string != 'Rk':
            print(th.string)
            if isAllPlayer is True:
                player.append(str(th['data-stat'] + ":" + str(th.string)))
            else:
                player.append(str(th['data-stat'] + ":" + str(th.a.string)))
            tds = tr.find_all('td')
            for td in tds:
                if str(td['data-stat']) == 'player':
                    link = td.a['href']
                    player.append(str(td['data-stat'] + ":" + str(td.string+'*'+link)))
                elif str(td['data-stat']) == 'pos':
                    if td.string is None:
                        g = ''
                    elif ',' in td.string:
                        gs = td.string.split(',')
                        g = gs[0] + '/' + gs[1]
                    else:
                        g = td.string
                    player.append(str(td['data-stat'] + ":" + str(g)))
                else:
                    player.append(str(td['data-stat'] + ":" + str(td.string)))
            if isAllPlayer is True:
                players.append({th.string: player})
            else:
                players.append({th.a.string: player})


    values = {'values': players}
    return json.dumps(values)


def jsonToCsv(tableStr):
    keyStr = ""
    for key in tableStr[0]:
        keyStr = keyStr + key + ","
    keyStr = keyStr[0:len(keyStr) - 1]

    rank = 1
    listPlayer = []
    for player in tableStr[1]:
        player = player[str(rank)]

        dataStr = ""
        for data in player:
            dataStr = dataStr + data.split(':')[1] + ","

        rank = rank + 1
        dataStr = dataStr[0:len(dataStr) - 1]
        listPlayer.append(dataStr)

    with open('player.csv', 'w+', encoding='utf-8') as playerFile:
        result = keyStr
        for player in listPlayer:
            result = result + "\n" + player
        playerFile.write(result)


def playerJsonToCsv(tableStr, playerName, teamName):
    keyStr = ""
    for key in tableStr[0]:
        keyStr = keyStr + key + ","
    keyStr = keyStr[0:len(keyStr) - 1]

    listPlayer = []
    for player in tableStr[1]:
        key = list(player.keys())[0]
        player = player[key]
        # print(player)

        dataStr = ""
        for data in player:
            dataStr = dataStr + data.split(':')[1] + ","

        dataStr = dataStr[0:len(dataStr) - 1]
        listPlayer.append(dataStr)

    if not os.path.exists(teamName + '/csv'):
        os.makedirs(teamName + '/csv')
    with open('players/'+teamName + '/csv/' + playerName + '.csv', 'w+', encoding='utf-8') as playerFile:
        result = keyStr
        for player in listPlayer:
            result = result + "\n" + player
        playerFile.write(result)
