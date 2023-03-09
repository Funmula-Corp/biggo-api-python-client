from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="biggo-api",
    version="0.2.0",
    author="FUNMULA CO., LIMITED",
    author_email="info@funmula.com",
    description="client for accessing biggo api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Funmula-Corp/biggo-api-python-client",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=[
        'async_oauthlib',
        'oauthlib',
        'pydantic',
        'requests_oauthlib',
    ],
    keywords=['BigGo', 'Funmula', 'API', 'Open-Authentication', 'Social-Media', 'Social-Networking'],
    platforms=['Linux', 'Windows', 'Mac'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Communications',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
