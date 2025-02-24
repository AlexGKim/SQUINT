from setuptools import setup

setup(name='squint',
      version='0.1',
      description='SQUINT',
      url='https://github.com/AlexGKim/SQUINT',
      author='Alex Kim',
      author_email='agkim@lbl.gov',
      license='MIT',
      packages=['squint'],
      install_requires=[
           'numpy', 'astropy',
      ],
      entry_points = {
           'console_scripts': [
               'squint-noise=squint.command_line:noise_flam',
               'squint-diffraction-limit=squint.command_line:diffraction_limit',
               ],
      },
      zip_safe=False)
