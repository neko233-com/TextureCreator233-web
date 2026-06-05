# TextureCreator233

TextureCreator233 是一个纯前端、实时渲染的程序化纹理创作网站。

它面向游戏特效、材质贴图、UI 动效和技术美术快速迭代场景，主打“可视化参数 + 多图层合成 + 一键导出”。

## 这个网站是做什么的

- 在线生成程序化纹理（无需安装客户端）
- 用多图层工作流叠加出复杂效果
- 对纹理做后期处理与渐变重映射
- 导出可直接用于项目的贴图文件（PNG、GIF、法线贴图）

## 核心能力总览

### 1. 程序化纹理引擎

- 内置 117 种程序纹理类型
- 每种类型都有独立参数面板
- 支持实时预览与参数联动

### 2. 图层系统

- 图层新增、删除
- 图层上下移动（调整叠加顺序）
- 图层显示/隐藏
- 图层重命名（支持双击快速改名）
- 图层混合模式：Normal、Add、Multiply、Screen、Mask
- 图层不透明度控制
- 图层纯色覆盖（Solid Color）

### 3. 变换与基础控制

- 极坐标变换（Polar Conversion）
- 色调反转（Invert Tone）
- 平移（Offset X/Y）
- 缩放（Scale X/Y）
- 旋转（Rotation）
- 滚动（Scroll X/Y）
- 一键重置变换参数
- 一键重置当前类型参数

### 4. 全局设置与动画

- 分辨率：64、128、256、512、1024、2048
- 时间轴参数（Time）
- 动画开关（Animate）
- 动画速度（Speed）
- GIF 导出帧率（GIF FPS）
- GIF 导出时长（GIF Duration）
- GIF 无缝循环模式（Seamless Loop）

### 5. 后期效果系统

- Blur（模糊）
- Bloom（泛光）
- Sharpen（锐化）
- Pixelation（像素化）
- Chromatic Aberration（色差）
- Vignette（晕影）
- Scanline（扫描线）
- Kaleidoscope（万花筒）
- Mirror Tile（镜像平铺）
- Swirl（漩涡）
- Edge Detection（边缘检测）
- Toon Shading（卡通分级）
- Color Correction（三色校正：Shadow/Midtone/Highlight）
- Radial Mask（径向遮罩）

### 6. 渐变映射编辑器（Gradient Ramp）

- 启用/关闭渐变映射
- 点击色带添加 Stop
- 拖拽 Stop 调整位置
- 选中并修改 Stop 颜色
- 删除 Stop
- 重置到默认黑白渐变
- 内置预设：B/W、Fire、Water、Plasma、Lava、Ice、Nature、Neon、Desert

### 7. 导出能力

- 保存 PNG
- 保存 GIF（显示导出进度）
- 保存法线贴图（Normal Map）

### 8. 预览与界面交互

- 中央画布实时渲染
- 支持黑色背景与棋盘背景切换
- 类型缩略图面板（可折叠）
- 缩略图搜索
- 纹理类型总览弹窗
- 中英双语切换

## 技术特性

- 前端本地渲染：WebGL2 + Canvas
- 无后端依赖
- 无数据库依赖
- 无构建步骤（静态站点即可运行）

## 本地运行

方式 A（推荐，Windows）：

1. 双击 启动.cmd
2. 自动使用可用浏览器打开 index.html

方式 B（跨平台）：

1. 直接用浏览器打开 index.html

## 生产部署（Cloudflare Pages）

1. 将仓库推送到 GitHub
2. 进入 Cloudflare Dashboard
3. 打开 Workers & Pages，创建 Pages 项目并选择 Connect to Git
4. 安装并授权 Cloudflare GitHub 应用（Cloudflare for GitHub）到本仓库
5. 选择仓库后由 Cloudflare 自动拉取源码并创建部署
6. 构建配置：
   - Framework preset: None
   - Build command: 留空
   - Build output directory: /
7. 完成部署后绑定自定义域名

说明：

- 本项目使用 Cloudflare GitHub 应用的集成部署方式。
- 不需要 GitHub Actions workflow。
- 之后每次推送到生产分支，Cloudflare 会自动触发新部署。

