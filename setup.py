from setuptools import setup, find_packages


setup(
    name="hrdware_monitoring_syst",
    version="0.1.5",
    author="dev_ehsan96",
    author_email="eh.bahmanipor@gamil.com",
    description="""It is a simple app that can monitor the resources used by the following hardware components and report the usage as a percentage.
     And it saves the results to log files after processing.""",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/zZ72ehsan74Zz/hrdware_monitoring_syst",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
