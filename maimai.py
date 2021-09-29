import time

from nonebot.typing import State_T
from hoshino import Service, priv
from hoshino.typing import CQEvent
from collections import defaultdict
import os, re, asyncio, json, traceback

from .libraries.maimai_best_40 import *
from .libraries.image import *
from .libraries.maimaidx_music import *
from .libraries.tool import hash
from .libraries.maimaidx_guess import GuessObject

sv_help = '''可用命令如下：
帮助maimaiDX 查看指令帮助
今日mai,今日舞萌,今日运势 查看今天的舞萌运势
XXXmaimaiXXX什么 随机一首歌
随个[dx/标准][绿黄红紫白]<难度> 随机一首指定条件的乐曲
查歌<乐曲标题的一部分> 查询符合条件的乐曲
[绿黄红紫白]id <歌曲编号> 查询乐曲信息或谱面信息
<歌曲别名>是什么歌 查询乐曲别名对应的乐曲
<id/歌曲别称>有什么别称 查询乐曲对应的别称 识别id，歌名和别称
定数查歌 <定数>  查询定数对应的乐曲
定数查歌 <定数下限> <定数上限>
分数线 <难度+歌曲id> <分数线> 详情请输入“分数线 帮助”查看
开启/关闭mai猜歌 开关猜歌功能
猜歌 顾名思义，识别id，歌名和别称
b40 <名字> 查B40
b50 <名字> 查B50
我要(在<难度>)上<分数>分 <名字> 查看推荐的上分乐曲'''

sv = Service('maimaiDX', manage_priv=priv.ADMIN, enable_on_default=False, help_=sv_help)

static = os.path.join(os.path.dirname(__file__), 'static')

def random_music(music: Music) -> str:
    msg = f'''{music.id}. {music.title}
[CQ:image,file=https://www.diving-fish.com/covers/{music.id}.jpg]
{'/'.join(list(map(str, music.ds)))}'''
    return msg

def song_level(ds1: float, ds2: float = None) -> list:
    result = []
    diff_label = ['Bas', 'Adv', 'Exp', 'Mst', 'ReM']
    if ds2 is not None:
        music_data = total_list.filter(ds=(ds1, ds2))
    else:
        music_data = total_list.filter(ds=ds1)
    for music in sorted(music_data, key = lambda i: int(i['id'])):
        for i in music.diff:
            result.append((music['id'], music['title'], music['ds'][i], diff_label[i], music['level'][i]))
    return result

@sv.on_prefix('帮助maimaiDX')
async def dx_help(bot, ev: CQEvent):
    await bot.send(ev, f'[CQ:image,file=base64://{image_to_base64(text_to_image(sv_help)).decode()}]', at_sender=True)

@sv.on_prefix('定数查歌')
async def search_dx_song_level(bot, ev: CQEvent):
    args = ev.message.extract_plain_text().strip().split()
    if len(args) > 2 or len(args) == 0:
        await bot.finish(ev, '命令格式为\n定数查歌 <定数>\n定数查歌 <定数下限> <定数上限>', at_sender=True)
    if len(args) == 1:
        result = song_level(float(args[0]))
    else:
        result = song_level(float(args[0]), float(args[1]))
    if len(result) >= 60:
        await bot.finish(ev, f'结果过多（{len(result)} 条），请缩小搜索范围', at_sender=True)
    msg = ''
    for i in result:
        msg += f'{i[0]}. {i[1]} {i[3]} {i[4]}({i[2]})\n'
    await bot.finish(ev, f'[CQ:image,file=base64://{image_to_base64(text_to_image(msg.strip())).decode()}]', at_sender=True)

