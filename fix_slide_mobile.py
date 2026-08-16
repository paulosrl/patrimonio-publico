import os
import re

file_path = "/home/pl/projetos/patrimonio-publico/01-Introducao-IA-Patrimonio-Publico-Paulo-Lima.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's inspect current CSS and ensure:
# 1. `.agenda-grid-epic`, `.agenda-card-pro`, `.icon-box`, `svg` sizing are added.
# 2. `.foot-center` is NOT hidden on mobile, and `.foot-count` is nicely styled as a badge.
# 3. Mobile responsiveness for slide 4, font sizes, margins, stage overflow, etc.

agenda_css = """
    /* Agenda Epic & Pro Card Styles */
    .agenda-grid-epic {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 16px 20px;
      margin-top: 1.1em;
      width: 100%;
      max-width: 1720px;
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
      box-shadow: 0 4px 20px rgba(0,0,0,0.2);
      transition: transform 0.2s ease, background 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
    }
    .agenda-card-pro:hover {
      transform: translateY(-3px) translateX(3px);
      background: var(--panel2);
      border-color: hsl(var(--chue, 28) 78% 58% / 0.6);
      box-shadow: 0 10px 25px rgba(0,0,0,0.3);
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
    }
    .agenda-card-pro .icon-box svg {
      width: 28px;
      height: 28px;
      stroke: currentColor;
    }
    .agenda-card-pro .c-title {
      font-size: var(--fs-h3);
      font-weight: 700;
      color: var(--ink);
      line-height: 1.25;
      margin-bottom: 2px;
    }
    .agenda-card-pro .c-desc {
      font-size: var(--fs-small);
      color: var(--muted);
      line-height: 1.35;
    }
"""

# Check where </style> is
if "</style>" in content:
    # First inject agenda_css before </style> if not present
    if ".agenda-grid-epic" not in content:
        content = content.replace("</style>", agenda_css + "\n  </style>", 1)
        print("Injected agenda_css")

# Now let's check media queries around max-width: 820px or max-width: 768px
# Let's inspect the mobile footer rule in content
# Replace any .foot-center { display: none !important; } or similar
mobile_extra_css = """
    /* Mobile responsive enhancements */
    @media (max-width: 820px) {
      .foot-left .ft-title,
      .theme-chip {
        display: none !important;
      }
      .foot-center {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
      }
      .foot-count {
        color: var(--ink) !important;
        font-size: var(--fs-small) !important;
        font-weight: 700 !important;
        background: rgba(255, 255, 255, 0.08);
        padding: 4px 10px;
        border-radius: 8px;
        border: 1px solid var(--line);
        display: inline-block !important;
      }
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
        width: 42px !important;
        height: 42px !important;
        border-radius: 10px !important;
      }
      .agenda-card-pro .icon-box svg {
        width: 22px !important;
        height: 22px !important;
      }
      .agenda-card-pro .c-title {
        font-size: 1rem !important;
      }
      .agenda-card-pro .c-desc {
        font-size: 0.82rem !important;
      }
    }
"""

if "/* Mobile responsive enhancements */" not in content:
    content = content.replace("</style>", mobile_extra_css + "\n  </style>", 1)
    print("Injected mobile_extra_css")

# Also check if .foot-center was hidden in existing @media (max-width: 820px)
# Let's replace '.foot-center { display: none; }' or similar if present
content = re.sub(r'\.foot-center\s*\{\s*display:\s*none\s*!important;\s*\}', '/* .foot-center visible */', content)
content = re.sub(r'\.foot-center\s*\{\s*display:\s*none;\s*\}', '/* .foot-center visible */', content)

# Check touch swipe support in JS if missing
touch_js = """
  // Touch swipe support for mobile devices
  let touchStartX = 0;
  let touchStartY = 0;
  let touchEndX = 0;
  let touchEndY = 0;

  document.addEventListener('touchstart', function(e) {
    touchStartX = e.changedTouches[0].screenX;
    touchStartY = e.changedTouches[0].screenY;
  }, { passive: true });

  document.addEventListener('touchend', function(e) {
    touchEndX = e.changedTouches[0].screenX;
    touchEndY = e.changedTouches[0].screenY;
    handleSwipe();
  }, { passive: true });

  function handleSwipe() {
    const diffX = touchEndX - touchStartX;
    const diffY = touchEndY - touchStartY;
    if (Math.abs(diffX) > Math.abs(diffY) && Math.abs(diffX) > 45) {
      if (diffX < 0) {
        // Swipe left -> Next
        if (typeof nextSlide === 'function') nextSlide();
        else if (typeof next === 'function') next();
        else if (typeof goTo === 'function' && typeof current !== 'undefined') goTo(current + 1);
      } else {
        // Swipe right -> Prev
        if (typeof prevSlide === 'function') prevSlide();
        else if (typeof prev === 'function') prev();
        else if (typeof goTo === 'function' && typeof current !== 'undefined') goTo(current - 1);
      }
    }
  }
"""

if "handleSwipe" not in content:
    content = content.replace("</script>", touch_js + "\n</script>", 1)
    print("Injected touch swipe JS")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully updated 01-Introducao-IA-Patrimonio-Publico-Paulo-Lima.html")
