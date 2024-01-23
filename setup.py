import setuptools

with open("README.md","r",encoding="utf-8") as f:
    desc=f.read()


__version__= "0.0.0"

REPO_NAME="Product-Complaint-Bucketization-using-NLP"
AUTHOR_USER_NAME="sujith-kamme"
SRC_REPO="code"
AUTHOR_EMAIL="kammesujith27@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for NLP application",
    long_description=desc,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)