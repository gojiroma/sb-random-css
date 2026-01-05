from flask import Flask, Response
import random

app = Flask(__name__)

PASTEL_COLORS = [
    "#FFD1DC", "#FFB3BA", "#FF9AA2", "#FF8598", "#FF768E",
    "#FFDAC1", "#FFC3A0", "#FFAB91", "#FF9980", "#FF8A65",
    "#E2F0CB", "#C8E6C9", "#A5D6A7", "#81C784", "#66BB6A",
    "#B3E5FC", "#81D4FA", "#4FC3F7", "#29B6F6", "#03A9F4",
    "#E1BEE7", "#CE93D8", "#BA68C8", "#AB47BC", "#9C27B0",
    "#F0F4C3", "#E6EE9C", "#DCE775", "#D4E157", "#CDDC39",
]

FONTS = [
    "'Kaisei HarunoUmi', serif",
    "'Noto Sans JP', sans-serif",
    "'M PLUS Rounded 1c', sans-serif",
    "'Sawarabi Mincho', sans-serif",
    "'Hannari', sans-serif",
]

def generate_random_css():
    bg_color = random.choice(PASTEL_COLORS)
    text_color = random.choice(PASTEL_COLORS)
    border_color = random.choice(PASTEL_COLORS)
    font_family = random.choice(FONTS)
    font_size = random.randint(8, 14)
    line_height = random.randint(15, 25)
    border_radius = random.randint(3, 10)
    opacity = round(random.uniform(0.1, 0.9), 1)

    css = f"""@import url("https://fonts.googleapis.com/css2?family=Kaisei+HarunoUmi&family=Hannari&family=M+PLUS+Rounded+1c&family=Noto+Sans+JP&family=Sawarabi+Mincho&display=swap");
body {{
    font-family: {font_family};
    background: #{bg_color[1:]};
}}
.page {{
    background: #{adjust_color(bg_color, -10)[1:]}
}}
.search-form .form-group input {{
    background: #{adjust_color(bg_color, 20)[1:]}26;
    color: #{text_color[1:]};
}}
.search-form .form-group input:focus, .search-form .form-group input.for-mobile {{
    color: #{text_color[1:]};
    background-color: #00000040;
}}
.dropdown-menu {{
    color: #{text_color[1:]};
    background: #{adjust_color(bg_color, -50)[1:]}d4;
}}
.dropdown-menu>li>a {{
    color: #{text_color[1:]};
}}
.dropdown-menu>li>a:active, [data-hover-visible] .dropdown-menu>li>a:hover, [data-focus-visible] .dropdown-menu>li>a:focus {{
    background-color: #{adjust_color(text_color, -30)[1:]}bd;
}}
.line.line-title .text,
.grid li.page-list-item a .title,
span.title {{
    color: #{text_color[1:]};
}}
.grid li.page-list-item a .description {{
    writing-mode: vertical-rl;
    font-size: {font_size}px;
    line-height: {line_height}px;
}}
.grid li.page-list-item a {{
    border: #{adjust_color(border_color, 20)[1:]} solid 0.5px;
    border-radius: {border_radius}px;
}}
.quick-launch .flex-box, div.toolbar {{
    opacity: {opacity};
}}
.dropdown.user-menu-dropdown > a > img {{
    opacity: {opacity};
    animation: fa-spin 0.8s infinite linear;
}}
"""
    return css

def adjust_color(color, amount):
    color = color.lstrip('#')
    rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
    new_rgb = tuple(max(0, min(255, c + amount)) for c in rgb)
    return '#{:02x}{:02x}{:02x}'.format(*new_rgb)

@app.route('/api/style.css')
def style():
    css = generate_random_css()
    return Response(css, mimetype='text/css')

