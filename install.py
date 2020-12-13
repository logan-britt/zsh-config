import os
import shutil
import platform

# get the home folder of the user in question
home_path = str(os.path.expanduser())

# deleate config files not in current use
path_list = os.listdir(home_path)
for thing in path_list:
  if os.path.isfile(thing):
    file_name = thing

    if file_name == '.bashrc':
      rc_path = str(os.path.join(home_path, '.bashrc'))
      os.remove(rc_path)

    elif file_name == '.bash_profile':
      profile_path = str(os.path.join(home_path, '.bash_profile'))
      os.remove(profile_path)

    elif file_name == '.zshrc':
      rc_path = str(os.path.join(home_path, '.zshrc'))
      os.remove(rc_path)

    elif file_name == '.zprofile':
      profile_path = str(os.path.join(home_path, '.zprofile'))
      os.remove(profile_path)

    elif file_name == '':
      pass

# here we build the "new" zsh config scrips and move them into there locations
