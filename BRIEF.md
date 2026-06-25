# eco-home-guide 站点需求简报

## 背景

这是 central-intelligence pipeline 自动生成的第一批内容站之一。
Pipeline 目录：`/Users/yechaozheng/Work/git_respository/my-sites/central-intelligence`

## 站点定位

- **主题**：可持续生活、环保家居产品、竹制品、绿色生活方式指南
- **变现方式**：Amazon 联盟佣金 + 生态/环保品牌广告
- **目标读者**：关注可持续生活的家居消费者，想买环保产品但不知道选哪款
- **内容方向**：产品选购指南、品类横向对比、竹制品专题、生活方式文章

## 已有内容

`src/content/blog/` 下已有第一篇文章：
- `best-bamboo-products-2026-kitchen-home-decor-and-daily-essentials-affiliate-buyi.md`

后续内容由 pipeline 持续生成写入这个目录。

## 可合并内容方向

这个站可以承接 pipeline 发现的以下机会（不只竹制品）：
- 竹制品（厨房、家居装饰、日用品）
- 可持续家居（堆肥、二手、节能）
- 环保日用品

## 技术要求

- **框架**：Astro 6 + Tailwind 4（与 diy-maker-station 一致）
- **内容**：Markdown，frontmatter 字段：`title, description, pubDate, category, tags, image, imageAlt, draft`
- **架构参考**：clone 自 diy-maker-station，但所有文件名、组件名、函数名、站点名称都要改成本站相关名称，不能保留 DIY Maker Station 的字样
- **搜索**：pagefind 全文搜索（同 diy-maker-station）
- **SEO**：sitemap、JSON-LD structured data、OG tags

## UI 设计要求

- **风格参考**：Apartment Therapy（温暖自然、生活感）、Good Housekeeping（可信赖、整洁）、Treehugger（环保调性、绿色）
- **配色**：自然系，建议以绿色、米白、土棕为主色，温暖而不土气，区别于科技站的冷色调
- **字体**：可考虑带点人情味的无衬线字体，标题可用衬线增加质感
- **核心 UI 组件**：
  - 产品推荐卡（含材质标注、环保认证标签、联盟购买链接）
  - 品类导航（竹制品 / 厨房 / 家居装饰 / 日用）
  - Pros/Cons 块
  - "为什么选择环保替代品" 信息块
  - 文章卡片（首页/列表页）

## diy-maker-station 架构参考

```
src/
  components/
    Header.astro
    Footer.astro
    PostCard.astro
    ProductCard.astro
    NewsletterForm.astro
    TableOfContents.astro
  content/
    blog/   ← pipeline 写入这里
  content.config.ts
  layouts/
    BaseLayout.astro
    PostLayout.astro
  pages/
    index.astro
    blog/index.astro
    blog/[slug].astro
    categories/[category].astro
    search.astro
    about.astro
    (+ privacy-policy, disclaimer, terms)
  styles/
    global.css
```

diy-maker-station 路径：`/Users/yechaozheng/Work/git_respository/my-sites/diy-maker-station`
可以读取参考，但不要直接复制文字内容。

## 启动指令

在这个目录下开新 Claude session 后，告诉 Claude：

> 请读取 BRIEF.md，基于其中的需求，用 brainstorming skill 开始设计这个站点。
