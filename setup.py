from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='background_removal',
    version='1.0.0',
    description='Background removal supporting threshold_sauvola and sae binarizing.',
    url='https://github.com/DDMAL/Paco_classifier',
    author='Khoi Nguyen, Wanyi Lin',
    license='MIT License',
    packages=find_packages(include=['background_removal', 'background_removal.*']),
    install_requires=requirements,
    package_data={"":["MODELS/*.h5"]},
    python_requires=">=3.7.3"
)
