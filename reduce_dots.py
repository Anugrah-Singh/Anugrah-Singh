import re

new_text_block = """<tspan x="350" y="30">Anugrah-Singh</tspan> -—————————————————————————————————————————————-—-
<tspan x="350" y="50" class="cc">. </tspan><tspan class="key">OS</tspan>:<tspan class="cc"> .................... </tspan><tspan class="value">Linux</tspan>
<tspan x="350" y="70" class="cc">. </tspan><tspan class="key">Uptime</tspan>:<tspan class="cc" id="age_data_dots"> ................ </tspan><tspan class="value" id="age_data">20 years</tspan>
<tspan x="350" y="90" class="cc">. </tspan><tspan class="key">IDE</tspan>:<tspan class="cc"> ................... </tspan><tspan class="value">VSCode</tspan>
<tspan x="350" y="110" class="cc">. </tspan>
<tspan x="350" y="130" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Programming</tspan>:<tspan class="cc"> . </tspan><tspan class="value">Javascript, Typescript, Python, C, C++, JAVA</tspan>
<tspan x="350" y="150" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Computer</tspan>:<tspan class="cc"> .... </tspan><tspan class="value">HTML, CSS</tspan>
<tspan x="350" y="170" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Real</tspan>:<tspan class="cc"> ........ </tspan><tspan class="value">English, Hindi</tspan>
<tspan x="350" y="190" class="cc">. </tspan>
<tspan x="350" y="210" class="cc">. </tspan><tspan class="key">Hobbies</tspan>.<tspan class="key">Software</tspan>:<tspan class="cc"> ...... </tspan><tspan class="value">Cloud, Devops</tspan>
<tspan x="350" y="230" class="cc">. </tspan><tspan class="key">Hobbies</tspan>.<tspan class="key">Hardware</tspan>:<tspan class="cc"> ...... </tspan><tspan class="value">Edge AI, Homelabbing</tspan>
<tspan x="350" y="250" class="cc">. </tspan>
<tspan x="350" y="270">- Contact</tspan> -—————————————————————————————————————————————-—-
<tspan x="350" y="290" class="cc">. </tspan><tspan class="key">Portfolio</tspan>:<tspan class="cc"> ............. </tspan><a href="https://anugrah-singh.github.io/" target="_blank"><tspan class="value">https://anugrah-singh.github.io/</tspan></a>
<tspan x="350" y="310" class="cc">. </tspan><tspan class="key">Email</tspan>:<tspan class="cc"> ................. </tspan><tspan class="value">anugrahsinngh@gmail.com</tspan>
<tspan x="350" y="330" class="cc">. </tspan><tspan class="key">LinkedIn</tspan>:<tspan class="cc"> .............. </tspan><tspan class="value">anugrahsinngh</tspan>
<tspan x="350" y="350" class="cc">. </tspan><tspan class="key">X</tspan>:<tspan class="cc"> ..................... </tspan><tspan class="value">anugrahsingh</tspan>
<tspan x="350" y="370" class="cc">. </tspan><tspan class="key">Discord</tspan>:<tspan class="cc"> ............... </tspan><tspan class="value">anugrahsingh</tspan>
"""

with open('/home/shubham-singh/code/Anugrah-Singh/light_mode.svg', 'r') as f:
    content = f.read()

# Replace the width
content = re.sub(r'width="950px"', 'width="985px"', content)
content = re.sub(r'<rect width="950px"', '<rect width="985px"', content)

# Replace the text block
pattern = re.compile(r'<tspan x="350" y="30">Anugrah-Singh</tspan>.*?(?=\n</text>)', re.DOTALL)
content = pattern.sub(new_text_block.strip(), content)

with open('/home/shubham-singh/code/Anugrah-Singh/light_mode.svg', 'w') as f:
    f.write(content)
print("Updated light_mode.svg")
