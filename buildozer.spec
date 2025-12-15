[app]
title = KENTA Sudoku
package.name = kentasudoku
package.domain = org.kenta
source.dir = .
source.include_exts = py,yaml,png,jpg
version = 1.0.0
requirements = python3,kivy,pyyaml
orientation = portrait
fullscreen = 0
icon.filename = icon.png
presplash.filename = icon.png

# Android
android.permissions = 
android.api = 33
android.minapi = 21
android.arch = arm64-v8a

# Build
log_level = 2
warn_on_root = 1
