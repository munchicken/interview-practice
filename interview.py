test = [0,1,1,0,1,1,1,0,0,1,0,1,1]
counter = 0
most = 0

for i in test:
    if i == 1:
        counter += 1
        if counter > most:
            most = counter
    else:
        counter = 0

print(most)
