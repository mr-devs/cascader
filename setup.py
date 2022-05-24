"""
The setup script for PyPi package installation/updates.
"""

from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="cascader",
    version="0.0",
    description="Infer the diffusion of retweet cascades on Twitter.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Matthew DeVerna",
    author_email="mdeverna@iu.edu",
    url="https://github.com/mr-devs/cascader",
    project_urls={
        "Documentation": "https://github.com/mr-devs/cascader",
        "Issue Tracker": "https://github.com/mr-devs/cascader/issues",
        "Source Code": "https://github.com/mr-devs/cascader",
    },
    download_url="https://pypi.org/project/cascader/",
    packages=["cascader"],
    # package_data={
    #     'cascader': ['data/falsity_scores.csv']
    # },
    # include_package_data = True,
    install_requires=["numpy>=1.21.6", "pandas>=1.2.4"],
    python_requires=">=3.7",
)
