from setuptools import setup

setup(
    name='server',
    packages=['server'],
    include_package_data=True,
    install_requires=[
        "Flask",
        "Flask-Login",
        "Flask-SQLAlchemy",
        "Flask-WTF",
        "gunicorn",
        "ibmcloudenv",
        "pipenv",
        "prometheus-client"
    ]
)