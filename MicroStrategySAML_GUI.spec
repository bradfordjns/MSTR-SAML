# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\bjones\\PycharmProjects\\XML_EDITS_GUI\\MicroStrategySAML_GUI.py'],
             pathex=['C:\\Users\\bjones\\PycharmProjects\\XML_EDITS_GUI'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='MicroStrategySAML_GUI',
          debug=False,
          strip=False,
          upx=True,
          console=False , version='C:\\Users\\bjones\\PycharmProjects\\XML_EDITS_GUI\\version.txt', icon='C:\\Users\\bjones\\PycharmProjects\\XML_EDITS_GUI\\KEY.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='MicroStrategySAML_GUI')
