file, links, versions = input('file | links | versions: ').split()

links = links.split(',')
versions = versions.split(',')

for i in range(len(links)):
    with open(f'{file}.html', 'r') as f:
        data = f.read().replace('{B45}', links[i])

    with open(f'{file} - {versions[i]}.html', 'w') as f:
        f.write(data)