data = ['a', 'b', 'c', 'x', 'y', 'z']
file = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h3>Hello World!</h3>
    <p>My name is {B45_0}</p>
    <img src="https://raw.githubusercontent.com/SaintClever/b45/main/assets/{B45_1}.jpeg" alt="{B45_2}">
    <p>My profile was made in B45</p>
</body>
</html>
'''


for i in data:
    data_index = data.index(i)
    print(data_index, i)
    file = file.replace(f'{{B45_{str(data_index)}}}', i)
print(file)