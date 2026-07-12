import os
from .manager import get_editor_manager
from i18n import get_t


def run_editor_manager(lang=None):
    mgr = get_editor_manager()
    _tr = get_t(lang)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'=== Scratcher {_tr("editor.title")} ===')
        print()

        if not mgr.editors:
            print(_tr('editor.empty'))
        else:
            for i, editor in enumerate(mgr.editors):
                print(f'  {i + 1}. {editor}')

        print()
        print(_tr('editor.actions'))
        print(f'  {_tr("editor.toggle")}')
        print(f'  {_tr("editor.install")}')
        print(f'  {_tr("editor.delete")}')
        print(f'  {_tr("editor.export")}')
        print(f'  {_tr("editor.merge")}')
        print(f'  {_tr("editor.quit")}')
        print()

        cmd = input('> ').strip().lower()
        if cmd == 'q':
            return
        elif cmd == 'm':
            mgr.merge_tools()
            print(_tr('editor.merged'))
            input('回车继续...')
        elif cmd.startswith('i '):
            path = cmd[2:].strip()
            if os.path.exists(path):
                mgr.install(path)
                print(_tr('editor.installed', path=path))
            else:
                print(_tr('editor.not_found', path=path))
            input('回车继续...')
        elif cmd.startswith('d '):
            try:
                idx = int(cmd[2:].strip()) - 1
                mgr.remove(idx)
                print(_tr('editor.deleted'))
            except (ValueError, IndexError):
                print(_tr('editor.invalid'))
            input('回车继续...')
        elif cmd.startswith('e '):
            try:
                idx = int(cmd[2:].strip()) - 1
                editor = mgr.editors[idx]
                import zipfile, tempfile, shutil
                tmp = tempfile.mkdtemp()
                try:
                    with zipfile.ZipFile(editor.filepath, 'r') as zf:
                        zf.extractall(tmp)
                    if editor.pack_type == 'turbowarp' and editor.entry:
                        src = os.path.join(tmp, editor.entry)
                        if os.path.exists(src):
                            dst = os.path.join(os.getcwd(), editor.entry)
                            shutil.copy2(src, dst)
                            print(_tr('editor.exported', path=dst))
                            print(_tr('editor.export_hint'))
                    else:
                        print(_tr('editor.no_export'))
                finally:
                    shutil.rmtree(tmp)
            except (ValueError, IndexError):
                print(_tr('editor.invalid'))
            input('回车继续...')
        else:
            try:
                idx = int(cmd) - 1
                mgr.toggle(idx)
            except (ValueError, IndexError):
                pass