@sv.on_rex(r'^随个((?:dx|sd|标准))?([绿黄红紫白]?)([0-9]+\+?)')
async def random_song(bot, ev: CQEvent):
    try:
        match = ev['match']
        diff = match.group(1)
        if diff == 'dx':
            tp = ['DX']
        elif diff == 'sd' or diff == '标准':
            tp = ['SD']
        else:
            tp = ['SD', 'DX']
        level = match.group(3)
        if match.group(2) == '':
            music_data = total_list.filter(level=level, type=tp)
        else:
            music_data = total_list.filter(level=level, diff=['绿黄红紫白'.index(match.group(2))], type=tp)
        if len(music_data) == 0:
            msg = '没有这样的乐曲哦。'
        else:
            msg = random_music(music_data.random())
        await bot.send(ev, msg, at_sender=True)
    except:
        await bot.send(ev, '随机命令错误，请检查语法', at_sender=True)

@sv.on_rex(r'.*mai.*什么')
async def random_day_song(bot, ev: CQEvent):
    await bot.send(ev, random_music(total_list.random()))

@sv.on_prefix('查歌')
async def search_song(bot, ev: CQEvent):
    name = ev.message.extract_plain_text().strip()
    if not name:
        return
    result = total_list.filter(title_search=name)
    if len(result) == 0:
        await bot.send(ev, '没有找到这样的乐曲。', at_sender=True)
    elif len(result) < 50:
        search_result = ''
        for music in sorted(result, key=lambda i: int(i['id'])):
            search_result += f'{music["id"]}. {music["title"]}\n'
        await bot.send(ev, search_result.strip(), at_sender=True)
    else:
        await bot.send(ev, f'结果过多（{len(result)} 条），请缩小查询范围。', at_sender=True)

@sv.on_rex(r'^([绿黄红紫白]?)\s?id\s?([0-9]+)')
async def query_chart(bot, ev: CQEvent):
    match = ev['match']
    level_labels = ['绿', '黄', '红', '紫', '白']
    if match.group(1) != '':
        try:
            level_index = level_labels.index(match.group(1))
            level_name = ['Basic', 'Advanced', 'Expert', 'Master', 'Re: MASTER']
            name = match.group(2)
            music = total_list.by_id(name)
            chart = music['charts'][level_index]
            ds = music['ds'][level_index]
            level = music['level'][level_index]
            if len(chart['notes']) == 4:
                result = f'''{level_name[level_index]} {level}({ds})
TAP: {chart['notes'][0]}
HOLD: {chart['notes'][1]}
SLIDE: {chart['notes'][2]}
BREAK: {chart['notes'][3]}
谱师: {chart['charter']}'''
            else:
                result = f'''{level_name[level_index]} {level}({ds})
TAP: {chart['notes'][0]}
HOLD: {chart['notes'][1]}
SLIDE: {chart['notes'][2]}
TOUCH: {chart['notes'][3]}
BREAK: {chart['notes'][4]}
谱师: {chart['charter']}'''

            msg = f'''
{music["id"]}. {music["title"]}
[CQ:image,file=https://www.diving-fish.com/covers/{music["id"]}.jpg]
{result}'''
            await bot.send(ev, msg, at_sender=True)
        except:
            await bot.send(ev, '未找到该谱面', at_sender=True)
    else:
        try:
            name = match.group(2)
            music = total_list.by_id(name)
            msg = f'''{music["id"]}. {music["title"]}
[CQ:image,file=https://www.diving-fish.com/covers/{music["id"]}.jpg]
艺术家: {music['basic_info']['artist']}
分类: {music['basic_info']['genre']}
BPM: {music['basic_info']['bpm']}
版本: {music['basic_info']['from']}
定数: {'/'.join([str(i) for i in music['ds']])}
难度: {'/'.join(list(map(str, music["ds"])))}'''
            await bot.send(ev, msg, at_sender=True)
        except:
            await bot.send(ev, '未找到该乐曲', at_sender=True)

