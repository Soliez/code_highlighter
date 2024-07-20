import os
import sys
import subprocess



def get_default_shell() -> str:
    shell = os.getenv('SHELL')
    if not shell:
        shell = subprocess.check_output('echo $SHELL', shell=True).decode().strip()
    return shell


def get_shell_profile(shell: str) -> str:
    home = os.getenv('HOME')
    shell_name = os.path.basename(shell)
    
    profile_files = {
        'bash': ['.profile'],
        'zsh': ['.zshrc', '.zprofile'],
        'fish': ['.config/fish/config.fish'],
        'csh': ['.cshrc'],
        'tcsh': ['.tcshrc'],
        'ksh': ['.kshrc'],
        'dash': ['.profile'],
        'sh': ['.profile'],
    }
    
    for profile in profile_files.get(shell_name, []):
        profile_path = os.path.join(home, profile)
        if os.path.exists(profile_path):
            return profile_path
    
    return os.path.join(home, '.profile')


def append_alias_to_profile(profile_path: str, script_path: str) -> None:
    alias = f'alias pylight="{script_path}"\n'
    lines = ["", "# Set alias for pylight", alias, ""]
    blurb = "\n".join(lines)
    with open(profile_path, 'a') as profile:
        profile.write(blurb)
    print(f"Alias 'pylight' added to {profile_path}")
    

def install_dependencies() -> None:
    if not os.path.exists("requirements.txt"):
        lines = [
            f"Error: requirements.txt seems to be missing",
            "Please re-download it from the pylight Github repo: https://github.com/Soliez/pylight/blob/main/requirements.txt"            
        ]
        error_message = "\n".join(lines)
        print(error_message)
        sys.exit(1)
    else:
        subprocess.run('pip3 install -r requirements.txt', shell=True)


def main():
    script_path = os.path.abspath("pylight.py")
    if not os.path.exists(script_path):
        lines = [
            f"Error: {os.path.basename(script_path)} seems to be missing",
            "Please re-download it from the pylight Github repo: https://github.com/Soliez/pylight/blob/main/pylight.py"            
        ]
        error_message = "\n".join(lines)
        print(error_message)
        sys.exit(1)
    
    shell = get_default_shell()
    profile_path = get_shell_profile(shell)
    
    append_alias_to_profile(profile_path, script_path)
    subprocess.run(f'source {profile_path}', shell=True)
    


if __name__ == "__main__":
    main()