[app]
title = Bus Announcer
package.name = busannouncer
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3
version = 1.0.0

requirements = python3, kivy, plyer, gtts
android.permissions = ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, ACCESS_BACKGROUND_LOCATION

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
