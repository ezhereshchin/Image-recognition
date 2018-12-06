def get_threshold():
    result = float(input("Please enter threshold (float 0 to 1)"))
    if result > 1:
        result = 1
    elif result < 0:
        result = 0

    result = int(round(result* 255))
    return result


def apply_threshold(orig, pixelsO, pixelsE):
    threshold = get_threshold()
    width, height = orig.size
    for i in range(width-1):
        for j in range(height-1):
            if pixelsO[i, j][0] < threshold:
                pixelsE[i, j] = (0, 0, 0)
            else:
                pixelsE[i, j] = (255, 255, 255)
    return
