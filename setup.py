from setuptools import setup, find_packages

# Define your project metadata and dependencies
setup(
    name="aitools",                             # Name of your package
    version="0.1.0",                            # Package version
    author="Hongbing Li",                       # Package author
    author_email="cshbli@hotmail.com",          # Author's email
    description="Python AI tools and utilities",  # Short description
    long_description=open("README.md").read(),  # Long description (from README.md)
    long_description_content_type="text/markdown",  # Format of README (e.g., markdown)
    url="https://github.com/yourusername/your_project",  # Project's home page (e.g., GitHub)
    packages=find_packages(),                   # Automatically find all packages in the project
    install_requires=[                          # List your project's dependencies here
        "numpy>=1.19.0",
        "pandas>=1.1.0",
        # Add more dependencies as needed
    ],
    classifiers=[                               # Optional metadata for the project
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',                    # Specify compatible Python versions
    include_package_data=True,                  # Include other files (e.g., data, config) specified in MANIFEST.in
)
