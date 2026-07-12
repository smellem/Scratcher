| BlockType | Tools | Function | JSON Opcode |
| ---- | ---- | ---- | ---- |
| Command | Motion | move `{num}` steps | {"opcode":"motion_movesteps","inputs":{"STEPS":[4,{"type":4,"num":{num}}]}} |
| Command | Motion | turn clockwise `{num}` degrees | {"opcode":"motion_turnright","inputs":{"DEGREES":[4,{"type":4,"num":{num}}]}} |
| Command | Motion | turn counterclockwise `{num}` degrees | {"opcode":"motion_turnleft","inputs":{"DEGREES":[4,{"type":4,"num":{num}}]}} |
| Command | Motion | point towards `{opt}` (direction / mouse pointer / sprite) | {"opcode":"motion_pointtowards","inputs":{"TOWARDS":[10,{"type":1,"opt":{opt}}]}} |
| Command | Motion | go to `{opt}` (random position / mouse pointer / sprite) | {"opcode":"motion_goto","inputs":{"TO":[10,{"type":1,"opt":{opt}}]}} |
| Command | Motion | glide `{num}` secs to `{opt}` (random position / mouse pointer / sprite) | {"opcode":"motion_glideto","inputs":{"SECS":[4,{"type":4,"num":{num}}],"TO":[10,{"type":1,"opt":{opt}}]}} |
| Command | Motion | go to x:`{num}` y:`{num}` | {"opcode":"motion_gotoxy","inputs":{"X":[4,{"type":4,"num":{num}}],"Y":[4,{"type":4,"num":{num}}]}} |
| Command | Motion | change x by `{num}` | {"opcode":"motion_changexby","inputs":{"DX":[4,{"type":4,"num":{num}}]}} |
| Command | Motion | set x to `{num}` | {"opcode":"motion_setx","inputs":{"X":[4,{"type":4,"num":{num}}]}} |
| Command | Motion | change y by `{num}` | {"opcode":"motion_changeyby","inputs":{"DY":[4,{"type":4,"num":{num}}]}} |
| Command | Motion | set y to `{num}` | {"opcode":"motion_sety","inputs":{"Y":[4,{"type":4,"num":{num}}]}} |
| Command | Motion | if on edge, bounce | {"opcode":"motion_ifonedgebounce","inputs":{}} |
| Reporter | Motion | x position | {"opcode":"motion_xposition","inputs":{}} |
| Reporter | Motion | y position | {"opcode":"motion_yposition","inputs":{}} |
| Reporter | Motion | direction | {"opcode":"motion_direction","inputs":{}} |
| Command | Looks | change size by `{num}` | {"opcode":"looks_changesizeby","inputs":{"CHANGE":[4,{"type":4,"num":{num}}]}} |
| Command | Looks | set size to `{num}` % | {"opcode":"looks_setsizeto","inputs":{"SIZE":[4,{"type":4,"num":{num}}]}} |
| Command | Looks | show | {"opcode":"looks_show","inputs":{}} |
| Command | Looks | hide | {"opcode":"looks_hide","inputs":{}} |
| Command | Looks | switch costume to `{opt}` | {"opcode":"looks_switchcostumeto","inputs":{"COSTUME":[10,{"type":1,"opt":{opt}}]}} |
| Command | Looks | next costume | {"opcode":"looks_nextcostume","inputs":{}} |
| Command | Looks | change costume number by `{num}` | {"opcode":"looks_changecostumenumberby","inputs":{"CHANGE":[4,{"type":4,"num":{num}}]}} |
| Command | Looks | set costume number to `{num}` | {"opcode":"looks_setcostumenumberto","inputs":{"NUM":[4,{"type":4,"num":{num}}]}} |
| Command | Looks | switch backdrop to `{opt}` | {"opcode":"looks_switchbackdropto","inputs":{"BACKDROP":[10,{"type":1,"opt":{opt}}]}} |
| Command | Looks | next backdrop | {"opcode":"looks_nextbackdrop","inputs":{}} |
| Command | Looks | change backdrop number by `{num}` | {"opcode":"looks_changebackdropnumberby","inputs":{"CHANGE":[4,{"type":4,"num":{num}}]}} |
| Command | Looks | set backdrop number to `{num}` | {"opcode":"looks_setbackdropnumberto","inputs":{"NUM":[4,{"type":4,"num":{num}}]}} |
| Command | Looks | say `{str}` for `{num}` secs | {"opcode":"looks_sayforsecs","inputs":{"MESSAGE":[10,{"type":0,"str":{str}}],"SECS":[4,{"type":4,"num":{num}}]}} |
| Command | Looks | say `{str}` | {"opcode":"looks_say","inputs":{"MESSAGE":[10,{"type":0,"str":{str}}]}} |
| Command | Looks | think `{str}` for `{num}` secs | {"opcode":"looks_thinkforsecs","inputs":{"MESSAGE":[10,{"type":0,"str":{str}}],"SECS":[4,{"type":4,"num":{num}}]}} |
| Command | Looks | think `{str}` | {"opcode":"looks_think","inputs":{"MESSAGE":[10,{"type":0,"str":{str}}]}} |
| Reporter | Looks | costume number | {"opcode":"looks_costumenumber","inputs":{}} |
| Reporter | Looks | backdrop number | {"opcode":"looks_backdropnumber","inputs":{}} |
| Reporter | Looks | size | {"opcode":"looks_size","inputs":{}} |
| Command | Sound | play sound `{opt}` until done | {"opcode":"sound_playuntildone","inputs":{"SOUND_MENU":[10,{"type":1,"opt":{opt}}]}} |
| Command | Sound | start sound `{opt}` | {"opcode":"sound_play","inputs":{"SOUND_MENU":[10,{"type":1,"opt":{opt}}]}} |
| Command | Sound | stop all sounds | {"opcode":"sound_stopallsounds","inputs":{}} |
| Command | Sound | change volume by `{num}` | {"opcode":"sound_changevolumeby","inputs":{"VOLUME":[4,{"type":4,"num":{num}}]}} |
| Command | Sound | set volume to `{num}` % | {"opcode":"sound_setvolumeto","inputs":{"VOLUME":[4,{"type":4,"num":{num}}]}} |
| Reporter | Sound | volume | {"opcode":"sound_volume","inputs":{}} |
| Hat | Events | when green flag clicked | {"opcode":"event_whenflagclicked","inputs":{}} |
| Hat | Events | when `{opt}` key pressed | {"opcode":"event_whenkeypressed","inputs":{"KEY_OPTION":[10,{"type":1,"opt":{opt}}]}} |
| Hat | Events | when this sprite clicked | {"opcode":"event_whenthisspriteclicked","inputs":{}} |
| Hat | Events | when backdrop switches to `{opt}` | {"opcode":"event_whenbackdropswitchesto","inputs":{"BACKDROP":[10,{"type":1,"opt":{opt}}]}} |
| Hat | Events | when `{opt}` > `{num}` | {"opcode":"event_whengreaterthan","inputs":{"VALUE":[4,{"type":4,"num":{num}}],"WHENGREATERTHAN_MENU":[10,{"type":1,"opt":{opt}}]}} |
| Hat | Events | when I receive `{str}` | {"opcode":"event_whenbroadcastreceived","inputs":{"BROADCAST_INPUT":[10,{"type":0,"str":{str}}]}} |
| Command | Events | broadcast `{str}` | {"opcode":"event_broadcast","inputs":{"BROADCAST_INPUT":[10,{"type":0,"str":{str}}]}} |
| Command | Events | broadcast `{str}` and wait | {"opcode":"event_broadcastandwait","inputs":{"BROADCAST_INPUT":[10,{"type":0,"str":{str}}]}} |
| Command | Control | wait `{num}` secs | {"opcode":"control_wait","inputs":{"DURATION":[4,{"type":4,"num":{num}}]}} |
| Command | Control | repeat `{num}` times [script area] | {"opcode":"control_repeat","inputs":{"TIMES":[4,{"type":4,"num":{num}}],"SUBSTACK":[2,[]]}} |
| Command | Control | forever [script area] | {"opcode":"control_forever","inputs":{"SUBSTACK":[2,[]]}} |
| Command | Control | if `{bool}` then [script area] | {"opcode":"control_if","inputs":{"CONDITION":[10,{"type":2,"bool":{bool}}],"SUBSTACK":[2,[]]}} |
| Command | Control | if `{bool}` then [script area] else [script area] | {"opcode":"control_if_else","inputs":{"CONDITION":[10,{"type":2,"bool":{bool}}],"SUBSTACK":[2,[]],"SUBSTACK2":[2,[]]}} |
| Command | Control | wait until `{bool}` | {"opcode":"control_wait_until","inputs":{"CONDITION":[10,{"type":2,"bool":{bool}}]}} |
| Command | Control | repeat until `{bool}` [script area] | {"opcode":"control_repeat_until","inputs":{"CONDITION":[10,{"type":2,"bool":{bool}}],"SUBSTACK":[2,[]]}} |
| Command | Control | stop `{opt}` (all / this script / other scripts in sprite) | {"opcode":"control_stop","inputs":{"STOP_OPTION":[10,{"type":1,"opt":{opt}}]}} |
| Command | Control | create clone of `{opt}` | {"opcode":"control_create_clone_of","inputs":{"CLONE_OPTION":[10,{"type":1,"opt":{opt}}]}} |
| Hat | Control | when I start as a clone | {"opcode":"control_start_as_clone","inputs":{}} |
| Command | Control | delete this clone | {"opcode":"control_delete_this_clone","inputs":{}} |
| Boolean | Sensing | touching `{opt}` (mouse pointer / edge / sprite) | {"opcode":"sensing_touchingobject","inputs":{"TOUCHINGOBJECTMENU":[10,{"type":1,"opt":{opt}}]}} |
| Boolean | Sensing | touching color `{opt}` | {"opcode":"sensing_touchingcolor","inputs":{"COLOR":[10,{"type":1,"opt":{opt}}]}} |
| Boolean | Sensing | color `{opt}` touching `{opt}` | {"opcode":"sensing_coloristouchingcolor","inputs":{"COLOR":[10,{"type":1,"opt":{opt}}],"COLOR2":[10,{"type":1,"opt":{opt}}]}} |
| Boolean | Sensing | mouse down | {"opcode":"sensing_mousedown","inputs":{}} |
| Boolean | Sensing | key `{opt}` pressed | {"opcode":"sensing_keypressed","inputs":{"KEY_OPTION":[10,{"type":1,"opt":{opt}}]}} |
| Reporter | Sensing | distance to `{opt}` | {"opcode":"sensing_distanceto","inputs":{"DISTANCETOMENU":[10,{"type":1,"opt":{opt}}]}} |
| Reporter | Sensing | mouse x | {"opcode":"sensing_mousex","inputs":{}} |
| Reporter | Sensing | mouse y | {"opcode":"sensing_mousey","inputs":{}} |
| Reporter | Sensing | loudness | {"opcode":"sensing_loudness","inputs":{}} |
| Reporter | Sensing | answer | {"opcode":"sensing_answer","inputs":{}} |
| Boolean | Sensing | timer > `{num}` | {"opcode":"sensing_timer","inputs":{}} |
| Reporter | Sensing | timer | {"opcode":"sensing_timer","inputs":{}} |
| Command | Sensing | reset timer | {"opcode":"sensing_resettimer","inputs":{}} |
| Reporter | Sensing | backdrop name | {"opcode":"sensing_backdropname","inputs":{}} |
| Reporter | Sensing | sprite property `{opt}` of `{opt}` | {"opcode":"sensing_of","inputs":{"PROPERTY":[10,{"type":1,"opt":{opt}}],"OBJECT":[10,{"type":1,"opt":{opt}}]}} |
| Reporter | Operators | `{num}` + `{num}` | {"opcode":"operator_add","inputs":{"NUM1":[4,{"type":4,"num":{num}}],"NUM2":[4,{"type":4,"num":{num}}]}} |
| Reporter | Operators | `{num}` - `{num}` | {"opcode":"operator_subtract","inputs":{"NUM1":[4,{"type":4,"num":{num}}],"NUM2":[4,{"type":4,"num":{num}}]}} |
| Reporter | Operators | `{num}` * `{num}` | {"opcode":"operator_multiply","inputs":{"NUM1":[4,{"type":4,"num":{num}}],"NUM2":[4,{"type":4,"num":{num}}]}} |
| Reporter | Operators | `{num}` / `{num}` | {"opcode":"operator_divide","inputs":{"NUM1":[4,{"type":4,"num":{num}}],"NUM2":[4,{"type":4,"num":{num}}]}} |
| Reporter | Operators | pick random `{num}` to `{num}` | {"opcode":"operator_random","inputs":{"FROM":[4,{"type":4,"num":{num}}],"TO":[4,{"type":4,"num":{num}}]}} |
| Boolean | Operators | `{num}` < `{num}` | {"opcode":"operator_lt","inputs":{"NUM1":[4,{"type":4,"num":{num}}],"NUM2":[4,{"type":4,"num":{num}}]}} |
| Boolean | Operators | `{num}` = `{num}` | {"opcode":"operator_equals","inputs":{"NUM1":[4,{"type":4,"num":{num}}],"NUM2":[4,{"type":4,"num":{num}}]}} |
| Boolean | Operators | `{num}` > `{num}` | {"opcode":"operator_gt","inputs":{"NUM1":[4,{"type":4,"num":{num}}],"NUM2":[4,{"type":4,"num":{num}}]}} |
| Boolean | Operators | `{bool}` and `{bool}` | {"opcode":"operator_and","inputs":{"OPERAND1":[10,{"type":2,"bool":{bool}}],"OPERAND2":[10,{"type":2,"bool":{bool}}]}} |
| Boolean | Operators | `{bool}` or `{bool}` | {"opcode":"operator_or","inputs":{"OPERAND1":[10,{"type":2,"bool":{bool}}],"OPERAND2":[10,{"type":2,"bool":{bool}}]}} |
| Boolean | Operators | not `{bool}` | {"opcode":"operator_not","inputs":{"OPERAND":[10,{"type":2,"bool":{bool}}]}} |
| Reporter | Operators | join `{str}` `{str}` | {"opcode":"operator_join","inputs":{"STRING1":[10,{"type":0,"str":{str}}],"STRING2":[10,{"type":0,"str":{str}}]}} |
| Reporter | Operators | letter `{num}` of `{str}` | {"opcode":"operator_letter_of","inputs":{"LETTER":[4,{"type":4,"num":{num}}],"STRING":[10,{"type":0,"str":{str}}]}} |
| Reporter | Operators | length of `{str}` | {"opcode":"operator_length","inputs":{"STRING":[10,{"type":0,"str":{str}}]}} |
| Boolean | Operators | `{str}` contains `{str}` | {"opcode":"operator_contains","inputs":{"STRING1":[10,{"type":0,"str":{str}}],"STRING2":[10,{"type":0,"str":{str}}]}} |
| Reporter | Operators | `{num}` mod `{num}` | {"opcode":"operator_mod","inputs":{"NUM1":[4,{"type":4,"num":{num}}],"NUM2":[4,{"type":4,"num":{num}}]}} |
| Reporter | Operators | round `{num}` | {"opcode":"operator_round","inputs":{"NUM":[4,{"type":4,"num":{num}}]}} |
| Reporter | Operators | `{opt}` of `{num}` (abs / sqrt / sin / cos / tan / log / ln / e^ / 10^) | {"opcode":"operator_mathop","inputs":{"NUM":[4,{"type":4,"num":{num}}],"OPERATOR":[10,{"type":1,"opt":{opt}}]}} |
| Command | Variables | set `{var}` to `{num}` | {"opcode":"data_setvariableto","inputs":{"VALUE":[4,{"type":4,"num":{num}}]},"fields":{"VARIABLE":[10,{"type":3,"var":{var}}]}} |
| Command | Variables | change `{var}` by `{num}` | {"opcode":"data_changevariableby","inputs":{"VALUE":[4,{"type":4,"num":{num}}]},"fields":{"VARIABLE":[10,{"type":3,"var":{var}}]}} |
| Command | Variables | show variable `{var}` | {"opcode":"data_showvariable","fields":{"VARIABLE":[10,{"type":3,"var":{var}}]}} |
| Command | Variables | hide variable `{var}` | {"opcode":"data_hidevariable","fields":{"VARIABLE":[10,{"type":3,"var":{var}}]}} |
| Reporter | Variables | `{var}` | {"opcode":"data_variable","fields":{"VARIABLE":[10,{"type":3,"var":{var}}]}} |
| Command | Lists | add `{str}` to `{list}` | {"opcode":"data_addtolist","inputs":{"ITEM":[10,{"type":0,"str":{str}}]},"fields":{"LIST":[10,{"type":6,"list":{list}}]}} |
| Command | Lists | delete `{num}` of `{list}` | {"opcode":"data_deleteoflist","inputs":{"INDEX":[4,{"type":4,"num":{num}}]},"fields":{"LIST":[10,{"type":6,"list":{list}}]}} |
| Command | Lists | insert `{str}` at `{num}` of `{list}` | {"opcode":"data_insertatlist","inputs":{"INDEX":[4,{"type":4,"num":{num}}],"ITEM":[10,{"type":0,"str":{str}}]},"fields":{"LIST":[10,{"type":6,"list":{list}}]}} |
| Command | Lists | replace item `{num}` of `{list}` with `{str}` | {"opcode":"data_replaceitemoflist","inputs":{"INDEX":[4,{"type":4,"num":{num}}],"ITEM":[10,{"type":0,"str":{str}}]},"fields":{"LIST":[10,{"type":6,"list":{list}}]}} |
| Reporter | Lists | item `{num}` of `{list}` | {"opcode":"data_itemoflist","inputs":{"INDEX":[4,{"type":4,"num":{num}}]},"fields":{"LIST":[10,{"type":6,"list":{list}}]}} |
| Reporter | Lists | length of `{list}` | {"opcode":"data_lengthoflist","fields":{"LIST":[10,{"type":6,"list":{list}}]}} |
| Boolean | Lists | `{list}` contains `{str}` | {"opcode":"data_listcontainsitem","inputs":{"ITEM":[10,{"type":0,"str":{str}}]},"fields":{"LIST":[10,{"type":6,"list":{list}}]}} |
| Command | Lists | show list `{list}` | {"opcode":"data_showlist","fields":{"LIST":[10,{"type":6,"list":{list}}]}} |
| Command | Lists | hide list `{list}` | {"opcode":"data_hidelist","fields":{"LIST":[10,{"type":6,"list":{list}}]}} |
| Hat | My Blocks | define `{str}` [custom input slots] | {"opcode":"procedures_definition","inputs":{},"fields":{"PROCEDURE":[10,{"type":0,"str":{str}}]}} |
| Command | My Blocks | `{str}` [custom input slots] | {"opcode":"procedures_call","inputs":{},"fields":{"PROCEDURE":[10,{"type":0,"str":{str}}]}} |
| Command | Motion | glide to x:`{num}` y:`{num}` in `{num}` secs | {"opcode":"motion_glidesecstoxy","inputs":{"SECS":[4,{"type":4,"num":{num}}],"X":[4,{"type":4,"num":{num}}],"Y":[4,{"type":4,"num":{num}}]}} |
| Command | Motion | set rotation style `{opt}` | {"opcode":"motion_setrotationstyle","inputs":{"STYLE":[10,{"type":1,"opt":{opt}}]}} |
| Command | Looks | go to front layer | {"opcode":"looks_gotofront","inputs":{}} |
| Command | Looks | go back `{num}` layers | {"opcode":"looks_gobackbylayers","inputs":{"NUM":[4,{"type":4,"num":{num}}]}} |
