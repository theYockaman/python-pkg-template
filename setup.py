from setuptools import setup, find_packages


with open("requirements.txt", "r") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name = "package_name"
    , version = "0.1.0"
    , author = "Nathan Yockey"
    , author_email = 'n8teyock@gmail'
    , url = ''
    , description = "Package Description"
    , packages = find_packages()
    , include_package_data=True
    , install_requires=requirements
    , python_requires='>=3.9'
    , test_suite='tests'
    # , package_data = {
    #     'utils': ['templates/HTML/*'
    #               ,'templates/CSS/*'
    #               ,'templates/CSS/Basics/*'
    #               ,'templates/JS/*'
    #               ,'templates/PHP/*'
    #               ,'templates/MD/*'
    #               ,'templates/Templates/*'
    #     ]
    # }
    , long_description = open("README.md").read()
    , long_description_content_type = 'text/markdown'
    
)