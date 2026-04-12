# -*- coding: utf-8 -*-
import re

path = r"M:\cat分身\代理\knowledge-base\thinking\index.html"

with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# 添加 cat-link 样式（在 cat-badge 样式后面）
css_insert = """.cat-link {
  font-size:12px; color:var(--accent2); text-decoration:none;
  padding:5px 14px; border-radius:20px;
  border:1px solid rgba(124,106,247,0.3);
  background:rgba(124,106,247,0.08);
  transition:all 0.2s; white-space:nowrap; margin-left:10px;
}
.cat-link:hover { background:rgba(124,106,247,0.18); border-color:var(--accent2); }"""

html = html.replace(
    "footer { border-top:1px solid var(--border); padding:30px; text-align:center; color:var(--text3); font-size:12px; }",
    css_insert + "\n\nfooter { border-top:1px solid var(--border); padding:30px; text-align:center; color:var(--text3); font-size:12px; }"
)

# 替换每个分类的 cat-badge 为 cat-link
replacements = [
    # (旧badge文本, 新链接文件, 分类名)
    ('<!-- ① 学习管理 -->', 'cat-01.html'),
    ('<!-- ② 认知管理 -->', 'cat-02.html'),
    ('<!-- ③ 情绪管理 -->', 'cat-03.html'),
    ('<!-- ④ 习惯管理 -->', 'cat-04.html'),
    ('<!-- ⑤ 目标管理 -->', 'cat-05.html'),
    ('<!-- ⑥ 复盘管理 -->', 'cat-06.html'),
    ('<!-- ⑦ 沟通管理 -->', 'cat-07.html'),
    ('<!-- ⑧ 人际管理 -->', 'cat-08.html'),
    ('<!-- ⑨ 财富管理 -->', 'cat-09.html'),
    ('<!-- ⑩ 商业管理 -->', 'cat-10.html'),
]

# 用正则把每个 cat-section 里的 <div class="cat-badge">10 个</div> 替换为链接
# 策略：找到每个 cat-section 块，替换其中的 cat-badge
def replace_badge(html, comment, link_file):
    # 找到注释后的第一个 cat-badge，替换为 cat-link
    pattern = re.compile(
        r'(' + re.escape(comment) + r'.*?<div class="cat-badge">10 个</div>)',
        re.DOTALL
    )
    replacement_link = f'<a href="{link_file}" class="cat-link">查看详情 →</a>'
    def replacer(m):
        return m.group(1).replace('<div class="cat-badge">10 个</div>', replacement_link)
    return pattern.sub(replacer, html)

for comment, link_file in replacements:
    html = replace_badge(html, comment, link_file)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("index.html 更新完成！")
