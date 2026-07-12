import json
import os
import shutil
import zipfile
import pathlib
import yaml
from svg import SVG, Rect, Circle, Ellipse, Line, Path, Text, Group, Defs, LinearGradient, RadialGradient, Filter, Polygon, Polyline
from svg.templates import sprite_circle, sprite_rect, sprite_star, sprite_arrow, backdrop_grid, backdrop_color
from scratch import Project, Sprite, BlockBuilder
from scratch.sprite import Costume
from llm import LLMClient
from editor import get_editor_manager
from editor.ui import run_editor_manager
from i18n import get_t


def build_from_llm_output(data):
    project = Project()

    btype = data.get('backdrop', {}).get('type', 'color')
    if btype == 'grid':
        b_svg = backdrop_grid(
            rows=data['backdrop'].get('rows', 3),
            cols=data['backdrop'].get('cols', 4),
            color1=data['backdrop'].get('color1', '#FFFFFF'),
            color2=data['backdrop'].get('color2', '#CCCCCC'))
    else:
        b_svg = backdrop_color(data.get('backdrop', {}).get('color', '#87CEEB'))
    stage = Sprite(name='Stage', is_stage=True)
    stage.add_costume(Costume('backdrop1', b_svg.to_xml()))
    project.add_target(stage)

    for sprite_data in data.get('sprites', []):
        sprite = Sprite(name=sprite_data.get('name', 'Sprite1'))
        sprite.x = sprite_data.get('x', 0)
        sprite.y = sprite_data.get('y', 0)
        sprite.size = sprite_data.get('size', 100)
        sprite.direction = sprite_data.get('direction', 90)

        costume = sprite_data.get('costume', {})
        ctype = costume.get('type', 'circle')
        if ctype == 'circle':
            svg = sprite_circle(costume.get('radius', 50), costume.get('color', '#4A90D9'), costume.get('label'))
        elif ctype == 'rect':
            svg = sprite_rect(costume.get('width', 80), costume.get('height', 80), costume.get('color', '#E74C3C'), costume.get('rx', 8))
        elif ctype == 'star':
            svg = sprite_star(costume.get('size', 60), costume.get('color', '#F1C40F'))
        elif ctype == 'arrow':
            svg = sprite_arrow(costume.get('size', 50), costume.get('color', '#2ECC71'), costume.get('direction', 'right'))
        else:
            svg = sprite_circle(50, '#4A90D9', '?')

        costume_obj = Costume(f'{sprite.name}_costume', svg.to_xml())
        sprite.add_costume(costume_obj)

        bb = BlockBuilder()
        prev_id = None
        for script in sprite_data.get('scripts', []):
            opcode = script['opcode']
            bid = None
            if opcode == 'event_whenflagclicked':
                bid = bb.event_whenflagclicked()
            elif opcode == 'event_whenkeypressed':
                bid = bb.event_whenkeypressed(script.get('key', 'space'))
            elif opcode == 'motion_movesteps':
                bid = bb.motion_movesteps(script.get('steps', 10))
            elif opcode == 'motion_turnright':
                bid = bb.motion_turnright(script.get('degrees', 15))
            elif opcode == 'motion_turnleft':
                bid = bb.motion_turnleft(script.get('degrees', 15))
            elif opcode == 'motion_goto':
                bid = bb.motion_goto(script.get('target', '_mouse_'))
            elif opcode == 'motion_gotoxy':
                bid = bb.motion_gotoxy(script.get('x', 0), script.get('y', 0))
            elif opcode == 'motion_changexby':
                bid = bb.motion_changexby(script.get('dx', 10))
            elif opcode == 'motion_changeyby':
                bid = bb.motion_changeyby(script.get('dy', 10))
            elif opcode == 'motion_setx':
                bid = bb.motion_setx(script.get('x', 0))
            elif opcode == 'motion_sety':
                bid = bb.motion_sety(script.get('y', 0))
            elif opcode == 'motion_ifonedgebounce':
                bid = bb.motion_ifonedgebounce()
            elif opcode == 'looks_say':
                bid = bb.looks_say(script.get('message', ''))
            elif opcode == 'looks_show':
                bid = bb.looks_show()
            elif opcode == 'looks_hide':
                bid = bb.looks_hide()
            elif opcode == 'looks_switchcostumeto':
                bid = bb.looks_switchcostumeto(script.get('costume', ''))
            elif opcode == 'looks_setsizeto':
                bid = bb.looks_setsizeto(script.get('size', 100))
            elif opcode == 'looks_changesizeby':
                bid = bb.looks_changesizeby(script.get('change', 10))
            elif opcode == 'control_wait':
                bid = bb.control_wait(script.get('secs', 1))
            elif opcode == 'control_repeat':
                bid = bb.control_repeat(script.get('times', 10))
            elif opcode == 'control_forever':
                bid = bb.control_forever()
            elif opcode == 'control_if':
                bid = bb.control_if(script.get('condition', True))
            elif opcode == 'control_wait_until':
                bid = bb.control_wait_until(script.get('condition', True))
            elif opcode == 'sensing_touchingobject':
                bid = bb.sensing_touchingobject(script.get('target', 'mouse-pointer'))
            elif opcode == 'operator_add':
                bid = bb.operator_add(script.get('num1', 1), script.get('num2', 2))
            elif opcode == 'operator_subtract':
                bid = bb.operator_subtract(script.get('num1', 1), script.get('num2', 2))
            elif opcode == 'operator_random':
                bid = bb.operator_random(script.get('from', 1), script.get('to', 10))
            elif opcode == 'data_setvariableto':
                bid = bb.data_setvariableto(script.get('var', 'score'), script.get('value', 0))
            elif opcode == 'data_changevariableby':
                bid = bb.data_changevariableby(script.get('var', 'score'), script.get('value', 1))
            elif opcode == 'event_broadcast':
                bid = bb.event_broadcast(script.get('message', 'start'))
            elif opcode == 'twsettings_setFramerate':
                bid = bb.twsettings_setFramerate(script.get('fps', 60))
            elif opcode == 'twsettings_setInterpolation':
                bid = bb.twsettings_setInterpolation(script.get('mode', '开启'))
            elif opcode == 'twsettings_setStageSize':
                bid = bb.twsettings_setStageSize(script.get('size', '2x'))
            elif opcode == 'twsettings_setHighQualityPen':
                bid = bb.twsettings_setHighQualityPen(script.get('mode', '开启'))
            elif opcode == 'twsettings_setCloneLimit':
                bid = bb.twsettings_setCloneLimit(script.get('limit', 300))
            elif opcode == 'twsettings_toggleTurboMode':
                bid = bb.twsettings_toggleTurboMode()
            elif opcode == 'twsettings_setDragMode':
                bid = bb.twsettings_setDragMode(script.get('mode', '可拖拽'))

            if bid and prev_id:
                bb.link_blocks(prev_id, bid)
            if bid:
                prev_id = bid

        sprite.set_blocks(bb.get_blocks())
        project.add_target(sprite)

    return project


