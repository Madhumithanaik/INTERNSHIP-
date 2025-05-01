def convert_to_positive_coordinates(coords):
    min_x = min(coord[0] for coord in coords)
    min_y = min(coord[1] for coord in coords)
    
    x_offset = -min_x if min_x < 0 else 0
    y_offset = -min_y if min_y < 0 else 0
    
    return [(x + x_offset, y + y_offset) for x, y in coords]

input_coords = [(1, -2), (-2, 4), (-1, -1), (-8, -3), (0, 4), (10, -3)]
output_coords = convert_to_positive_coordinates(input_coords)
print(output_coords)
