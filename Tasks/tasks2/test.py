import pathlib


class IncorrectFilename(Exception):
    pass


def get_correct_filenames(filenames: list, use_extension: bool = False):
    longest_name = max(filenames, key=lambda item: len(item))
    longest_width = len(longest_name)
    result = []
    for full_filename in filenames:
        if use_extension:
            extension = pathlib.Path(full_filename).suffix
            filename = full_filename.rstrip(extension)
        else:
            filename = full_filename

        if len(set(filename.lower())) < len(filename):
            raise IncorrectFilename(filename)

        result.append(full_filename.rjust(longest_width, "_"))
    return result
