from setuptools import setup, find_packages
import re

with open('README.md', 'r') as f:
    long_description = f.read()

def get_version(file_name):
    """Get the package version from the specified file."""
    with open(file_name, 'r', encoding='utf-8') as f:
        version_file = f.read()
        version_match = re.search(r'__version__\s*=\s*["\']([^"\']+)["\']', version_file)
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find version string.")

setup(
    name='numo',
    version=get_version('numo/__init__.py'),
    #description=''
    long_description = long_description,
    long_description_content_type='text/markdown',
    project_urls={
        'Source': 'https://github.com/DevByEagle/numo',
        'Tracker': 'https://github.com/DevByEagle/numo/issues'
    },
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        #'Development Status :: 4 - Beta',
    ],
    python_requires='>=3.10',
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
    license='MIT',
)
