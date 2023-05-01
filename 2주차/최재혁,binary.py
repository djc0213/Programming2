import pickle

fares = [1000,2000]

with open('bus.bin', 'wb') as f:
    pickle.dump(fares, f)

with open('bus.bin', 'rb') as f:
    fares_bin = pickle.load(f)
    print(fares_bin)
    print(type(fares_bin))

with open('bus.txt', 'w') as f:
    f.write(f'The fares are : {fares}.')

with open('bus.txt', 'r') as f:
    fares_txt = f.read()
    print(fares_txt + 'Which one would you take?')
    print(type(fares_txt))