@sv.on_fullmatch(['今日mai', '今日舞萌', '今日运势'])
async def day_mai(bot, ev: CQEvent):
    wm_list = ['拼机', '推分', '越级', '下埋', '夜勤', '练底力', '练手法', '打旧框', '干饭', '抓绝赞', '收歌']
    uid = ev.user_id
    h = hash(uid)
    rp = h % 100
    wm_value = []
    for i in range(11):
        wm_value.append(h & 3)
        h >>= 2
    msg = f'\n今日人品值：{rp}\n'
    for i in range(11):
        if wm_value[i] == 3:
            msg += f'宜 {wm_list[i]}\n'
        elif wm_value[i] == 0:
            msg += f'忌 {wm_list[i]}\n'
    msg += f'{NICKNAME} Bot提醒您：打机时不要大力拍打或滑动哦\n今日推荐歌曲：'
    music = total_list[h % len(total_list)]
    msg += random_music(music)
    await bot.send(ev, msg, at_sender=True)

music_aliases = defaultdict(list)
f = open(os.path.join(static, 'aliases.csv'), 'r', encoding='utf-8')
tmp = f.readlines()
f.close()
for t in tmp:
    arr = t.strip().split('\t')
    for i in range(len(arr)):
        if arr[i] != '':
            music_aliases[arr[i].lower()].append(arr[0])

@sv.on_suffix('是什么歌')
async def what_song(bot, ev: CQEvent):
    name = ev.message.extract_plain_text().strip().lower()
    if name not in music_aliases:
        await bot.finish(ev, '未找到此歌曲\n舞萌 DX 歌曲别名收集计划：https://docs.qq.com/sheet/DQ0pvUHh6b1hjcGpl', at_sender=True)
    result = music_aliases[name]
    if len(result) == 1:
        music = total_list.by_title(result[0])
        await bot.send(ev, '您要找的是不是：' + random_music(music), at_sender=True)
    else:
        msg = '\n'.join(result)
        await bot.send(ev, f'您要找的可能是以下歌曲中的其中一首：\n{msg}', at_sender=True)

@sv.on_suffix('有什么别称')
async def how_song(bot, ev: CQEvent):
    name = ev.message.extract_plain_text().strip().lower()
    if name.isdigit():
        music = total_list.by_id(name)
        if music:
            title = music_aliases[music.title.lower()]
        else:
            await bot.finish(ev, '未找到此歌曲', at_sender=True)
    else:
        if name not in music_aliases:
            await bot.finish(ev, '未找到此歌曲', at_sender=True)
        title = music_aliases[name]
    result = []
    for key, value in music_aliases.items():
        for t in title:
            if t in value and key not in result:
                result.append(key)
    if len(result) == 0 or len(result) == 1:
        await bot.finish(ev, '该曲目没有别称', at_sender=True)
    else:
        msg = f'该曲目有以下别称：\n'
        for r in result:
            msg += f'{r}\n'
        await bot.send(ev, msg, at_sender=True)

