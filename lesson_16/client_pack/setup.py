from setuptools import setup, find_packages

setup(name='client_chat_2023',
      version='0.2',
      description='Client packet',
      packages=find_packages(),  # ,Будем искать пакеты тут(включаем авто поиск пакетов)
      author_email='test@mail.ru',
      author='Paul_Kozic',
      install_requeres=['PyQt5', 'sqlalchemy', 'pycruptodome', 'pycryptodomex']
      ##зависимости которые нужно до установить
      )
