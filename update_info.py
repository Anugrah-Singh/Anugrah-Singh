import re

new_text_block = """<tspan x="390" y="30">Anugrah-Singh</tspan> -———————————————————————————————————————————-—-
<tspan x="390" y="50" class="cc">. </tspan><tspan class="key">OS</tspan>:<tspan class="cc"> ........................ </tspan><tspan class="value">Linux</tspan>
<tspan x="390" y="70" class="cc">. </tspan><tspan class="key">Uptime</tspan>:<tspan class="cc" id="age_data_dots"> .................... </tspan><tspan class="value" id="age_data">20 years</tspan>
<tspan x="390" y="90" class="cc">. </tspan><tspan class="key">IDE</tspan>:<tspan class="cc"> ....................... </tspan><tspan class="value">VSCode</tspan>
<tspan x="390" y="110" class="cc">. </tspan>
<tspan x="390" y="130" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Programming</tspan>:<tspan class="cc"> ..... </tspan><tspan class="value">Javascript, Typescript, Python, C, C++, JAVA</tspan>
<tspan x="390" y="150" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Computer</tspan>:<tspan class="cc"> ........ </tspan><tspan class="value">HTML, CSS</tspan>
<tspan x="390" y="170" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Real</tspan>:<tspan class="cc"> ............ </tspan><tspan class="value">English, Hindi</tspan>
<tspan x="390" y="190" class="cc">. </tspan>
<tspan x="390" y="210" class="cc">. </tspan><tspan class="key">Hobbies</tspan>.<tspan class="key">Software</tspan>:<tspan class="cc"> ........ </tspan><tspan class="value">Cloud, Devops</tspan>
<tspan x="390" y="230" class="cc">. </tspan><tspan class="key">Hobbies</tspan>.<tspan class="key">Hardware</tspan>:<tspan class="cc"> ........ </tspan><tspan class="value">Edge AI, Homelabbing</tspan>
<tspan x="390" y="250" class="cc">. </tspan>
<tspan x="390" y="270">- Contact</tspan> -——————————————————————————————————————————————-—-
<tspan x="390" y="290" class="cc">. </tspan><tspan class="key">Email</tspan>:<tspan class="cc"> ..................... </tspan><tspan class="value">anugrahsinngh@gmail.com</tspan>
<tspan x="390" y="310" class="cc">. </tspan><tspan class="key">LinkedIn</tspan>:<tspan class="cc"> .................. </tspan><tspan class="value">anugrahsinngh</tspan>
<tspan x="390" y="330" class="cc">. </tspan><tspan class="key">X</tspan>:<tspan class="cc"> ......................... </tspan><tspan class="value">anugrahsingh</tspan>
<tspan x="390" y="350" class="cc">. </tspan><tspan class="key">Discord</tspan>:<tspan class="cc"> ................... </tspan><tspan class="value">anugrahsingh</tspan>
"""

for filename in ['/home/shubham-singh/code/Anugrah-Singh/light_mode.svg', '/home/shubham-singh/code/Anugrah-Singh/dark_mode.svg']:
    with open(filename, 'r') as f:
        content = f.read()
    
    # The block we want to replace starts with <text x="390" and goes until </text>
    pattern = re.compile(r'<text x="390"([^>]*)>.*?</text>', re.DOTALL)
    
    def replacer(match):
        attrs = match.group(1)
        res = f'<text x="390"{attrs}>\n{new_text_block}</text>'
        return res

    new_content = pattern.sub(replacer, content)
    with open(filename, 'w') as f:
        f.write(new_content)
    print(f"Updated info in {filename}")

# We should also update today.py to change the birthday to 2006-08-09 so it gives ~20 years uptime
with open('/home/shubham-singh/code/Anugrah-Singh/today.py', 'r') as f:
    today_content = f.read()

today_content = re.sub(r'datetime\.datetime\([0-9]+, [0-9]+, [0-9]+\)', 'datetime.datetime(2006, 8, 9)', today_content)

with open('/home/shubham-singh/code/Anugrah-Singh/today.py', 'w') as f:
    f.write(today_content)
