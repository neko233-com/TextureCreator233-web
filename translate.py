# -*- coding: utf-8 -*-
"""Translate Japanese strings in the TextureCreate JS bundle to Chinese."""

import re
import os
from pathlib import Path

# Translation dictionary for parameter labels (ja:"..." pattern)
PARAM_TRANSLATIONS = {
    "半径": "半径",
    "背景の柄サイズ": "背景图案大小",
    "変化の速度": "变化速度",
    "標高・強度": "海拔/强度",
    "柄のサイズ": "图案大小",
    "波打ち": "波动",
    "波及頻度": "波及频率",
    "波形数": "波形数",
    "波の密度": "波密度",
    "波の強さ": "波强度",
    "波の数": "波数量",
    "波の振幅": "波振幅",
    "粗さ": "粗糙度",
    "大きさ": "大小",
    "帯の幅": "带宽",
    "帯の数": "带数",
    "点滅速度": "闪烁速度",
    "点滅スピード": "闪烁速度",
    "頂点数": "顶点数",
    "対称軸の数": "对称轴数",
    "発光": "发光",
    "発光力": "发光强度",
    "範囲": "范围",
    "分布範囲": "分布范围",
    "分割数": "分割数",
    "分割数 X": "分割数 X",
    "分割数 Y": "分割数 Y",
    "幅": "宽度",
    "複雑度": "复杂度",
    "複雑さ": "复杂度",
    "高さ": "高度",
    "個数": "数量",
    "光線本数": "光线数量",
    "光線数": "光线数",
    "光源角度": "光源角度",
    "光の筋の数": "光束数量",
    "光の筋の太さ": "光束粗细",
    "光の筋の長さ": "光束长度",
    "広がり": "扩散",
    "横糸の密度": "横纬密度",
    "横スケール": "横向缩放",
    "横ブロック数": "横向块数",
    "後光の強さ": "光晕强度",
    "花びらの数": "花瓣数",
    "滑らかさ": "平滑度",
    "環境光": "环境光",
    "輝度": "亮度",
    "回転角度": "旋转角度",
    "回転数": "旋转次数",
    "回転速度": "旋转速度",
    "火花の数": "火花数量",
    "火花の太さ": "火花粗细",
    "火花の長さ": "火花长度",
    "減衰": "衰减",
    "減衰力": "衰减强度",
    "減衰効果": "衰减效果",
    "角度": "角度",
    "角度 1": "角度 1",
    "角度 2 (クロス)": "角度 2 (交叉)",
    "角度オフセット": "角度偏移",
    "角数": "角数",
    "角の丸み": "圆角",
    "階調数": "阶调数",
    "解像度": "分辨率",
    "筋の太さ": "线条粗细",
    "筋の長さ": "线条长度",
    "巻きの強さ": "卷曲强度",
    "拡散": "扩散",
    "立体感": "立体感",
    "粒半径": "粒子半径",
    "列数": "列数",
    "流れる速度": "流动速度",
    "密度": "密度",
    "密度 / スケール": "密度 / 缩放",
    "明るさ": "亮度",
    "目地の太さ": "砖缝宽度",
    "内半径": "内半径",
    "内側の丸み": "内侧圆角",
    "内円の半径": "内圆半径",
    "欠ける角度": "缺角角度",
    "強度": "强度",
    "強さ": "强度",
    "曲がり具合": "弯曲程度",
    "燃え上がり": "燃烧",
    "融合しきい値": "融合阈值",
    "锐さ": "锐度",
    "鋭さ": "锐度",
    "色褱": "色衰减",
    "色相シフト": "色相偏移",
    "傷の量": "划痕数量",
    "深さ": "深度",
    "速度": "速度",
    "太さ": "粗细",
    "太さのばらつき": "粗细变化",
    "条数": "条数",
    "同時リング数": "同时环数",
    "透明度": "透明度",
    "歪み": "扭曲",
    "歪みの強さ": "扭曲强度",
    "歪みの細かさ": "扭曲细度",
    "外半径": "外半径",
    "外側の丸み": "外侧圆角",
    "丸み": "圆度",
    "丸み (Vignette)": "圆度 (晕影)",
    "微細さ": "细腻度",
    "渦の強さ": "漩涡强度",
    "吸い込み速度": "吸入速度",
    "細部": "细节",
    "細部ディテール": "细节细腻度",
    "線の密度": "线条密度",
    "線の数": "线条数量",
    "線の太さ": "线条粗细",
    "線の太さ / 枠幅": "线条粗细 / 边框宽度",
    "線の細さ": "线条细度",
    "行数": "行数",
    "炎の大きさ": "火焰大小",
    "炎のサイズ": "火焰尺寸",
    "揺らぎ速度": "摇曳速度",
    "影響半径": "影响半径",
    "湧き上げ速度": "涌起速度",
    "円の密度": "圆形密度",
    "雲の幅": "云宽度",
    "雲の高さ": "云高度",
    "長さのばらつき": "长度变化",
    "振幅": "振幅",
    "振幅 (ジグザグ)": "振幅 (锯齿)",
    "中心座標 X": "中心坐标 X",
    "中心座標 Y": "中心坐标 Y",
    "中心の強さ": "中心强度",
    "中心の穴サイズ": "中心孔大小",
    "中心の余白": "中心留白",
    "重なり": "重叠",
    "縦列の密度": "纵列密度",
    "縦糸の密度": "纵经密度",
    "縦スケール": "纵向缩放",
    "縦ブロック数": "纵向块数",
    "走査線数": "扫描线数",
    "Y位置": "Y位置",
    "アーム数": "臂数",
    "アウトライン幅": "描边宽度",
    "うねり度": "起伏度",
    "エッジの強調": "边缘强调",
    "オクターブ(細部)": "倍频(细节)",
    "オフセット": "偏移",
    "オフセット / 捻り": "偏移 / 扭曲",
    "グリッド分割": "网格分割",
    "グロー": "辉光",
    "グロー範囲": "辉光范围",
    "グロー強度": "辉光强度",
    "ゲイン": "增益",
    "コアグロー": "核心辉光",
    "コントラスト": "对比度",
    "サイズ": "尺寸",
    "しきい値": "阈值",
    "シード": "种子",
    "シミの量": "污点数量",
    "シャープネス": "锐化",
    "ずれ": "偏移",
    "ズーム": "缩放",
    "スケール": "缩放",
    "スケール / リング数": "缩放 / 环数",
    "スケール(反復)": "缩放(重复)",
    "スケールX / 列数": "缩放X / 列数",
    "スケールY / 行数": "缩放Y / 行数",
    "スパイク数": "尖刺数",
    "スピード": "速度",
    "ゼワさ": "柔和度",
    "ディテール": "细节",
    "ドット半径": "圆点半径",
    "ドット密度": "圆点密度",
    "ドットの大きさ": "圆点大小",
    "なめらかさ": "平滑度",
    "ねじれ": "扭曲",
    "ノイズ": "噪声",
    "ノイズ幅": "噪声宽度",
    "ノイズ周波数": "噪声频率",
    "ノイズスケール": "噪声缩放",
    "ハロの広がり": "光晕扩散",
    "ひねり": "扭转",
    "ひねりの強さ": "扭转强度",
    "ビーム本数": "光束数量",
    "ブレンド率": "混合比例",
    "ブロック出現率": "方块出现率",
    "ブロック密度": "方块密度",
    "ベベル深さ": "倒角深度",
    "ぼかし": "模糊",
    "ボール半径": "球半径",
    "もやの濃さ": "雾浓度",
    "ライン数": "线条数",
    "ランダム・ノイズ": "随机噪声",
    "ランダム性": "随机性",
    "リング半径": "环半径",
    "リング幅": "环宽度",
    "リング数": "环数",
    "リングの太さ": "环厚度",
}

