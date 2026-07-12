import json
import io
import zipfile


class Project:
    def __init__(self):
        self.targets = []
        self.meta = {
            "semver": "3.0.0",
            "vm": "0.2.0",
            "agent": "Scratcher"
        }
        self._assets = {}

    def add_target(self, target):
        self.targets.append(target)

    def _collect_assets(self):
        self._assets = {}
        for target in self.targets:
            for costume in target.costumes:
                self._assets[costume.asset_id] = {
                    'data': costume.svg_xml.encode('utf-8'),
                    'ext': '.svg'
                }
            for sound in target.sounds:
                self._assets[sound.asset_id] = {
                    'data': b'',
                    'ext': '.wav'
                }

    def save(self, path):
        self._collect_assets()
        project_json = {
            "targets": [t.to_dict() for t in self.targets],
            "monitors": [],
            "extensions": [],
            "meta": self.meta
        }
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
            zf.writestr('project.json', json.dumps(project_json, separators=(',', ':')))
            for asset_id, asset in self._assets.items():
                zf.writestr(f'{asset_id}{asset["ext"]}', asset['data'])
        with open(path, 'wb') as f:
            f.write(buffer.getvalue())
