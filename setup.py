from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='verb-inspector',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Verb Inspector",
    license="MIT",
    author="Mijael Bueno",
    author_email='mijaelbueno@gmail.com',
    url='https://github.com/mijaelb/verb-inspector',
    packages=['verb-inspector'],
    entry_points={
        'console_scripts': [
            'verb-inspector=verb-inspector.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='verb-inspector',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