# Full Chinese translation for the i18n table (le.ja in the JS)
# Format: each entry is "key":"chinese_translation"
ZH_TRANSLATION_TABLE = {
    "Type & Parameters": "类型与参数",
    "Type": "类型 (Type)",
    "Resolution": "分辨率",
    "Time": "时间 (Time)",
    "Animate": "启用动画",
    "Polar Conversion": "极坐标变换",
    "Invert": "色调反转",
    "Params": "参数",
    "Reset Params": "重置参数",
    "Toon": "卡通/阶调化",
    "Toon Shading": "阶调化 (Toon)",
    "Dark Steps": "暗部级数",
    "Light Steps": "亮部级数",
    "Tiling": "平铺预处理",
    "Radial Mask": "晕影遮罩",
    "GradationLine": "渐变线",
    "SweepGradient": "扫描渐变",
    "Mosaic": "马赛克",
    "Black Bg": "黑色背景",
    "Animation": "动画",
    "Post Effects": "后期效果",
    "Blur": "模糊",
    "Sharpen": "锐化",
    "Pixelation": "像素化",
    "Chromatic Aberration": "色差 (RGB偏移)",
    "Vignette": "晕影 (Vignette)",
    "Scanline": "扫描线",
    "Kaleidoscope": "万花筒",
    "Mirror Tile": "镜像平铺",
    "Swirl": "漩涡",
    "Edge Detection": "边缘检测",
    "Strength": "强度",
    "Size": "尺寸",
    "Density": "密度",
    "Speed": "速度",
    "Segments": "分段数",
    "Rotation": "旋转",
    "Mirror X": "X轴镜像",
    "Mirror Y": "Y轴镜像",
    "Radius": "半径",
    "Thickness": "厚度",
    "Color": "颜色",
    "Color Balance": "色彩平衡",
    "Color Correction": "三色渐变",
    "Shadow": "阴影 (暗部)",
    "Midtone": "中间调",
    "Highlight": "高光 (亮部)",
    "Save PNG": "保存 PNG",
    "Save NormalMap": "保存法线贴图",
    "Hide Types": "隐藏类型列表",
    "Show Types": "显示类型列表",
    "Save ChannelPack": "保存通道包",
    "All Types": "纹理类型一览",
    "Gradient Ramp": "渐变映射",
    "Enable": "启用",
    "LANG_BTN": "🌐 EN",
    "Terms of Use": "使用条款",
    "Save GIF": "保存 GIF",
    "Encoding GIF...": "GIF 保存中...",
    "Seamless Loop": "无缝循环 (β)",
    "EnergyRing": "能量环",
    "SparkBurst": "火花迸发",
    "Wormhole": "虫洞",
    "StarFlare": "星光耀斑",
    "ImpactLines": "集中线",
    "AuraRing": "光环",
    "Crescent": "月牙",
    "Glare": "强光",
    "LaserBeam": "激光束",
    "GlitchBlock": "故障方块",
    "AnalogGlitch": "模拟故障 (VHS)",
    "CosmicPortal": "宇宙之门 (星际漩涡)",
    "CyberBlock": "赛博方块",
    "ToxicCloud": "毒云",
    "GeoRelief": "地形浮雕",
    "Layer Settings": "图层设置",
    "Layer List": "图层列表",
    "Add Layer": "+ 添加图层",
    "Remove Layer": "删除",
    "Move Up": "上移 (↑)",
    "Move Down": "下移 (↓)",
    "Blend Mode": "混合模式",
    "Opacity": "不透明度",
    "Normal": "正常 (Normal)",
    "Add": "相加 (Add)",
    "Multiply": "正片叠底 (Multiply)",
    "Screen": "滤色 (Screen)",
    "Mask": "遮罩 (Mask)",
    "Solid Color": "纯色 (Solid Color)",
}

