import eventlet
import requests
import config


class BBRequests:
    @staticmethod
    def __get_image(cmd_type):
        timeout = eventlet.Timeout(10)
        try:
            response = requests.get(config.generators[cmd_type])
            r = response.json().pop()['preview']
            return config.media[cmd_type] + r
        except eventlet.timeout.Timeout:
            return None
        finally:
            timeout.cancel()

    @staticmethod
    def send_image_by_cmd(cmd, bot, chat_id):
        image = BBRequests.__get_image(cmd)
        if image is None:
            pass
        else:
            bot.send_photo(chat_id, image)

    @staticmethod
    def is_photo_cmd(cmd):
        if cmd == 'boobs' or cmd == 'butts':
            return True
        else:
            return False
