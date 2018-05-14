from setuptools import setup, find_packages


VERSION = '0.0.0'


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='resolver',
    version=VERSION,
    description="Resolve missing arguments at runtime",
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/HazardDede/resolver',
    author='d.muth',
    author_email='nicetry@bitch.com',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Data Engineering :: Data Pipeline',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='push pull data pipeline',
    project_urls={
        'Documentation': 'https://github.com/HazardDede/pnp/blob/master/README.md',
        'Source': 'https://github.com/HazardDede/pnp/',
        'Tracker': 'https://github.com/HazardDede/pnp/issues',
    },
    packages=find_packages(exclude=[]),
    install_requires=[
    ],
    python_requires='>=3.4',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pnp=pnp.runner:main',
        ],
    },
)