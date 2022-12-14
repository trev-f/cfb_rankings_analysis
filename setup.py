from setuptools import find_packages, setup

setup(
    name='cfb_rankings_analysis',
    packages=find_packages(),
    version='0.1.0',
    description='Analyze historical rankings and ratings for college football teams.',
    author='Trevor F. Freeman',
    license='MIT',
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'cfb-rankings-analysis = cfb_rankings_analysis.cli:cli',
        ],
    },
)
