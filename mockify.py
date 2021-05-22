import numpy, time


def _invert_case(char, do_invert=False):
    if do_invert:
        char = char.lower() if char >= 'A' and char <= 'Z' else char.upper()
    
    return char


# Attempts to open a file. If that fails, assume it's just a string and mockify it.
def mockify(text_or_source, dump_to_file=False, dump_file_name='mockify.txt'):
    start = time.time()
    char_buffer = list()

    # Side-effecty AF, but whatever. 
    try:
        source = open(text_or_source, 'r').read()  # Not every file name will have a dot, so I don't bother checking.
    except:
        if not isinstance(text_or_source, str):
            raise ValueError('"text_or_source" must be a string or file name.')

        source = text_or_source

    # We could condense this, but is it more readable? Not really.
    for char in source:
        char_buffer.append(_invert_case(char, numpy.random.binomial(1, .5)))

    mockified_text = ''.join(char_buffer)

    # Lines 26-29, in one line - y'know, if code golf is more your speed.
    # mockified_text = ''.join([_invert_case(char, numpy.random.binomial(1, .5)) for char in source])

    # TODO
    if dump_to_file:
        # with open(dump_file_name, 'w') as dump_file:
        #   dump_file.write(mockified_text)
        pass  

    return mockified_text, len(source.split(' ')), time.time()-start


def dump_stats(data):
    print "{} \nMockified {} words in {:0.2f}s\n".format(data[0], data[1], data[2])


def dummy_file(name='dummy.txt'):
    with open(name) as f:
        f.write('hi')
    f.close()

if __name__ == '__main__':
    # Basic testing shows 41000+ words "mockified" in about .5 seconds
    dump_stats(mockify('mockify_1.txt'))
    dump_stats(mockify('mockify_2.txt'))