@sv.on_prefix('分数线')
async def quert_score(bot, ev: CQEvent):
    text = ev.message.extract_plain_text().strip()
    args = ev.message.extract_plain_text().strip().split()
    if len(args) == 1 and args[0] == '帮助':
        msg = '''此功能为查找某首歌分数线设计。
命令格式：分数线 <难度+歌曲id> <分数线>
例如：分数线 紫799 100
命令将返回分数线允许的 TAP GREAT 容错以及 BREAK 50落等价的 TAP GREAT 数。
以下为 TAP GREAT 的对应表：
GREAT/GOOD/MISS
TAP\t1/2.5/5
HOLD\t2/5/10
SLIDE\t3/7.5/15
TOUCH\t1/2.5/5
BREAK\t5/12.5/25(外加200落)'''
        await bot.send(ev, f'[CQ:image,file=base64://{image_to_base64(text_to_image(msg)).decode()}]', at_sender=True)
    else:
        try:
            result = re.search(r'([绿黄红紫白])\s?([0-9]+)', text)
            level_labels = ['绿', '黄', '红', '紫', '白']
            level_labels2 = ['Basic', 'Advanced', 'Expert', 'Master', 'Re:MASTER']
            level_index = level_labels.index(result.group(1))
            chart_id = result.group(2)
            line = float(args[-1])
            music = total_list.by_id(chart_id)
            chart: Dict[Any] = music['charts'][level_index]
            tap = int(chart['notes'][0])
            slide = int(chart['notes'][2])
            hold = int(chart['notes'][1])
            touch = int(chart['notes'][3]) if len(chart['notes']) == 5 else 0
            brk = int(chart['notes'][-1])
            total_score = 500 * tap + slide * 1500 + hold * 1000 + touch * 500 + brk * 2500
            break_bonus = 0.01 / brk
            break_50_reduce = total_score * break_bonus / 4
            reduce = 101 - line
            if reduce <= 0 or reduce >= 101:
                raise ValueError
            msg = f'''{music['title']} {level_labels2[level_index]}
分数线 {line}% 允许的最多 TAP GREAT 数量为 {(total_score * reduce / 10000):.2f}(每个-{10000 / total_score:.4f}%),
BREAK 50落(一共{brk}个)等价于 {(break_50_reduce / 100):.3f} 个 TAP GREAT(-{break_50_reduce / total_score * 100:.4f}%)'''
            await bot.send(ev, msg, at_sender=True)
        except:
            await bot.send(ev, '格式错误，输入“分数线 帮助”以查看帮助信息', at_sender=True)

@sv.on_rex('^[Bb]([45])0\s?(.+)?')
async def best_40(bot, ev: CQEvent):
    match = ev['match']
    if not match.group(2):
        payload = {'qq': str(ev.user_id)}
    else:
        payload = {'username': match.group(2)}
    if match.group(1) == '5': payload['b50'] = True
    img, success = await generate(payload)
    if success == 400:
        await bot.send(ev, '未找到此玩家，请确保此玩家的用户名和查分器中的用户名相同。', at_sender=True)
    elif success == 403:
        await bot.send(ev, '该用户禁止了其他人获取数据。', at_sender=True)
    else:
        await bot.send(ev, f'[CQ:image,file=base64://{image_to_base64(img).decode()}]', at_sender=True)

