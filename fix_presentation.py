import os
import re

file_path = "/home/pl/projetos/patrimonio-publico/01-Inteligencia-Artificial-e-Engenharia-de-Contexto-na-Tutela-do-Patrimonio-Publico-Paulo-Lima.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Check if agenda-grid-epic and icon-box styles are already present
css_to_add = """
    /* Global SVG containment */
    svg {
      max-width: 100%;
      height: auto;
    }

    /* Agenda Grid Epic & Cards (Slide 4 / Topics) */
    .agenda-grid-epic {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 16px 20px;
      margin-top: 1.1em;
      width: 100%;
      box-sizing: border-box;
    }

    .agenda-card-pro {
      display: flex;
      align-items: center;
      gap: 1.1em;
      padding: 1.1em 1.3em;
      border-radius: 18px;
      background: linear-gradient(180deg, var(--panel), var(--panel2));
      border: 1px solid var(--line);
      border-left: 6px solid hsl(var(--chue, 28) 78% 58%);
      cursor: pointer;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
      transition: transform 0.2s ease, background 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
      box-sizing: border-box;
    }

    .agenda-card-pro:hover {
      transform: translateY(-3px) translateX(3px);
      background: var(--panel2);
      border-color: hsl(var(--chue, 28) 78% 58% / 0.6);
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
    }

    .agenda-card-pro .icon-box {
      flex: none;
      width: 52px;
      height: 52px;
      border-radius: 14px;
      background: hsl(var(--chue, 28) 78% 58% / 0.14);
      border: 1px solid hsl(var(--chue, 28) 78% 58% / 0.4);
      color: hsl(var(--chue, 28) 78% 62%);
      display: flex;
      align-items: center;
      justify-content: center;
      box-sizing: border-box;
    }

    .agenda-card-pro .icon-box svg {
      width: 28px;
      height: 28px;
      stroke: currentColor;
      display: block;
    }

    .agenda-card-pro div strong {
      display: block;
      font-size: var(--fs-body);
      color: var(--ink);
      margin-bottom: 2px;
    }

    .agenda-card-pro div small {
      display: block;
      font-size: var(--fs-small);
      color: var(--muted);
      line-height: 1.35;
    }
"""

# Let's inspect where in the CSS we can insert this, and also inspect mobile rules.
# Let's see the current @media (max-width: 820px) block in content.
# We'll replace or update the mobile rules to guarantee foot-count visibility and responsive 1-col layout for agenda-grid-epic.

mobile_css = """
    @media (max-width: 820px) {
      .app {
        height: 100dvh;
      }
      .topbar {
        padding: 0 10px;
        height: 48px;
      }
      .top-title {
        font-size: 0.85rem;
        max-width: 55vw;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
      .top-right {
        gap: 6px;
      }
      .stage {
        padding: 12px 10px 80px 10px;
        overflow-y: auto !important;
        -webkit-overflow-scrolling: touch;
      }
      .slide {
        min-height: auto;
        padding-bottom: 30px;
      }
      .slide-head h2 {
        font-size: 1.25rem !important;
      }
      .slide-head p {
        font-size: 0.85rem !important;
      }

      /* Slide 4 / Agenda Epic on Mobile */
      .agenda-grid-epic {
        grid-template-columns: 1fr !important;
        gap: 12px !important;
        margin-top: 0.8em !important;
      }
      .agenda-card-pro {
        padding: 0.85em 1em !important;
        gap: 0.9em !important;
      }
      .agenda-card-pro .icon-box {
        width: 44px !important;
        height: 44px !important;
        border-radius: 12px !important;
      }
      .agenda-card-pro .icon-box svg {
        width: 24px !important;
        height: 24px !important;
      }

      /* General grids responsiveness on mobile */
      .grid-2, .grid-3, .grid-4, .cols-2, .cols-3, .split {
        grid-template-columns: 1fr !important;
        gap: 12px !important;
      }

      /* Footerbar and slide counter on mobile */
      .footerbar {
        height: 52px;
        padding: 0 12px;
      }
      .foot-left .ft-title,
      .foot-left .theme-chip {
        display: none !important;
      }
      .foot-center {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
      }
      .foot-count {
        color: var(--ink) !important;
        font-size: 0.85rem !important;
        font-weight: 700 !important;
        background: rgba(255, 255, 255, 0.1) !important;
        padding: 4px 12px !important;
        border-radius: 999px !important;
        border: 1px solid var(--line) !important;
        display: inline-block !important;
      }
      .foot-right {
        gap: 6px;
      }
      .foot-right .btn-nav {
        padding: 6px 10px !important;
        font-size: 0.8rem !important;
      }
    }
"""

# Let's check how @media (max-width: 820px) currently looks or where to insert
if ".agenda-grid-epic" not in content:
    # Insert right before </style>
    style_end = content.find("</style>")
    if style_end != -1:
        content = content[:style_end] + "\n" + css_to_add + "\n" + mobile_css + "\n" + content[style_end:]
        print("CSS added successfully before </style>")
    else:
        print("Could not find </style>")
else:
    print(".agenda-grid-epic already in content, updating...")

# Also let's check goTo() to ensure stage scrolls to top on navigation
if "stage.scrollTop = 0;" not in content:
    content = content.replace("function renderSlide(", "function renderSlide() {\n      if (stage) stage.scrollTop = 0;\n")
    print("Added stage.scrollTop = 0 to renderSlide")

# Let's save the file
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("File updated successfully.")
