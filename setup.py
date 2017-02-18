try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project of yourFinance program.',
    'author': '_Sikorsky',
    'url': 'None',
    'download_url': 'None',
    'author_email': 'inpursuitpl@gmail.com',
    'version': '1.3',
    'install_requires': ['nose'],
    'packages': ['yourFinance'],
    'scripts': [],
    'name': 'yourFinance'
}

setup(**config)