@sv.on_rex('^我要在?([0-9]+\+?)?上([0-9]+)分\s?(.+)?')  # 慎用，垃圾代码非常吃机器性能
async def rise_score(bot, ev: CQEvent):
    match = ev['match']
    if not match.group(3):
        payload = {'qq': str(ev.user_id)}
    else:
        payload = {'username': match.group(3)}
    player_data, success = await get_player_data(payload)
    if success == 400:
        await bot.send(ev, '未找到此玩家，请确保此玩家的用户名和查分器中的用户名相同。', at_sender=True)
    elif success == 403:
        await bot.send(ev, '该用户禁止了其他人获取数据。', at_sender=True)
    else:
        dx_ra_lowest = 999
        sd_ra_lowest = 999
        achievement_list = [50.0, 60.0, 70.0, 75.0, 80.0, 90.0, 94.0, 97.0, 98.0, 99.0, 99.5, 100.0, 100.5]
        rank = ['C', 'B', 'BB', 'BBB', 'A', 'AA', 'AAA', 'S', 'S+', 'SS', 'SS+', 'SSS', 'SSS+']
        player_dx_list = []
        player_sd_list = []
        music_dx_list = []
        music_sd_list = []
        for dx in player_data['charts']['dx']:
            dx_ra_lowest = min(dx_ra_lowest, dx['ra'])
            player_dx_list.append([int(dx['song_id']), int(dx["level_index"]), int(dx['ra'])])
        for sd in player_data['charts']['sd']:
            sd_ra_lowest = min(sd_ra_lowest, sd['ra'])
            player_sd_list.append([int(sd['song_id']), int(sd["level_index"]), int(sd['ra'])])
        player_dx_id_list = [[d[0], d[1]] for d in player_dx_list]
        player_sd_id_list = [[s[0], s[1]] for s in player_sd_list]
        for music in total_list:
            for i, achievement in enumerate(achievement_list):
                for j, ds in enumerate(music.ds):
                    if match.group(1) and music['level'][j] != match.group(1): continue
                    if music.version in ['maimai でらっくす PLUS', 'maimai でらっくす Splash']:
                        music_ra = computeRa(ds, achievement)
                        if music_ra < dx_ra_lowest: continue
                        if [int(music.id), j] in player_dx_id_list:
                            player_ra = player_dx_list[player_dx_id_list.index([int(music.id), j])][2]
                            if music_ra - player_ra == int(match.group(2)) and [int(music.id), j, music_ra] not in player_dx_list:
                                music_dx_list.append([music, diffs[j], ds, achievement, rank[i], music_ra])
                        else:
                            if music_ra - dx_ra_lowest == int(match.group(2)) and [int(music.id), j, music_ra] not in player_dx_list:
                                music_dx_list.append([music, diffs[j], ds, achievement, rank[i], music_ra])
                    else:
                        music_ra = computeRa(ds, achievement)
                        if music_ra < sd_ra_lowest: continue
                        if [int(music.id), j] in player_sd_id_list:
                            player_ra = player_sd_list[player_sd_id_list.index([int(music.id), j])][2]
                            if music_ra - player_ra == int(match.group(2)) and [int(music.id), j, music_ra] not in player_sd_list:
                                music_sd_list.append([music, diffs[j], ds, achievement, rank[i], music_ra])
                        else:
                            if music_ra - sd_ra_lowest == int(match.group(2)) and [int(music.id), j, music_ra] not in player_sd_list:
                                music_sd_list.append([music, diffs[j], ds, achievement, rank[i], music_ra])
        if len(music_dx_list) == 0 and len(music_sd_list) == 0:
            await bot.finish(ev, '没有找到这样的乐曲', at_sender=True)
        elif len(music_dx_list) + len(music_sd_list) > 60:
            await bot.finish(ev, f'结果过多（{len(music_dx_list) + len(music_sd_list)} 条），请缩小查询范围。', at_sender=True)
        msg = ''
        if len(music_sd_list) != 0:
            msg += f'为您推荐以下标准乐曲：\n'
            for music, diff, ds, achievement, rank, ra in sorted(music_sd_list, key=lambda i: int(i[0]['id'])):
                msg += f'{music["id"]}. {music["title"]} {diff} {ds} {achievement} {rank} {ra}\n'
        if len(music_sd_list) != 0:
            msg += f'\n为您推荐以下2021乐曲：\n'
            for music, diff, ds, achievement, rank, ra in sorted(music_dx_list, key=lambda i: int(i[0]['id'])):
                msg += f'{music["id"]}. {music["title"]} {diff} {ds} {achievement} {rank} {ra}\n'
        await bot.send(ev, f'[CQ:image,file=base64://{image_to_base64(text_to_image(msg.strip())).decode()}]', at_sender=True)

guess_dict: Dict[Tuple[str], GuessObject] = {}
guess_time_dict: Dict[Tuple[str], float] = {}

async def guess_music_loop(bot, ev: CQEvent, state: State_T):
    cycle = state['cycle']
    if cycle != 0:
        await asyncio.sleep(8)
    else:
        await asyncio.sleep(4)
    guess: GuessObject = state['guess_object']
    if ev.group_id not in config['enable'] or guess.is_end:
        return
    if cycle < 6:
        await bot.send(ev, f'{cycle + 1}/7 这首歌{guess.guess_options[cycle]}')
    else:
        msg = f'''7/7 这首歌封面的一部分是：
[CQ:image,file=base64://{guess.b64image.decode()}]
答案将在30秒后揭晓'''
        await bot.send(ev, msg)
        await give_answer(bot, ev, state)
    state['cycle'] += 1
    await guess_music_loop(bot, ev, state)

