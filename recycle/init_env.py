# coding: utf-8

import json
import os
import sys

from recycle.lib import my_print, my_input
from recycle.config import (
    CONFIG_PATH,
    HOME,
    ENABLE_EMOJI,
    ENABLE_COLOR,
    TREE_ALL_DIRECTORY_SIZE,
    TRASH_PATH,
    FILE_SIZE_COLORS,
)

zsh_config = """# py-recycle config start
# Don't put your config inside "# py-recycle config start" and "# py-recycle config end"!
# Else it will be DELETE!
autoload -Uz compinit
compinit
compdef '_files -W {}`pwd`' undel
compdef '_files -W {}`pwd`' pdel
compdef '_files -W {}`pwd`' tt
alias tl='tl(){{ tt $1 | less -r }};tl'
# py-recycle config end
""".format(
    TRASH_PATH, TRASH_PATH, TRASH_PATH
)

bash_config = """# py-recycle config start
# Don't put your config inside "# py-recycle config start" and "# py-recycle config end"!
# Else it will be DELETE!
_undel() {{
    local trash_home="{}"
    local current_path=`pwd`
    local current_arg="${{COMP_WORDS[COMP_CWORD]}}"
    local trash_dir=$trash_home$current_path/${{COMP_LINE:6:999}}
    local IFS=$'\t\n'

    if [[ $current_arg =~ ^/ ]] ; then
      # /a/b/c
      return 0
    elif [[ $current_path =~ $trash_home ]] ; then
      # in {}
      return 0
    elif [[ ! -d $trash_dir ]] ; then
      # {}`pwd` don't exists
      return 0
    elif [[ -d $trash_dir ]] ; then
      COMPREPLY=( $(compgen -W "`ls -a $trash_dir|grep -Pv '^\.{{1,2}}$'`" -- ${{current_arg}}) )
      return 0
    fi
}}

complete -o filenames -o dirnames -o default -F _undel undel
complete -o filenames -o dirnames -o default -F _undel pdel
complete -o filenames -o dirnames -o default -F _undel tt
alias tl='tl(){{ tt $1 | less -r }};tl'
# py-recycle config end
""".format(
    TRASH_PATH, TRASH_PATH, TRASH_PATH
)

shell_config = {"zsh": zsh_config, "bash": bash_config}


def install(shell, path):
    shellrc_path = "{}/.{}rc".format(HOME, shell)

    if not os.path.exists("/bin/" + shell):
        return my_print("your don't have {}, skip it".format(shell))
    config_info = ""
    config_info_bp = ""
    if os.path.isfile(shellrc_path):
        config_info = open(shellrc_path, "r").read()
        config_info_bp = config_info
        if "# py-recycle config start" in config_info:
            config_info = config_info.split("\n")
            config_info = "\n".join(
                config_info[0 : config_info.index("# py-recycle config start")]
                + config_info[config_info.index("# py-recycle config end") + 1 :]
            )
    try:
        open(shellrc_path, "w").write(config_info + shell_config[shell])
        my_print("Installed in {}, enjoy it :)".format(shellrc_path))
    except:
        open(shellrc_path + ".old", "w").write(config_info_bp)
        my_print(
            "Install Failed in {}, old config file in {}.".format(
                shellrc_path, shellrc_path + ".old"
            )
        )

    if not path:
        return

    path = "export PATH={}\n".format(path)
    if path in open(shellrc_path).readlines():
        return
    my_print('Write "{}" in {}'.format(path.strip(), shellrc_path))
    open(shellrc_path, "a+").write(path)


def main():
    scripts_dir_path = os.path.dirname(sys.argv[0])
    if scripts_dir_path in os.getenv("PATH"):
        path = None
    elif (
        "n"
        in my_input(
            'Add "{}" to your PATH, to enable it?[Y/n]'.format(scripts_dir_path)
        ).lower()
    ):
        path = None
    else:
        path = "{}:$PATH".format(scripts_dir_path)

    install("zsh", path)
    install("bash", path)

    if not os.path.exists(TRASH_PATH):
        os.makedirs(TRASH_PATH)
    open(CONFIG_PATH, "w").write(
        json.dumps(
            dict(
                ENABLE_EMOJI=ENABLE_EMOJI,
                ENABLE_COLOR=ENABLE_COLOR,
                TREE_ALL_DIRECTORY_SIZE=TREE_ALL_DIRECTORY_SIZE,
                TRASH_PATH=TRASH_PATH,
                FILE_SIZE_COLORS=FILE_SIZE_COLORS,
            ),
            indent=4,
        )
    )
    current_shell = os.getenv("SHELL").split("/")[-1]
    my_print("\n")
    if current_shell in ["bash", "zsh"]:
        command = "source ~/.{}rc".format(current_shell)
        my_print('\tPlease Execute "{}"'.format(command))
    else:
        my_print(
            '\tSorry, detect current shell is "{}", recycle onle support "zsh" and  "bash"'.format(
                current_shell
            )
        )
        my_print(
            '\tYou can manually execute "source ~/.zshrc" or "source ~/.bashrc" to config zsh or bash'
        )
    my_print("\n")
