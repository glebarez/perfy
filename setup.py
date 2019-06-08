from distutils.core import setup
setup(
  name = 'perfy',         
  packages = ['perfy'],  
  version = '0.21',     
  license='MIT',      
  description = 'Perfy - a lightweight performance tracer for python',
  author = 'Gleb Sakhnov',                   
  author_email = 'gleb.sakhnov@gmail.com',    
  url = 'https://github.com/glebarez/perfy',   
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['profiling', 'trace', 'runtime', 'analysis'],
  install_requires=[],
  classifiers=[
    'Development Status :: 5 - Production/Stable',     
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Profiling Tools',
    'Topic :: Software Development :: Performance Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)