# Hardcoded Japanese UI strings to translate
HARDCODED_TRANSLATIONS = {
    "WebGL2 が利用できません。ブラウザを確認してください。": "无法使用 WebGL2，请检查您的浏览器。",
    "ロードに失敗しました: ": "加载失败: ",
    "GIF 保存中... ": "GIF 保存中... ",
    "＋ レイヤー追加": "+ 添加图层",
    "クリックで追加 / 選択して削除": "点击添加 / 选中后删除",
    "🌐 日本語": "🌐 中文",
    "gif.js が読み込まれていません。": "gif.js 未加载。",
    "選択中のストップを削除": "删除选中的色标",
}

# Translation for the en mode LANG_BTN (was "🌐 日本語" meaning "click to go Japanese")
# Now should say "🌐 中文" (click to go Chinese, since ja slot now holds Chinese)
EN_TABLE_OVERRIDES = {
    "LANG_BTN": "🌐 中文",
}


def build_ja_table_string():
    """Build the Japanese (now Chinese) translation table string for replacement."""
    parts = []
    for key, value in ZH_TRANSLATION_TABLE.items():
        # Match the JS object key syntax - keys with special chars are quoted
        if re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', key):
            key_str = key
        else:
            key_str = f'"{key}"'
        parts.append(f'{key_str}:"{value}"')
    return "{" + ",".join(parts) + "}"


