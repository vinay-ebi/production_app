from setuptools import setup, find_packages

setup(
    name='production_app',
    version='1.0.0',
    description= 'production serverices',
    url='https://github.com/vinay-ebi/production_app.git',
    author='Vinay kaikala',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='embl production_app',

    packages=find_packages(),

    install_requires=['flask-restplus==0.12.1', 'Flask-SQLAlchemy==2.4.0', 'requests', 'click', "PyMysql==0.9.3"],

    entry_points={
        'console_scripts': [
            'production_app = production_app.app:main'
        ]
    }
)
