// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

import { themes } from "prism-react-renderer";
const lightCodeTheme = themes.github;
const darkCodeTheme = themes.dracula;

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "LLMStack",
  tagline: "AI Agents in Minutes | No-code AI App Builder",
  favicon: "img/llmstack-icon.png",

  // Set the production url of your site here
  url: "https://llmstack.ai",
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: "/",

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: "trypromptly", // Usually your GitHub org/user name.
  projectName: "LLMStack", // Usually your repo name.

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        sitemap: {
          changefreq: "weekly",
          priority: 0.5,
          ignorePatterns: ["/tags/**"],
          filename: "sitemap.xml",
        },
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
        },
        blog: {
          showReadingTime: true,
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
        gtag: {
          trackingID: "G-55DZJ46RPF",
        },
      }),
    ],
  ],

  themes: [
    [
      require.resolve("@easyops-cn/docusaurus-search-local"),
      {
        hashed: true,
        docsRouteBasePath: "/docs",
        blogRouteBasePath: "/blog",
      },
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      image:
        "https://storage.googleapis.com/trypromptly-static/static/images/opengraph.jpg",
      navbar: {
        title: "",
        logo: {
          alt: "LLMStack",
          src: "img/logo.svg",
          srcDark: "img/logo-grayscale.svg",
        },
        items: [
          {
            href: "https://docs.trypromptly.com/llmstack/introduction",
            position: "left",
            label: "Docs",
          },
          {
            href: "https://trypromptly.com",
            position: "left",
            label: "Promptly",
          },
          {
            label: "Blog",
            to: "/blog",
          },
          {
            href: "https://github.com/trypromptly/LLMStack",
            label: "GitHub",
            position: "right",
          },
        ],
      },
      footer: {
        style: "dark",
        links: [
          {
            title: "Docs",
            items: [
              {
                label: "LLMStack UI",
                href: "https://docs.trypromptly.com/getting-started/ui",
              },
              {
                label: "Processors",
                href: "https://docs.trypromptly.com/processors/introduction",
              },
              {
                label: "Apps",
                href: "https://docs.trypromptly.com/apps/introduction",
              },
              {
                label: "Datasources",
                href: "https://docs.trypromptly.com/datasources/introduction",
              },
            ],
          },
          {
            title: "Community",
            items: [
              {
                label: "Discord",
                href: "https://discord.gg/3JsEzSXspJ",
              },
              {
                label: "LinkedIn",
                href: "https://linkedin.com/company/trypromptly",
              },
              {
                label: "Twitter",
                href: "https://twitter.com/trypromptly",
              },
            ],
          },
          {
            title: "More",
            items: [
              {
                label: "Blog",
                to: "/blog",
              },
              {
                label: "GitHub",
                href: "https://github.com/trypromptly/llmstack",
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} MakerDojo, Inc.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
        additionalLanguages: ["javascript", "python"],
      },
      colorMode: {
        defaultMode: "dark",
        disableSwitch: false,
        respectPrefersColorScheme: true,
      },
      scripts: [
        {
          src: "https://buttons.github.io/buttons.js",
          async: true,
          defer: true,
        },
      ],
    }),
};

export default config;
