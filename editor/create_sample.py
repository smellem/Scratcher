import json, os, shutil

tmp = os.path.join(os.path.dirname(__file__), '_tmp')
os.makedirs(os.path.join(tmp, 'agent'), exist_ok=True)

pack = {'name': '运动扩展', 'version': '1.0.0', 'description': '添加更多运动类积木', 'author': 'Scratcher', 'enabled': True}
with open(os.path.join(tmp, 'pack.json'), 'w', encoding='utf-8') as f:
    json.dump(pack, f, ensure_ascii=False, indent=2)

tools_lines = [
    '| BlockType | Tools | Function | JSON Opcode |',
    '| ---- | ---- | ---- | ---- |',
    '| Command | Motion | glide to x:`{num}` y:`{num}` in `{num}` secs | {"opcode":"motion_glidesecstoxy","inputs":{"SECS":[4,{"type":4,"num":{num}}],"X":[4,{"type":4,"num":{num}}],"Y":[4,{"type":4,"num":{num}}]}} |',
    '| Command | Motion | set rotation style `{opt}` | {"opcode":"motion_setrotationstyle","inputs":{"STYLE":[10,{"type":1,"opt":{opt}}]}} |',
    '| Command | Looks | go to front layer | {"opcode":"looks_gotofront","inputs":{}} |',
    '| Command | Looks | go back `{num}` layers | {"opcode":"looks_gobackbylayers","inputs":{"NUM":[4,{"type":4,"num":{num}}]}} |',
]
with open(os.path.join(tmp, 'agent', 'tools.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(tools_lines))

output = os.path.join(os.path.dirname(__file__), 'motion-plus.editor')
shutil.make_archive(output.replace('.editor', ''), 'zip', tmp)
os.rename(output.replace('.editor', '.zip'), output)
shutil.rmtree(tmp)
print(f'Created: {output}')
