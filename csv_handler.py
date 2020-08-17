# Line ending so file is displayed correctly
line_ending = '\n'

# Function to split each column by its comma separation
def csv_split_columns(line):
  return line.split(',')
  
# Function to join columns so they are comma separated again
def csv_join_columns(line):
  return (',').join(line)

# Function to remove the line ending from each line ('\n')
def remove_line_ending(line):
  if line.endswith(line_ending):
    return line[:-1]
  else:
    return line

# Function to add line endings back in
def join_with_line_endings(data):
  return (line_ending).join(data)

def read(file):
  with open(file) as input_csv_file:
    print('Reading file {}\n'.format(file))
    # Reach each line but remove the line endings 
    lines = list(map(remove_line_ending, input_csv_file.readlines()))
    # Remove last line if it is empty
    if lines[-1] == '':
      del lines[-1]

    print('{} rows of data'.format(len(lines)-1))
    # Split each column
    data = list(map(csv_split_columns, lines))
    print('{} columns per row\n'.format(len(data[0])))
    print('The columns are: {}\n\n'.format(str(data[0])))
    # Close file because it is no longer needed
    input_csv_file.close()
    return data

def write(file, data):
  with open(file, "w") as output_csv_file:
    comma_separated_columns = map(csv_join_columns, data)
    file_as_string = join_with_line_endings(comma_separated_columns)
    print('Writing output to {}\n'.format(file))
    output_csv_file.write(file_as_string)
    print ('Done!')

def join_columns(data):
  return set([''.join(row) for row in data])
