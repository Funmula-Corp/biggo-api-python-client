from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="biggo-api",
    version="0.1.0",
    author="FUNMULA CO., LIMITED",
    author_email="info@funmula.com",
    description="client for accessing biggo api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=[
        'oauthlib',
        'requests_oauthlib',
    ],
    keywords=['BigGo', 'Funmula', 'API', 'Open-Authentication', 'Social-Media', 'Social-Networking'],
    platforms=['Linux', 'Windows', 'Mac'],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Environment :: Desktop Environment',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Communications :: API',
        'Topic :: Software Development :: API-Client',
    ],
)
