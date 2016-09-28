Title: Dropbox in linux mint
Author: SergeM
Date: 2016-04-10 20:50:00
Slug: dropbox-in-linux-mint
Tags: useful,linux


Hmm. It doesn't work.
I see the icon when i do
```
dropbox stop
dropbox start
```
but I cannot click on it.

Installed [nemo-dropbox](https://github.com/linuxmint/nemo-extensions/tree/master/nemo-dropbox). At least now I have "Copy dropbox link" command in menu.
Don't forget to do

```
$ killall nemo
```

after installation to make it work.
# Final Solution
[source](https://forums.linuxmint.com/viewtopic.php?f=47&t=184839&sid=1d53fe0089b25098495531994c543ee4&start=80)&nbsp;

Use
```
dropbox stop && dbus-launch dropbox start
```

Or

Do: opening 'Preferences' -> 'Startup Applications' and editing the dropbox entry so the command now reads:

CODE: [SELECT ALL](https://forums.linuxmint.com/viewtopic.php?f=47&t=184839&sid=1d53fe0089b25098495531994c543ee4&start=80)

```
dbus-launch dropbox start
```

update might overwrite the change. I think it's better to leave the existing entry alone (only disabled) and create a new entry (e.g. "Launch DropBox") with the new start command (`dbus-launch dropbox start`)
