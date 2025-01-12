from setuptools import setup

setup(
    author="Deepesh",
    author_email="dpssalhotra@gmail.com",
    description="""A cli tool written in python which mimic linux/unix command wc behaviour.
    more info visit: https://codingchallenges.fyi/challenges/challenge-wc
    """,
    version="0.0.1",
    name="final",
    py_modules=["main"],
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "py_wc = main:final",
        ],
    },
)