def draw_horizontal_line(screed_data, width, x1, x2, y):
    """
    Draws a horizontal line across the screen
    :param screed_data: array of bytes, eight consecutive pixels stored in one byte
    :param width: screen width, wis divisible by 8
    :param x1: start of horizontal line
    :param x2: end of horizontal line
    :param y: height of line
    :return: new screen data
    """
    
    row_to_write = width*y+(x1//8)
    start_point = x1%8
    end_point = x2%8
    end_row = width*y+(x2//8)
    while 1:
        if row_to_write == end_row and start_point == end_point+1:
            break
        screed_data[row_to_write] = screed_data[row_to_write]|(1<<(7-start_point))
        start_point += 1
        if start_point > 7:
            row_to_write += 1
            start_point = 0
    return screed_data



data = [0,0,0,0,
        0,0,0,0,
        0,0,0,0]


print(draw_horizontal_line(data,4,7,18,1))

for i in data:
    print(bin(i))