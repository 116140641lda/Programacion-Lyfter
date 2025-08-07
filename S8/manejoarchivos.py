in_file = 'song.txt'
out_file = 'salida.txt'

def read_songs (in_file, out_file):
    with open(in_file, 'r') as file:
        songs_name = file.readlines()
        songs_name.sort()

    with open(out_file, 'w') as file:
        for line in songs_name:
            file.write(line + '\n')
            print(line)


read_songs (in_file, out_file)


