from setuptools import setup

setup(
    name='central_server',
    version='1.0.0',
    install_requires=[
        'pyramid',
        'pyramid_mako',
        'paho-mqtt',
        'waitress'
    ],
    entry_points="""\
         [paste.app_factory]
         main = central_server:main
         """,
    url='',
    license='',
    author='Stephen Goedhart',
    author_email='sdg25@hotmail.com',
    description=''
)
