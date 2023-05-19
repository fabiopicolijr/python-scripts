import shutil


def copy_files(to_folder):
    # copy .ebextensions
    shutil.copytree(".ebextensions", f"{to_folder}/.ebextensions", dirs_exist_ok=True)
    # copy blog
    shutil.copytree("blog", f"{to_folder}/blog", dirs_exist_ok=True)
    # copy my_site
    shutil.copytree("my_site", f"{to_folder}/my_site", dirs_exist_ok=True)
    # copy templates
    shutil.copytree("templates", f"{to_folder}/templates", dirs_exist_ok=True)
    # copy manage.py
    shutil.copy("manage.py", f"{to_folder}/manage.py")
    # copy custom_storages.py
    shutil.copy("custom_storages.py", f"{to_folder}/custom_storages.py")
    # copy requirements.txt
    shutil.copy("requirements.txt", f"{to_folder}/requirements.txt")
