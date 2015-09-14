def calculate_thumbnail_size(p_width, p_height, desired_longest_side):
    if p_width and p_height:
        w = float(p_width)
        h = float(p_height)
        desired_longest_side = float(desired_longest_side)
        if w > h:
            desired_width = desired_longest_side
            factor = w / desired_longest_side
            desired_height = h / factor
        else:
            desired_height = desired_longest_side
            factor = h / desired_longest_side
            desired_width = w / factor
    else:
        return 400, 300

    return int(desired_width), int(desired_height)
