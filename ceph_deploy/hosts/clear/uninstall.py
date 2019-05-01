def uninstall(distro, purge=False):
    packages = [
            'storage-cluster'
            ]

    distro.packager.remove(packages)
