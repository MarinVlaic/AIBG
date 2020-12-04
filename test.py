import requests
_gameId = 1
_playerIndex = 1
_playerId = 2
train = True
url = 'http://localhost:9080' if train else 'http://localhost:9080/train'


def get(url):
    r = requests.get(url)
    res = r.json()
    print(res)
    return res


def join(playerId, gameId):
    global _gameId, _playerIndex
    res = get(url + '/train/play?playerID=' + str(playerId) + '&gameID=' + str(gameId))
    return res


def run():
    counter = 0
    global _playerIndex, _playerId, _gameId
    actions = ["initial 0 10", "initial 95 85", "move 10",]
    while True:
        move = None        # After we send an action - we wait for response
        get(url + '/train/canAction?playerID=' + str(_playerId) + '&gameID=' + str(_gameId) + '&action=' + actions[counter])
        res = do_action(_playerId, _gameId, actions[counter])
        print(actions[counter] + '\n')
        # Other player made their move - we send our move again
        counter = counter + 1
        if counter >= 3:
            break


def do_action(playerId, gameId, action):
    return get(url + '/train/doAction?playerID=' + str(playerId) + '&gameID=' + str(gameId) + '&action=' + action)


def main():
    global _playerId, _gameId
    _gameId = 1
    _playerId = "1"
    print(join(_playerId, _gameId))
    run()

main()
