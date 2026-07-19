import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'zh-CN',
  title: 'Will Wang',
  description: '架构开发工程师，关注 Sandbox、Agent 系统、长期记忆与 AI 工程化。',
  cleanUrls: true,
  lastUpdated: true,
  head: [
    ['link', { rel: 'icon', href: '/profile/favicon.svg' }],
    ['meta', { name: 'theme-color', content: '#176b5b' }],
    ['meta', { property: 'og:title', content: 'Will Wang | Architecture & AI Engineering' }],
    ['meta', { property: 'og:description', content: '架构、Sandbox、Agent 系统与长期记忆实践。' }]
  ],
  themeConfig: {
    logo: '/will-avatar.png',
    siteTitle: 'Will Wang',
    nav: [
      { text: '首页', link: '/' },
      { text: 'Will Wiki', link: '/wiki/' },
      { text: 'OpenClaw', link: '/openclaw/' },
      { text: 'GitHub', link: 'https://github.com/willwang2528' }
    ],
    sidebar: {
      '/wiki/': [
        {
          text: 'Will Wiki',
          items: [{ text: '知识目录', link: '/wiki/' }]
        },
        {
          text: '工程实践',
          collapsed: false,
          items: [
            { text: 'GitHub Pages 部署 SOP', link: '/wiki/github-pages/deployment-sop' }
          ]
        },
        {
          text: '架构研究',
          collapsed: false,
          items: [
            { text: 'Sandbox 技术', link: '/wiki/architecture/sandbox' },
            { text: 'Agent 系统', link: '/wiki/architecture/agent-systems' }
          ]
        },
        {
          text: 'AI 工程化',
          collapsed: false,
          items: [
            { text: '长期记忆', link: '/wiki/ai-engineering/long-term-memory' }
          ]
        }
      ],
      '/openclaw/': [
        {
          text: 'OpenClaw 记录',
          items: [
            { text: '当前配置', link: '/openclaw/' },
            { text: '公开边界', link: '/openclaw/privacy' }
          ]
        }
      ]
    },
    outline: {
      level: [2, 3],
      label: '本页目录'
    },
    docFooter: {
      prev: '上一篇',
      next: '下一篇'
    },
    lastUpdated: {
      text: '最后更新于',
      formatOptions: {
        dateStyle: 'medium',
        timeStyle: 'short'
      }
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/willwang2528' }
    ],
    search: { provider: 'local' },
    footer: {
      message: '知识来自持续实践，内容保持可验证与可追溯。',
      copyright: 'Copyright © 2026 Will Wang'
    }
  }
})
