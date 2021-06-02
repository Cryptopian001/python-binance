from setuptools import setup

setup(
    name='cp-binance',
    version='1.0.2',
    packages=['binance'],
    description='Binance REST API python implementation',
    url='https://github.com/sammchardy/python-binance',
    author='Sam McHardy',
    license='MIT',
    author_email='',
    install_requires=['requests', 'six', 'Twisted', 'pyOpenSSL', 'autobahn', 'service-identity', 'dateparser',
                      'urllib3', 'certifi', 'cryptography', 'ujson'],
    keywords='binance exchange rest api bitcoin ethereum btc eth neo',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
