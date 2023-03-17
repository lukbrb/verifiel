from setuptools import setup

setup(
    name='verifiel',
    version='0.0.1',
    packages=['verifiel'],
    install_requires=[
        'setuptools~=65.5.0',
        'tqdm~=4.64.1',
        'requests~=2.28.2'
    ],
    url='',
    license='Apache 2.0',
    author='Lucas Barbier',
    author_email='lucas.barbier@protonmail.com',
    description='Vérifiel est un logiciel de tri de courriels. Il permet en outre d\'automatiser le désabonnement des '
                'listes de distribution.'
)
