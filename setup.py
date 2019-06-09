from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='perfy',
    packages=['perfy'],
    version='0.26',
    license='MIT',
    description='Perfy - a lightweight performance tracer for python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Gleb Sakhnov',
    author_email='gleb.sakhnov@gmail.com',
    url='https://github.com/glebarez/perfy',
    keywords=['profiling', 'trace', 'runtime', 'analysis'],
    install_requires=[],
    python_requires='>=3.2',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
