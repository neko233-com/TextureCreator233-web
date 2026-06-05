# TextureCreator233 Web (中文汉化版)

本项目是 `TextureCreate` 的本地静态版，已完成中文汉化，可直接双击 `启动.cmd` 使用。

## 本地使用

1. 双击 `启动.cmd`
2. 脚本会优先用 Edge/Chrome 打开 `index.html`

无需 Python、无需 Node、无需后端。

## Cloudflare Pages 部署（推荐）

1. 将本仓库推送到 GitHub
2. 打开 Cloudflare Dashboard -> `Workers & Pages` -> `Create` -> `Pages`
3. 连接 GitHub 并选择本仓库
4. 构建设置：
   - Framework preset: `None`
   - Build command: 留空
   - Build output directory: `/`（根目录）
5. 点击部署

## GitHub Pages 部署

已提供 `.github/workflows/pages.yml`，推送到 `main` 后会自动发布。

发布地址示例：
- `https://<your-username>.github.io/<repo-name>/`