def interactive_setup(t):
    print(f'=== {t("app.title")} {t("app.init")} ===')
    print(t('app.no_api'))
    print()

    api_key = input(f'{t("app.api_key")}: ').strip()
    while not api_key:
        api_key = input(f'{t("app.api_key.empty")}: ').strip()

    print()
    print(t('app.provider.select'))
    print('  1. OpenAI          (https://api.openai.com/v1)')
    print('  2. DeepSeek        (https://api.deepseek.com)')
    print('  3. 通义千问        (https://dashscope.aliyuncs.com/compatible-mode/v1)')
    print(f'  4. {t("app.provider.custom")}')
    choice = input(f'{t("app.provider.prompt")}: ').strip()

    providers = {
        '1': ('https://api.openai.com/v1', 'gpt-4o'),
        '2': ('https://api.deepseek.com', 'deepseek-chat'),
        '3': ('https://dashscope.aliyuncs.com/compatible-mode/v1', 'qwen-plus'),
    }

    if choice in providers:
        base_url, model = providers[choice]
    else:
        base_url = input(f'{t("app.provider.url")}: ').strip() or 'https://api.openai.com/v1'
        model = input(f'{t("app.provider.model")}: ').strip() or 'gpt-4o'

    save = input(f'{t("app.config.save")}: ').strip().lower()
    if save == 'y':
        config = {'api_key': api_key, 'base_url': base_url, 'model': model}
        with open('config.yaml', 'w', encoding='utf-8') as f:
            yaml.dump(config, f, allow_unicode=True, default_flow_style=False)
        print(t('app.config.saved', path='config.yaml'))

    return LLMClient(api_key=api_key, base_url=base_url, model=model)


