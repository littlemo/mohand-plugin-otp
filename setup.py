from setuptools import setup, find_packages
from source.mohand_plugin_otp.version import get_setup_version


setup(
    name='mohand-plugin-otp',
    url='https://github.com/littlemo/mohand-plugin-otp',
    author='moear developers',
    author_email='moore@moorehy.com',
    maintainer='littlemo',
    maintainer_email='moore@moorehy.com',
    version=get_setup_version(),
    description='MoHand插件，用以提供定制化的一次性密码生成服务',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='mohand plugin otp',
    packages=find_packages('source'),
    package_dir={'': 'source'},
    include_package_data=True,
    zip_safe=False,
    license='GPLv3',
    python_requires='>=2.7',
    project_urls={
        'Documentation': 'http://mohand-plugin-otp.rtfd.io/',
        'Source': 'https://github.com/littlemo/mohand-plugin-otp',
        'Tracker': 'https://github.com/littlemo/mohand-plugin-otp/issues',
    },
    install_requires=open('requirements/pip.txt').read().splitlines(),
    entry_points={
        'mohand.plugin.hand': [
            'otp = mohand_plugin_otp.main:OtpHand',
        ],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: Chinese (Simplified)',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Communications :: Email',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Testing :: Unit',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Version Control :: Git',
        'Topic :: Terminals',
        'Topic :: Text Editors :: Emacs',
        'Topic :: Utilities',
    ],
)
