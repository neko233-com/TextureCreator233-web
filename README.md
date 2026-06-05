# TextureCreator233 Web (中文汉化版)

本项目是 `TextureCreate` 的本地静态版，已完成中文汉化，可直接双击 `启动.cmd` 使用。

## 本地使用

1. 双击 `启动.cmd`
2. 脚本会优先用 Edge/Chrome 打开 `index.html`

无需 Python、无需 Node、无需后端。

## Cloudflare Pages 部署

1. 将本仓库推送到 GitHub
2. 打开 Cloudflare Dashboard -> `Workers & Pages` -> `Create` -> `Pages`
3. 连接 GitHub 并选择本仓库
4. 构建设置：
   - Framework preset: `None`
   - Build command: 留空
   - Build output directory: `/`（根目录）
5. 点击部署
6. 在 `Custom domains` 添加 `texture.neko233.store`

发布后访问：`https://texture.neko233.store`