async def give_answer(bot, ev: CQEvent, state: State_T):
    await asyncio.sleep(30)
    guess: GuessObject = state['guess_object']
    if ev.group_id not in config['enable'] or guess.is_end:
        return
    guess.is_end = True
    del guess_dict[state['gid']]
    msg = f'''答案是：
{random_music(guess.music)}'''
    await bot.finish(ev, msg)

@sv.on_fullmatch('猜歌')
async def guess_music(bot, ev: CQEvent):
    gid = ev.group_id
    if gid not in config['enable']:
        await bot.finish(ev, '该群已关闭猜歌功能，开启请输入 开启mai猜歌')
    if gid in guess_dict:
        if gid in guess_time_dict and time.time() > guess_time_dict[gid] + 120:  # 如果已经过了 120 秒则自动结束上一次
            await bot.send(ev, '检测到卡死的猜歌进程，已清除')
            del guess_dict[gid]
        else: await bot.finish(ev, '当前已有正在进行的猜歌')

    guess = GuessObject()
    guess_dict[gid] = guess
    guess_time_dict[gid] = time.time()
    state: State_T = {'gid': gid, 'guess_object': guess, 'cycle': 0}
    await bot.send(ev, '我将从热门乐曲中选择一首歌，每隔8秒描述它的特征，请输入歌曲的 id 标题 或 别称（需bot支持，无需大小写） 进行猜歌（DX乐谱和标准乐谱视为两首歌）。猜歌时查歌等其他命令依然可用。')
    await guess_music_loop(bot, ev, state)

@sv.on_message()
async def guess_music_solve(bot, ev: CQEvent):
    gid = ev.group_id
    if gid not in guess_dict:
        return
    ans = ev.message.extract_plain_text().strip().lower()
    guess = guess_dict[gid]
    an = False
    if ans in music_aliases:
        result = music_aliases[ans]
        for i in result:
            if i == guess.music.title:
                an = True
                break
    if ans == guess.music.id or ans.lower() == guess.music.title.lower() or an:
        guess.is_end = True
        del guess_dict[gid]
        msg = f'''猜对了，答案是：
{random_music(guess.music)}'''
        await bot.finish(ev, msg, at_sender=True)

config_json = os.path.join(os.path.dirname(__file__), 'config.json')
config: Dict[str, List[int]] = json.load(open(config_json, 'r', encoding='utf-8'))

def change(gid: int, set: bool):
    if set:
        if gid not in config['enable']:
            config['enable'].append(gid)
        if gid in config['disable']:
            config['disable'].remove(gid)
    else:
        if gid not in config['disable']:
            config['disable'].append(gid)
        if gid in config['enable']:
            config['enable'].remove(gid)
    try:
        with open(config_json, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=True, indent=4)
    except:
        traceback.print_exc()

@sv.on_fullmatch('开启mai猜歌')
async def guess_on(bot, ev: CQEvent):
    gid = ev.group_id
    is_ad = priv.check_priv(ev, priv.ADMIN)
    if not is_ad:
        await bot.finish(ev, '仅允许管理员开启')
    if gid in config['enable']:
        await bot.send(ev, '该群已开启猜歌功能')
    else:
        change(gid, True)
        await bot.send(ev, '已开启该群猜歌功能')

@sv.on_fullmatch('关闭mai猜歌')
async def guess_on(bot, ev: CQEvent):
    gid = ev.group_id
    is_ad = priv.check_priv(ev, priv.ADMIN)
    if not is_ad:
        await bot.finish(ev, '仅允许管理员关闭')
    if gid in config['disable']:
        await bot.send(ev, '该群已关闭猜歌功能')
    else:
        change(gid, False)
        if gid in guess_dict:
            del guess_dict[gid]
        await bot.send(ev, '已关闭该群猜歌功能')