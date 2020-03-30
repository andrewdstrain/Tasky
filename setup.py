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
        "ibm-db-sa",
        "ibmcloudenv",
        "pipenv",
        "prometheus-client",
        "python-dotenv"
    ]
)
