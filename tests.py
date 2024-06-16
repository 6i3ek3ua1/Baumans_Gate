from unittest.mock import patch
from menu import GameMenu
import logging

# получим логгер для нашего приложения либо создадим новый, если он еще не создан (паттерн Синглтон)
logger = logging.getLogger("tests")
logger.setLevel(logging.DEBUG)
# опишем, куда и как будем сохранять логи: зададим файл и формат
handler = logging.FileHandler('test_log.txt', 'a', 'utf-8')
formatter = logging.Formatter("%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s")

# установим файлу нужный формат, а нужный файл - логгеру
handler.setFormatter(formatter)
logger.addHandler(handler)


# тест 1
def test_player():
    fake_inputs = [
        '0',
        'semen',
        'semen',
        '3',
        '2',
        'map',
        'Test',
        'test',
        '3',
        '0',
        'да',
    ]
    with patch('builtins.input', side_effect=fake_inputs):
        game = GameMenu()
        game.game_process()
        logger.info("Тест победы игрока успешно выполнен")
    assert game.result == "---------------Вы победили------------------\nвеликолепная доблесть"


# тест 2
def test_bot():
    fake_inputs = [
        '0',
        'semen',
        'semen',
        '3',
        '2',
        'map',
        'test',
        'Test',
        '3',
        '0',
        '0',
        '0'
    ]
    with patch('builtins.input', side_effect=fake_inputs):
        game = GameMenu()
        game.game_process()
        logger.info("Тест победы бота успешно выполнен")
    assert game.result == "---------------Вы проиграли------------------\nбессмысленная жертва"


# тест 3
def test_cost():
    fake_inputs = [
        '0',
        'semen',
        'semen',
        '3',
        '2',
        'map',
        'test',
        'Test',
        '3',
        '0',
        '0',
        '2'
    ]
    with patch('builtins.input', side_effect=fake_inputs):
        game = GameMenu()
        game.test_cost()
        logger.info("Тест прочсёта штрафа успешно выполнен")
    assert game.costing == "Недостаточно очков для перемещения"


# тест 4, 5
def test_attack():
    fake_inputs = [
        '0',
        'semen',
        'semen',
        '3',
        '2',
        'map',
        '0',
        'test',
        '3',
        '0',
        'да'
    ]
    with patch('builtins.input', side_effect=fake_inputs):
        game = GameMenu()
        game.test_attack()
        logger.info("Тест проведения атаки успешно выполнен")
    assert game.costing == "Вражеский боец был атакован"


# тест 6
def test_walk():
    fake_inputs = [
        '0',
        'semen',
        'semen',
        '3',
        '2',
        'map',
        'test',
        'Test',
        '0',
        '0',
        'X',
        '-1'
    ]
    with patch('builtins.input', side_effect=fake_inputs):
        game = GameMenu()
        game.test_cost()
        logger.info("Тест проведения ходьбы успешно выполнен")
    assert game.costing == 'Не выходите за карту'


# тест 7
def test_death():
    fake_inputs = [
        '0',
        'semen',
        'semen',
        '3',
        '2',
        'map',
        '1',
        'test',
        '3',
        '0',
        'да',
        '0',
        'да'
    ]
    with patch('builtins.input', side_effect=fake_inputs):
        game = GameMenu()
        death = game.test_death()
        logger.info("Тест смерти успешно выполнен")
    assert death == 0


# тест 9
def test_buy():
    fake_inputs = [
        '0',
        'semen',
        'semen',
        '3',
        '2',
        'map',
        '1',
        '20',
        'Маг-воин',
        'Маг-воин',
        '3'
    ]
    with patch('builtins.input', side_effect=fake_inputs):
        game = GameMenu()
        logger.info("Тест покупки юнитов успешно выполнен")
    assert game.units != 0


# тест 11
def test_field():
    fake_inputs = [
        '0',
        'semen',
        'semen',
        '3',
        '2',
        'map',
        'test',
        'Test',
        '3'
    ]
    with patch('builtins.input', side_effect=fake_inputs):
        game = GameMenu()
        logger.info("Тест отображения поля успешно выполнен")
    assert game.field.field == [["*", "*", "*", "U", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                                ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "!"],
                                ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                                ["*", "*", "*", "*", "*", "@", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                                ["*", "*", "*", "*", "*", "*", "*", "*", "*", "#", "*", "*", "*", "#", "*"],
                                ["*", "*", "*", "*", "*", "^", "*", "*", "*", "*", "@", "*", "*", "*", "*"],
                                ["@", "*", "*", "*", "*", "*", "^", "!", "#", "*", "*", "*", "*", "*", "*"],
                                ["*", "*", "*", "#", "*", "*", "*", "@", "*", "*", "*", "*", "*", "*", "*"],
                                ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                                ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "!", "*", "*", "*"],
                                ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                                ["!", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "!", "*", "#"],
                                ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                                ["*", "@", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                                ["*", "*", "*", "U", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]


# тест 12
def test_wizard():
    fake_inputs = [
        '0',
        'semen',
        'semen',
        '3',
        '2',
        'map',
        '1',
        '20',
        'Маг-воин',
        'Маг-воин',
        '3'
    ]
    with patch('builtins.input', side_effect=fake_inputs):
        game = GameMenu()
        logger.info("Тест покупки мага-воина успешно выполнен")
    assert game.units[0].spell1 == {'attack_range_min': 5, 'attack_range_max': 7, 'damage': 50,
                                    'name': 'земляной прорыв'}
