from distutils.core import setup

setup(
    name='url-shortener',
    version='0.1dev',
    packages=['shortener'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description='A command-line tool for shortening long URLs',
    author="Karan Suthar",
    author_email="karansthr97@gmail.com",
    entry_points={
        'console_scripts': ['shrt=shortener:main'],
    },
    install_requires=[
        "requests==2.18.4",
        "pyperclip"
    ],
)
