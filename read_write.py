f = open('template.html', 'r')
f1 = open('index.html', 'w')
f2 = open('contact.html', 'w')

replacements = {
    'index.html': {'{title}': 'Landing Page', '{heading}': 'Welcome', '{body}': 'This is my cool website'},
    'contact.html': {'{title}': 'Contact Me', '{heading}': 'Get In Touch', '{body}': 'me@example.com'},
}

for line in f.readlines():
    for src, target in replacements['index.html'].iteritems():
        line = line.replace(src, target)
    f1.write(line)
    for src, target in replacements['contact.html'].iteritems():
        line = line.replace(src, target)
    f2.write(line)

f.close()
f1.close()
f2.close()
