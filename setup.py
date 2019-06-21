from setuptools import setup

setup(name='db_access',
      version='0.1',
      description='easy db access through sqlalchemy',
      author='Weiyi Yin',
      url='https://github.com/weiyiyin0321/easy_db_access.git',
      packages=['db_access'],
      install_requires=[
          'cx_Oracle',
          'pyodbc',
          'sqlalchemy',
          'impyla',
          'pymysql'
      ],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
      zip_safe=False)
