Script renames multiple files selected files and enumerates them according to given pattern.

Command pattern:
rnmf [PATTERN] (--sort / -s) [FILES]

Pattern should contain \i and (optionally) \g to denote where to put index of the file.

GROUPING FILES:
Files can be grouped: "(file_a file_b)" groups the two files - they will receive the same file index but different group
indexes.

SORTING:
Files are not sorted by default. This can be changed by using --sort or -s with arguments:
a - alphabetical sorting
m - sort by modification date

Example:
rnmf "Hello \i There \g" file_a "(file_b file_c)" file_d
will rename file_a, file_b, file_c and file_d to "Hello 1 There", "Hello 2 There 1", "Hello 2 There 2", "Hello 3 There"
respectively.
If files are grouped, yet \g is not specified within the pattern, the group index will follow the file index after a dot.
