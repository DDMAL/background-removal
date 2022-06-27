from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='background_removal',
    version='1.0.0',
    description='Background removal supporting threshold_sauvola and sae binarizing.',
    url='https://github.com/DDMAL/Paco_classifier',
    author='Khoi Nguyen, Wanyi Lin',
    license='MIT License',
    packages=['background_removal'],
    install_requires=requirements,
    python_requires=">=3.7.5"
)
