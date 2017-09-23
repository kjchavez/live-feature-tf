from setuptools import setup

setup(name='livefeature_tf',
      version='0.1',
      description='Live features for TensorFlow models',
      url='http://github.com/kjchavez/live-feature-tf',
      author='Kevin Chavez',
      author_email='kevin.j.chavez@gmail.com',
      license='MIT',
      packages=['livefeature_tf'],
      install_requirements=["livefeature>=0.1"],
      zip_safe=False)
