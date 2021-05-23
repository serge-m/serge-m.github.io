---
Title: IDE for Rust
Author: SergeM
Date: 2021-05-23 12:30:00
Slug: ide-for-rust
Tags: [ rust, IDE, vscode, debug ]
---

I started to learn rust, and I needed to set up some IDE to handle my exercises. It seems that 
VScode has pretty good support for Rust.

# How to set up VS code to work with rust, including debugging.

Install `rust-analyzer` extension and `vscode-lldb` extension: 

    code --install-extension matklad.rust-analyzer
    code --install-extension vadimcn.vscode-lldb


`rust-analyzer` provides a nice UI for running binaries and tests:

![](/media/2021-05-23/rust-analyzer-run-buttons.png)

Also it gives a lot of hints:

![](/media/2021-05-23/rust-analyzer-hints.png)

Note that `rust-analyzer` doesn't work together with `Rust` extension (Rust for Visual Studio Code). You would have to uninstall or debug the later.

We needed `vscode-lldb` to support debugging. Now if you hit `F5` VScode will suggest to create a launch configuration for it. The default one works well. After that one can use keyboard shortcuts to debug. 

```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug executable 'vscode_rust_template'",
            "cargo": {
                "args": [
                    "build",
                    "--bin=vscode_rust_template",
                    "--package=vscode_rust_template"
                ],
                "filter": {
                    "name": "vscode_rust_template",
                    "kind": "bin"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug unit tests in executable 'vscode_rust_template'",
            "cargo": {
                "args": [
                    "test",
                    "--no-run",
                    "--bin=vscode_rust_template",
                    "--package=vscode_rust_template"
                ],
                "filter": {
                    "name": "vscode_rust_template",
                    "kind": "bin"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        }
    ]
}
```
