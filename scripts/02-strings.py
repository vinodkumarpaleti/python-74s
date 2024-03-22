# sample = 'a'
# sample_str = "abc"
# sample_str = """abc"""
# sample_str = "Today's weather is nice"
# 'Today's weather is nice' -> Invalid string

# sample_str = """Microsoft Windows [Version 10.0.22621.2861]
# (c) Microsoft Corporation. All rights reserved.

# Clink v1.6.0.3e6b73
# Copyright (c) 2012-2018 Martin Ridgers
# Portions Copyright (c) 2020-2023 Christopher Antos
# https://github.com/chrisant996/clink"""
# print(sample_str)

# sample_str = "Microsoft Windows [Version 10.0.22621.2861] \
# (c) Microsoft Corporation. All rights reserved. \
# Clink v1.6.0.3e6b73 \
# Copyright (c) 2012-2018 Martin Ridgers \
# Portions Copyright (c) 2020-2023 Christopher Antos\
# https://github.com/chrisant996/clink"
# print(sample_str)

# sample_str = """Microsoft Windows [Version 10.0.22621.2861]
# (c) Microsoft Corporation. All rights reserved.

# Clink v1.6.0.3e6b73
# Copyright (c) 2012-2018 Martin Ridgers
# Portions Copyright (c) 2020-2023 Christopher Antos
# https://github.com/chrisant996/clink"""
# print(len(sample_str))

# print(sample_str.upper())
# print(sample_str.capitalize())
# print(sample_str.count("Microsoft"))

# ans = sample_str.split(" ")
# ans = sample_str.split("\n")
# ans = sample_str.splitlines()
# print(ans)


# sample_str = "Microsoft Windows [Version 10.0.22621.2861]"

# Indexing
# print(sample_str[0])
# print(sample_str[2])
# print(sample_str[-1])
# print(sample_str[-2])

# Slicing
# print(sample_str[0:4]) # 0, 1, 2, 3
# print(sample_str[:5]) # 0, 1, 2, 3, 4
# print(sample_str[20:]) # 0, 1, 2, 3, 4
# print(sample_str[-1:-4]) # 0, 1, 2, 3
# start, start + 1, start + 2 ,.... end
# print(sample_str[-4:-1]) # 0, 1, 2, 3
# print(sample_str[:])
# start, start + 2, start + 4 ,.... end
# print(sample_str[::2])
# print(sample_str[1::2])

# [start:end:step]
# start: 0
# end: end
# step: -1
# print(sample_str[::-1])

# sample_str = "Microsoft Windows [Version 10.0.22621.2861]"
# sample_str[0] = "P" # is not allowed
# print(sample_str)

## String concatenation
# sample_str = "Microsoft Windows [Version 10.0.22621.2861]"
# sample_str = sample_str + "(c) Microsoft Corporation. All rights reserved."
# print(sample_str)

# sample_str = 'abc'
# sample_str *= 10
# print(sample_str)

sample_str = "Microsoft Windows [Version 10.0.22621.2861]"
sample_str = "{1}{0}".format(sample_str, "abc")
print(sample_str)