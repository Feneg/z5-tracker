import setuptools

setuptools.setup(
    name='z5-tracker',
    version='1.2.1',
    author='Feneg',
    description='Helper program for Ocarina of Time randomiser',
    url='https://www.github.com/feneg/z5-tracker',
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Games/Entertainment',
        'Topic :: Utilities'],
    entry_points={
        'gui_scripts': (
            'z5-tracker = z5tracker.main:main',
            'z5tracker = z5tracker.main:main')}
    )
