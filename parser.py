import re

detector = []
tail = []
amp_count_list = [0] * 8000


# @jit(nopython=True) # Set "nopython" mode for best performance, equivalent to @njit
def parse(string):
    global event_header, tail
    channel_re = r"\s*?ch:(\d+)([\s\d-]+);"
    try:
        event_header, tail = map(str.strip, string.split(';', maxsplit=1))
    except ValueError:
        None

    for chan_id, ints in re.findall(channel_re, tail):
        ints = list(map(int, ints.split()))
        #        max_amp = max(ints)
        amp_index = abs(min(ints))
        try:
            amp_count_list[amp_index] += 1
        except IndexError:
            None
    return amp_count_list, event_header

#    split_string = re.split(r"((?<=:)(.+?)(?=;))", string, maxsplit=0)
#    module_serial = re.search(r"\b\w{8}\b", split_string[0])
#    event_number = re.search(r"Ev_\d+;", split_string[0])
#    module_type= re.search(r"\b\w{3}\b", split_string[0])
