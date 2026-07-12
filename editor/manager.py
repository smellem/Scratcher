import json
import os
import shutil
import tempfile
import zipfile

EDITOR_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'editor')
AGENT_TOOLS = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'agent', 'tools.md')
AGENT_TOOLS_BASE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'agent', 'tools.base.md')


class Editor:
    def __init__(self, filename, pack):
        self.filename = filename
        self.filepath = os.path.join(EDITOR_DIR, filename)
        self.name = pack.get('name', filename)
        self.version = pack.get('version', '0.0.0')
        self.description = pack.get('description', '')
        self.author = pack.get('author', '')
        self.enabled = pack.get('enabled', True)
        self.pack_type = pack.get('type', 'editor')
        self.entry = pack.get('entry', '')

    def toggle(self):
        self.enabled = not self.enabled
        self._save_pack()

    def _save_pack(self):
        tmp = tempfile.mkdtemp()
        try:
            with zipfile.ZipFile(self.filepath, 'r') as zf:
                zf.extractall(tmp)
            pack_path = os.path.join(tmp, 'pack.json')
            with open(pack_path, 'r', encoding='utf-8') as f:
                pack = json.load(f)
            pack['enabled'] = self.enabled
            with open(pack_path, 'w', encoding='utf-8') as f:
                json.dump(pack, f, ensure_ascii=False, indent=2)
            os.remove(self.filepath)
            shutil.make_archive(self.filepath.replace('.editor', ''), 'zip', tmp)
            os.rename(self.filepath.replace('.editor', '.zip'), self.filepath)
        finally:
            shutil.rmtree(tmp)

    def __repr__(self):
        status = 'ON' if self.enabled else 'OFF'
        tag = f' [{self.pack_type}]' if self.pack_type != 'editor' else ''
        return f'[{status}] {self.name} v{self.version}{tag} - {self.description}'


class EditorManager:
    def __init__(self):
        self.editors = []
        self._scan()

    def _scan(self):
        self.editors = []
        if not os.path.isdir(EDITOR_DIR):
            return
        for f in sorted(os.listdir(EDITOR_DIR)):
            if f.endswith('.editor') and f != 'create_sample.py':
                filepath = os.path.join(EDITOR_DIR, f)
                try:
                    with zipfile.ZipFile(filepath, 'r') as zf:
                        pack_data = json.loads(zf.read('pack.json').decode('utf-8'))
                    self.editors.append(Editor(f, pack_data))
                except Exception:
                    pass

    def get_enabled_editors(self):
        return [e for e in self.editors if e.enabled]

    def merge_tools(self):
        base_path = AGENT_TOOLS_BASE if os.path.exists(AGENT_TOOLS_BASE) else AGENT_TOOLS
        try:
            with open(base_path, 'r', encoding='utf-8') as f:
                base = f.read().strip()
        except FileNotFoundError:
            base = ''

        parts = [base]
        for editor in self.get_enabled_editors():
            try:
                with zipfile.ZipFile(editor.filepath, 'r') as zf:
                    content = zf.read('agent/tools.md').decode('utf-8')
                lines = [l.strip() for l in content.splitlines() if l.strip()]
                if len(lines) > 2:
                    parts.append('\n'.join(lines[2:]))
            except Exception:
                pass

        with open(AGENT_TOOLS, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(parts))

    def toggle(self, index):
        if 0 <= index < len(self.editors):
            self.editors[index].toggle()

    def install(self, editor_path):
        dest = os.path.join(EDITOR_DIR, os.path.basename(editor_path))
        shutil.copy2(editor_path, dest)
        self._scan()

    def remove(self, index):
        if 0 <= index < len(self.editors):
            os.remove(self.editors[index].filepath)
            self._scan()


_manager = None


def get_editor_manager():
    global _manager
    if _manager is None:
        _manager = EditorManager()
    return _manager
