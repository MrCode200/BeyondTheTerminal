def sequential_item_id_generator(_id_generator_start = 1):
    while True:
        yield _id_generator_start
        _id_generator_start += 1