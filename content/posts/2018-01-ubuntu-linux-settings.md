---
Title: Ubuntu/linux settings
Author: SergeM
Date: 2018-01-11 08:00:00
Slug: ubuntu-linux-settings
aliases: [/ubuntu-linux-settings.html]
Tags: [ linux,useful,settings,ubuntu,shell, ubuntu 18, extensions, gui]
---




Some settings I find useful for a workstation

## CPU monitoring on the main panel
Default Ubuntu desktop seems to become finally convenient enough for me starting from Ubuntu 18.04. 
Only several tweaks are missing.
Constantly available CPU/Mem/HDD/Network monitor is one of them.
Here is how to install a small widget for a top panel in the default GNOME desktop environment.

1. ```sudo apt-get install gir1.2-gtop-2.0 gir1.2-networkmanager-1.0  gir1.2-clutter-1.0```

2. Go to **Ubuntu Software** and then search for `system monitor extension`. Install one named `system-monitor`: 

    >  Display system information in GNOME Shell status bar

3. After the installation you should see a new applet in the main pannel. One can find settings in the context menu.


## Desktop, workspaces and gnome extensions settings in Ubuntu 18.04
### only show applications of current workspace in launcher:

```
sudo apt install dconf-editor
```

Navigate to org > gnome > shell > extensions > dash-to-dock and check isolate-workspaces

### Show workspace indicator in the main pannel

Enable "Workspace Indicator" extension.

<img src="/media/2018-01-ubuntu-linux-settings/extensions_settings.png" alt="extensions settings in ubuntu 18"/>

### Static number of workspaces

<img src="/media/2018-01-ubuntu-linux-settings/workspaces_settings.png" alt="workspaces settings in ubuntu 18"/>

### Showing windows instead of notification "window is ready"

Install extension [noannoyance](https://extensions.gnome.org/extension/1236/noannoyance/)

or use dconf:

![show window insread of notification window is ready](/media/2018-01-ubuntu-linux-settings/dconf-auto-raise.png)

### Align windows to the corners or sides of the screen

Default settings allow only alignment to the sides and full screen.
To align windows to the corners I use [Put windows](https://extensions.gnome.org/extension/39/put-windows/) gnome  extension.

## Autocomplete in shell
See [autocomplete from history in terminal](/autocomplete-from-history-in-terminal.html)



## Set `nemo` as default file manager 
```
xdg-mime default nemo.desktop inode/directory application/x-gnome-saved-search
```

now if you run `xdg-open ./` or press `Super+E` nemo starts.

[source](http://www.fandigital.com/2013/01/set-nemo-default-file-manager-ubuntu.html)


## Auto completion for fabric
Add 
```
have fab && {
_fab_completion()
{
    COMPREPLY=() 
    local cur tasks
    tasks=$(fab --shortlist 2>/dev/null)
    _get_comp_words_by_ref cur
    COMPREPLY=( $(compgen -W "${tasks}" -- ${cur}) )
}
complete -F _fab_completion fab
}
```

to `~/.bash_completion`.

[Source](http://evans.io/legacy/posts/bash-tab-completion-fabric-ubuntu/)


## Default permissions for directories
By default when you call `mkdir abc` the following permissions are created 
```
u=rwx,g=rx,o=rx
```

That means that other users, also other groups, will be able to read and execute your files. That is a legacy setting. you can change it by replacing
```
UMASK       002 
```
with 
```
UMASK       077
```
in file `/etc/login.defs`. Here is the quote from this file:
```
# UMASK is the default umask value for pam_umask and is used by
# useradd and newusers to set the mode of the new home directories.
# 022 is the "historical" value in Debian for UMASK
# 027, or even 077, could be considered better for privacy
# There is no One True Answer here : each sysadmin must make up his/her
# mind.
#
# If USERGROUPS_ENAB is set to "yes", that will modify this UMASK default value
# for private user groups, i. e. the uid is the same as gid, and username is
# the same as the primary group name: for these, the user permissions will be
# used as group permissions, e. g. 022 will become 002.

```


# Useful for server setup
* [Default permissions for directories](#default-permissions-for-directories)
* [Add service in linux](add-service-in-linux.html)
* [configuring ssh](/ssh-cheatsheet.html)


# Appearance customization
* [Change background of the lock screen in Ubuntu 18](https://askubuntu.com/questions/1042942/how-to-change-ubuntu-budgie-login-screen-background) (stackoverflow)


# Ubuntu freezes when RAM is full

(DRAFT, from https://habr.com/en/company/selectel/blog/498526/ )

Кстати, никто не подскажет как вылечить зависание ubuntu при заполнении RAM?

    SergeyD
    today at 07:27 PM

+1

    Включить и настроить swap
    Включить использование zswap: https://wiki.archlinux.org/index.php/Zswap
    Установить и настроить earlyoom — осторожно, может прибить все процессы

ValdikSS
today at 08:16 PM

+2 1. Установить и настроить zram, проще всего через zram-tools.
2. Создать /etc/sysctl.d/60-dirty.conf со следующим содержимым:

vm.dirty_bytes = 67108864
vm.dirty_background_bytes = 16777216

vm.swappiness=100
vm.watermark_scale_factor=200


3. Убедиться, что используется достаточно свежее ядро (5.3+).

Эти три пункта заметно улучшают ситуацию. Если еще полтора года назад, во времена 4.19, я бы однозначно советовал Windows 10 для маломощных компьютеров с малым количеством RAM, то с параметрами, описанными выше, я ошибся с копированием файла, скопировав многогигабайтный файл в RAM целиком, и система только немного замедлилась. Также могу запускать несколько виртуалок одновременно, RAM в настройках которых превышает количество физически установленной памяти, и все также, не побоюсь этого слова, быстро работает, при 5+ ГБ в swap (и zram, и zswap).
