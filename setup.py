from setuptools import setup

setup(
    name='xgboost_tuner',
    version='0.1.1',
    description='XGBoost Automatic Parameter Tuning Library',
    author='cwerner87',
    author_email='cwerner87@users.noreply.github.com',
    url='https://github.com/cwerner87/xgboost_tuner',
    license='GPL v3',
    packages=['xgboost_tuner'],
    install_requires=[
        'numpy>=1.12',
        'scikit-learn>=0.18',
        'scipy>=0.19',
        'xgboost>=0.6'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis'
    ]
)