def extract_sb3(sb3_path, output_dir):
    with zipfile.ZipFile(sb3_path, 'r') as zf:
        zf.extractall(output_dir)


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Scratcher')
    parser.add_argument('prompt', nargs='*', help='自然语言描述')
    parser.add_argument('-o', '--output', default='output.sb3', help='输出 .sb3 文件路径')
    parser.add_argument('--api-key', help='LLM API Key')
    parser.add_argument('--base-url', help='LLM API 地址')
    parser.add_argument('--model', help='LLM 模型名称')
    parser.add_argument('--no-llm', action='store_true', help='不使用 LLM，直接生成测试项目')
    parser.add_argument('--editors', action='store_true', help='打开编辑器扩展管理')
    parser.add_argument('--lang', default=None, help='语言: zh / en')

    args = parser.parse_args()
    _tr = get_t(args.lang)

    if args.editors:
        run_editor_manager(args.lang)
        return

    mgr = get_editor_manager()
    mgr.merge_tools()

    if args.no_llm:
        project = Project()
        stage = Sprite(name='Stage', is_stage=True)
        stage_costume = Costume('backdrop1', backdrop_color('#87CEEB').to_xml())
        stage.add_costume(stage_costume)
        project.add_target(stage)

        sprite = Sprite(name='Cat')
        svg = sprite_circle(50, '#4A90D9', '喵')
        sprite.add_costume(Costume('cat_costume', svg.to_xml()))

        bb = BlockBuilder()
        flag = bb.event_whenflagclicked()
        move = bb.motion_movesteps(10, parent_id=flag)
        wait = bb.control_wait(1, parent_id=move)
        turn = bb.motion_turnright(15, parent_id=wait)
        bb.link_blocks(flag, move)
        bb.link_blocks(move, wait)
        bb.link_blocks(wait, turn)
        sprite.set_blocks(bb.get_blocks())
        project.add_target(sprite)

        output = args.output
        project.save(output)
        print(_tr('project.packed', path=output))

        extract_dir = pathlib.Path(output).stem
        extract_sb3(output, extract_dir)
        print(_tr('project.extracted', path=extract_dir))
        for f in sorted(os.listdir(extract_dir)):
            print(f'    {extract_dir}/{f}')
        return

    has_api = bool(args.api_key or os.getenv('LLM_API_KEY'))
    has_config = os.path.exists('config.yaml')
    if not has_api and has_config:
        with open('config.yaml', 'r', encoding='utf-8') as f:
            cfg = yaml.safe_load(f)
        base_url = cfg.get('base_url', '')
        model = cfg.get('model', '')
        if base_url == 'https://api.deepseek.com/v1':
            base_url = 'https://api.deepseek.com'
        if model == 'deepseek-v4-flash':
            model = 'deepseek-chat'
        cfg['base_url'] = base_url
        cfg['model'] = model
        with open('config.yaml', 'w', encoding='utf-8') as f:
            yaml.dump(cfg, f, allow_unicode=True, default_flow_style=False)
        llm = LLMClient(api_key=cfg.get('api_key'), base_url=base_url, model=model)
        print(_tr('app.config.loaded', url=base_url, model=model))
    elif not has_api:
        llm = interactive_setup(_tr)
    else:
        llm = LLMClient(
            api_key=args.api_key,
            base_url=args.base_url,
            model=args.model
        )

    model_name = llm.model if hasattr(llm, 'model') else '?'
    workdir = os.getcwd()
    prompt_queue = ' '.join(args.prompt) if args.prompt else ''

    import itertools, threading, time, sys

    while True:
        if prompt_queue:
            prompt = prompt_queue
            prompt_queue = ''
        else:
            print()
            prompt = input(f'Build-{model_name}-{workdir}> ').strip()
            if prompt.lower() in ('exit', 'quit', 'q'):
                break
            while not prompt:
                prompt = input(f'Build-{model_name}-{workdir}> ').strip()
            if prompt.lower() in ('exit', 'quit', 'q'):
                break

        done = False
        def spin(msg=''):
            for c in itertools.cycle('⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'):
                if done:
                    break
                sys.stdout.write(f'\r  {c} {msg}')
                sys.stdout.flush()
                time.sleep(0.1)
        th = threading.Thread(target=spin, daemon=True)
        th.start()

        try:
            gen = llm.chat_or_generate_stream(prompt)
            first = True
            full_text = ''
            result_type = 'chat'
            result_data = None
            is_json = False
            for tag, value in gen:
                if tag == 'chunk':
                    if first:
                        done = True
                        sys.stdout.write('\r  ')
                        first = False
                    full_text += value
                    if not is_json and (full_text.lstrip().startswith('{') or full_text.lstrip().startswith('```')):
                        is_json = True
                    if not is_json:
                        sys.stdout.write(value)
                        sys.stdout.flush()
                elif tag == 'project':
                    result_type = 'project'
                    result_data = value
                elif tag == 'chat':
                    result_type = 'chat'
                    result_data = value
        except Exception as e:
            done = True
            print(f'\r  {_tr("llm.failed", error=str(e))}')
            continue

        if first:
            done = True
            print(f'\r  ', end='')

        if result_type == 'project':
            print()
            done2 = False
            def spin2(msg):
                for c in itertools.cycle('⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'):
                    if done2:
                        break
                    sys.stdout.write(f'\r  {c} {msg}')
                    sys.stdout.flush()
                    time.sleep(0.1)
            th2 = threading.Thread(target=spin2, daemon=True)
            th2.start()

            project = build_from_llm_output(result_data)
            out = args.output
            if out == 'output.sb3':
                safe = ''.join(c if c.isalnum() or c in ' _-' else '_' for c in prompt[:30])
                out = f'{safe}.sb3'

            project.save(out)
            done2 = True
            print(f'\r  {_tr("project.packed", path=out)}')

            extract_dir = pathlib.Path(out).stem
            extract_sb3(out, extract_dir)
            print(f'  {_tr("project.extracted", path=extract_dir)}')
            for f in sorted(os.listdir(extract_dir)):
                print(f'    {extract_dir}/{f}')
        else:
            print()
            print(full_text)


if __name__ == '__main__':
    main()
