import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(

     name='ezblockReal',  
     version='0.1',
     scripts=['modules.py'] ,
     author="gpspelle",
     author_email="gpsunicamp016@gmail.com",
     description="Sunfounder utility block to use real components",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/gpspelle/ezblock-real-modules/blob/master/modules.py",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
