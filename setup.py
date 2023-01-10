from setuptools import find_packages, setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='baiis_utils',
    version='0.0.1',
    author='danielx',
    # author_email='',
    description='utlity package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/codebaiis/baiis-utils',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'psycopg2-binary',
    ],
)