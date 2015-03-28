from setuptools import setup

setup(name='reproducible',
      version='0.0.1',
      description='A collection of tools to faciliate reproducible computer experiments',
      author='Yanshuai Cao',
      author_email='yanshuaicao@gmail.com',
      license='MIT',
      packages=['reproducible'],
      install_requires=[
          'hglib',
      ],
      # test_suite='nose.collector',
      # tests_require=['nose'],
      zip_safe=False)



