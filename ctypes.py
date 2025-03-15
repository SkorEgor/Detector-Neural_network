# noinspection PyPep8Naming
def __getattr__(attr: str) -> object:
    import sys
    from os import name, getcwd

    if attr == "windll" and name != "nt":

        class windll:
            class shell32:
                @staticmethod
                def SetCurrentProcessExplicitAppUserModelID(_):
                    return None

        return windll

    cwd: str = getcwd()
    revert_sys_path: bool = False

    if cwd in sys.path:
        sys.path.remove(cwd)
        revert_sys_path = True

    sys.modules.pop("ctypes")

    import ctypes

    if revert_sys_path:
        sys.path.append(cwd)

    return getattr(ctypes, attr)
