---
Title: Temporary files format that can be deleted from project of Visual Studio 2010
Author: SergeM
Date: 2014-01-14 12:36:00
Slug: temporary-files-format-that-can-be
aliases: [/temporary-files-format-that-can-be.html]
Tags: [ c++,2010,git,visual studio]
---



Add to .gitignore:



* `*.ipch`
* Debug
* Release
* `*.sdf` - The SDF file is your code browsing database which uses SQL Sever Compact Edition. You don't need to copy this SDF file while you move your project, and it will be automatically populated in the new location once you open your project.

[[1](http://social.msdn.microsoft.com/Forums/en-US/20fee924-e267-4c1a-b0fe-3321f86e1bb5/sdf-file?forum=vcprerelease" target="_blank)]

[[2](http://social.msdn.microsoft.com/Forums/vstudio/en-US/1ef46540-e4b8-4779-8403-49239bc3f7ee/is-it-safe-to-delete-ipch-folder-precompiled-headers?forum=vcgeneral" target="_blank)]
