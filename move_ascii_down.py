import re

for filename in ['/home/shubham-singh/code/Anugrah-Singh/light_mode.svg', '/home/shubham-singh/code/Anugrah-Singh/dark_mode.svg']:
    with open(filename, 'r') as f:
        content = f.read()

    # Shift all 'y' coordinates in the ascii block down by 31px
    def offset_y(match):
        block = match.group(0)
        def add_offset(y_match):
            y_val = int(y_match.group(1))
            # 445 is the bottom-most target (450 total height - 5px margin)
            return f'y="{y_val + 31}"'
        return re.sub(r'y="(\d+)"', add_offset, block)

    content = re.sub(r'<text[^>]*class="ascii"[^>]*>.*?</text>', offset_y, content, flags=re.DOTALL)

    with open(filename, 'w') as f:
        f.write(content)
    print(f"Shifted ASCII art in {filename}")
