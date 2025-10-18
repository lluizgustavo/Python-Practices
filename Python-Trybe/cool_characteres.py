characteres_file = open("my_favorites_characteres.txt", mode="w")

characteres_file.write("Tio Patinhas\n")
characteres_file.write("Pica Pau\n")
characteres_file.write("Chaves\n")

print("Batman", file=characteres_file)

more_characteres = ['Mutano\n', 'Woody\n']

characteres_file.writelines(more_characteres)

characteres_file.close()