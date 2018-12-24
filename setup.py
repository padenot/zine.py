from setuptools import setup, find_packages

setup(
    name="zine",
    version="0.1.0",
    url='http://github.com/padenot/zine.py',
    author='Paul Adenot',
    author_email='paul@paul.cx',
    description="Generate a simple photobook pdf",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'weasyprint',
        'jinja2'
    ],
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'zine=zine.zine:main',
        ]
    },
    package_data={
        # Install the css and jinja files in the same directory than
        # the python module
        'zine': [
            'style.css',
            'template.html.jinja2'
        ],
    },
    classifiers=(
        'Environment :: Console',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
        'Programming Language :: Python :: 3.5'
        'Programming Language :: Python :: 3.6'
        'Programming Language :: Python :: 3.7'
    ),
)