## 浏览器要求

- 需要支持 WebGL2 的现代浏览器
- 推荐最新版 Chrome 或 Edge

## 项目结构

- index.html：页面结构与界面增强脚本
- assets/index-CE9_u47Z.js：核心渲染与交互逻辑
- assets/index-qS6aG5iE.css：样式文件
- gif.js：GIF 导出依赖
- 启动.cmd：Windows 快速启动脚本
- thumbnails：类型缩略图资源

## 完整纹理类型清单（117）

| 序号 | Type |
| ---: | ---- |
| 1 | Circle |
| 2 | Vignette |
| 3 | LensFlare |
| 4 | Sun |
| 5 | SolarGlow |
| 6 | Ring |
| 7 | Crescent |
| 8 | Flash |
| 9 | EnergyRing |
| 10 | AuraRing |
| 11 | Halo |
| 12 | Ripple |
| 13 | Concentric |
| 14 | Pulse |
| 15 | MetaBalls |
| 16 | WaveRingSine |
| 17 | WaveRingNoisy |
| 18 | WaveRingSquare |
| 19 | WaveRingDouble |
| 20 | Star |
| 21 | Polygon |
| 22 | HexGridRadial |
| 23 | Rectangle |
| 24 | Checker |
| 25 | GradientChecker |
| 26 | RoundChecker |
| 27 | DiamondChecker |
| 28 | Spark |
| 29 | Flare |
| 30 | Cross |
| 31 | Glare |
| 32 | StarFlare |
| 33 | RayBurst |
| 34 | Burst |
| 35 | ImpactLines |
| 36 | RadialLines |
| 37 | SpiralV2 |
| 38 | Swirl |
| 39 | GodRay |
| 40 | StarBurst |
| 41 | Flower |
| 42 | Spiral |
| 43 | Energy |
| 44 | Crack |
| 45 | Bokeh |
| 46 | Shimmer |
| 47 | VoronoiFluid |
| 48 | Speckle |
| 49 | CrossGrid |
| 50 | SquareGrid |
| 51 | PyramidPattern |
| 52 | RandomTiles |
| 53 | SquareGridDash |
| 54 | Dots |
| 55 | SquareGridPolka |
| 56 | DotMatrix |
| 57 | Zigzag |
| 58 | Crosshatch |
| 59 | TriGrid |
| 60 | Bricks |
| 61 | Scanline |
| 62 | FlowLines |
| 63 | Fabric |
| 64 | PolarDots |
| 65 | Weave |
| 66 | Halftone |
| 67 | SweepGradient |
| 68 | GradationLinear |
| 69 | GradationReflect |
| 70 | GradationRepeat |
| 71 | BevelSquare |
| 72 | Grain |
| 73 | PerlinNoise |
| 74 | FbmNoise |
| 75 | DistortionWave |
| 76 | StripeNoise |
| 77 | ToxicCloud |
| 78 | GeoRelief |
| 79 | Smoke |
| 80 | WaterTurbulence |
| 81 | Electric |
| 82 | SimplexNoise |
| 83 | Lava |
| 84 | Wrinkle |
| 85 | Crystal |
| 86 | AbsNoise |
| 87 | FractalCamo |
| 88 | PlasmaV2 |
| 89 | Squiggles |
| 90 | Grunge |
| 91 | GrungeV2 |
| 92 | CellularEdge |
| 93 | Twirl |
| 94 | CosmicPortal |
| 95 | Wormhole |
| 96 | Plasma |
| 97 | MarbleNoise |
| 98 | Fire |
| 99 | Cloud |
| 100 | Caustics |
| 101 | Aurora |
| 102 | Flame |
| 103 | PixelNoise |
| 104 | AnalogGlitch |
| 105 | CyberBlock |
| 106 | Mosaic |
| 107 | LaserBeam |
| 108 | GlitchBlock |
| 109 | VoronoiCell |
| 110 | Matrix |
| 111 | Wood |
| 112 | SparkBurst |
| 113 | VoronoiNoise |
| 114 | Cell |
| 115 | Lightning |
| 116 | Kaleido |
| 117 | SymmetricNoise |