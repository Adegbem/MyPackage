from setuptools import setup, find_packages

setup(
    name='MyPackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='First would-be install package on my system',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Adegbem/MyPackage.git',
    author='<Emmanuel Adetunji>',
    author_email='<adegbem@gmail.com>'
)
