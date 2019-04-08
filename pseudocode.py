get input
for option in all_options:
    field = create_field(option)
    if option_points(field) > best_fold_points:
        best_fold_points = option_points(field)
        best_option = option
