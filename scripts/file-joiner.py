import sys

pivot_file = sys.argv[1]
target_file = sys.argv[2]

output_file = 'joined.txt'

field_delimiter = '\t'

f = open(pivot_file, 'r')
pivot_value_by_pivot = dict()
duplicate_pivots = set()
total_pivot_rows = 0
for line in f:
    fields = line.split(field_delimiter)
    pivot = fields[0].strip()
    value = fields[1].strip()
    if pivot in pivot_value_by_pivot:
        duplicate_pivots.add(pivot)
    pivot_value_by_pivot[pivot] = value
    total_pivot_rows += 1
f.close()

# Throw away rows having duplicate pivots.
for pivot in duplicate_pivots:
    del pivot_value_by_pivot[pivot]

print "Total pivot rows: %d" % total_pivot_rows
print "Usable pivot rows: %d" % len(pivot_value_by_pivot)

f = open(target_file, 'r')
f_out = open(output_file, 'w')
total_target_rows = 0
success_target_rows = 0
for line in f:
    fields = line.split(field_delimiter)
    pivot = fields[0].strip()
    value = fields[1].strip()
    if pivot in pivot_value_by_pivot:
        f_out.write('%s\t%s\t%s\n' % (pivot, pivot_value_by_pivot[pivot], value))
        success_target_rows += 1
    total_target_rows += 1
f.close()
f_out.close()

print "Total target rows: %d" % total_target_rows
print "Success target rows: %d" % success_target_rows
