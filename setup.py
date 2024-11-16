from setuptools import setup, find_packages

setup(
    name='ilyaLR3',  # Название вашего проекта
    version='0.1.0',  # Версия
    packages=['prog5lr2'],  # Найдет все пакеты внутри my_project/
    install_requires=[],  # Укажите зависимости, если есть
    author='Ilya',
    author_email='ikinyaev2004@mail.ru',
    description='OpenweatherAPI fetch',
    long_description=open('README.md').read(),
    python_requires='>=3.6',  # Укажите минимальную версию Python
)