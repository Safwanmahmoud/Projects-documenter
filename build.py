import cx_Freeze, sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"


executables = [cx_Freeze.Executable("projects_ documenter.py", base=base, targetName="PD")]



cx_Freeze.setup(
   name="NAME_OF_EXE",
   options={"build_exe": {"packages": ["tkinter"],}},
   version="1.0",
   description="automating projects documenting",
   executables=executables
)