def main():
    js_path = Path("assets/index-CE9_u47Z.js")
    content = js_path.read_bytes().decode("utf-8")
    original_len = len(content)

    print(f"Original file size: {original_len} bytes")

    # Step 1: Replace all `ja:"<japanese>"` patterns with Chinese
    # Sort by length descending so longer strings are matched first
    sorted_params = sorted(PARAM_TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True)
    replaced_params = 0
    for ja_text, zh_text in sorted_params:
        old = f'ja:"{ja_text}"'
        new = f'ja:"{zh_text}"'
        if old in content:
            count = content.count(old)
            content = content.replace(old, new)
            replaced_params += count
    print(f"Replaced {replaced_params} ja:label patterns")

    # Step 2: Replace the i18n `le.ja` translation table content
    # Find pattern: le={ja:{...},en:{...}}
    # The ja table runs from "ja:{" to the matching "}" before ",en:"
    ja_start = content.find("ja:{")
    if ja_start < 0:
        print("ERROR: Could not find ja: table")
        return

    # Find the matching close brace
    depth = 0
    i = ja_start + 3  # position of '{'
    end_pos = -1
    while i < len(content):
        c = content[i]
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                end_pos = i + 1
                break
        elif c == '"':
            # skip string
            i += 1
            while i < len(content) and content[i] != '"':
                if content[i] == '\\':
                    i += 1
                i += 1
        i += 1

    if end_pos < 0:
        print("ERROR: Could not find ja: table end")
        return

    new_ja_table = "ja:" + build_ja_table_string()
    print(f"Replacing ja table: {ja_start} -> {end_pos} ({end_pos - ja_start} chars)")
    content = content[:ja_start] + new_ja_table + content[end_pos:]

    # Step 3: Modify the en table's LANG_BTN to point to "中文"
    # The pattern is: en:{...,LANG_BTN:"🌐 日本語",...}
    # We need to replace just the LANG_BTN value in the en table
    en_pattern = r'(en:\{[^}]*?LANG_BTN:")🌐 日本語(")'
    content_new = re.sub(en_pattern, r'\g<1>🌐 中文\g<2>', content)
    if content_new != content:
        print("Updated en table LANG_BTN")
        content = content_new

    # Step 4: Replace hardcoded Japanese strings
    replaced_hardcoded = 0
    sorted_hardcoded = sorted(HARDCODED_TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True)
    for ja_text, zh_text in sorted_hardcoded:
        if ja_text in content:
            count = content.count(ja_text)
            content = content.replace(ja_text, zh_text)
            replaced_hardcoded += count
            print(f"  Replaced '{ja_text[:30]}...': {count} times")
    print(f"Replaced {replaced_hardcoded} hardcoded strings")

    # Step 5: Change the localStorage default language reference if needed
    # The current code: U=localStorage.getItem("tc_lang")||"ja"
    # This is fine - "ja" now means Chinese
    # But let's also update the storage key check so old "ja" loads still work

    # Step 6: Write the modified content
    js_path.write_bytes(content.encode("utf-8"))
    new_len = len(content)
    print(f"New file size: {new_len} bytes (delta: {new_len - original_len:+d})")


if __name__ == "__main__":
    main()
