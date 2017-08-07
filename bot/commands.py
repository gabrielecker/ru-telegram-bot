"""
This module holds the command class
"""


class Command():
    """
    This class has static methods to handle the minimum commands
    recommended by Telegram
    """
    @staticmethod
    def help():
        """
        This static method returns the message for users '/help' call in chats
        """
        return 'Para usar o bot é preciso apenas chama-lo em qualquer chat ut\
ilizando @RUfsc_bot e aguardar aparecer o menu de opções.'

    @staticmethod
    def start():
        """
        This static method returns the message for users '/start' call in chats
        """
        return 'Bot para remover a necessidade de acessar o site do RU para v\
er o cardápio todos os dias, coleta informações diretamente do site.'

    @staticmethod
    def settings():
        """
        This static method returns the message for users
        '/settings' call in chats
        """
        pass
