import pkg_resources

# Get a list of all installed modules and their versions
installed_packages = pkg_resources.working_set

# Print the name and version of each installed module
for package in installed_packages:
    print(package)
