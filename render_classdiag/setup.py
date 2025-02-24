from setuptools import setup, find_packages

setup(
    name="render_classdiag",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['core.services'],
    # requiring Django later than 2.1
    install_requires=['Django>=2.1'],
    # Installing package data related to packge
    # https://docs.python.org/3/distutils/setupscript.html#installing-package-data
    # data_files specify additional files that are not closely related to the
    # source code of the package.
    # https://docs.python.org/3/distutils/setupscript.html#installing-additional-files
    entry_points={
        'kenigsberg.render': ['ep_render_classdiag=core.services.render_classdiag:RendererClassDiagram'],
    },  
    package_data={'core': ['templates/*.html']},
    zip_safe=False
)
