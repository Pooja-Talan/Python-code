#Function counter_99() prints the Lyrics of the song 99 Bottles of Beer

def  counter_99():
    for i in range(99, -1, -1):
        # print(i)
        if i == 1:
            print(i, 'bottle of beer on the wall', i, 'bottle of beer.')
            print('Take one down and pass it around, no more bottles of beer on the wall.')
        elif i == 0:
            print('No more bottles of beer on the wall, no more bottles of beer. ')
            print('Go to the store and buy some more, 99 bottles of beer on the wall.')
        elif i == 2:
            print(i, 'bottle of beer on the wall', i, 'bottle of beer.')
            print('Take one down and pass it around', i - 1, 'bottle of beer on the wall.')

        else:
            print(i, 'bottles of beer on the wall', i, 'bottles of beer.')
            print('Take one down and pass it around', i - 1, ' bottles of beer on the wall.')


counter_99()