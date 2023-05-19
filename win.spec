# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['E:\\git_desktop\\testBom\\manage.py'],
    pathex=['E:\\git_desktop\\testBom'],
    binaries=[],
    datas=[
        ('templates/dist/spa', 'templates/dist/spa'),
        ('static_new', 'static_new'),
        ('static', 'static'),
        ('media', 'media'),
        ('logs', 'logs'),
        ('GreaterWMS-Start.exe', '.')
    ],
    hiddenimports=[
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ],
    hookspath=['E:\\git_desktop\\venv\\greaterwms\\Bomiot\\Lib\\site-packages\\pyupdater\\hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'f2py',
        'coreschema'
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='win',
    debug=False,
    embed_manifest=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='logo.ico',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='win',
)
