import sys

def parse_csv(file_path, column_name):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            header = lines[0].rstrip().split(',')
            header_lower = [col.lower() for col in header]

            if column_name.lower() not in header_lower:
                print("[ERROR] - unknown column name")
                return

            if len(header_lower) != len(set(header_lower)):
                print("[ERROR] - invalid format - duplicate columns")
                return

            counts = {}
            invalid_format_error = False

            for line_number, line in enumerate(lines[1:], start=2):
                row = line.rstrip().split(',')
                if len(row) != len(header):
                    print(f"[ERROR] - invalid format - different words on line {line_number}")
                    invalid_format_error = True
                    break

                column_index = header_lower.index(column_name.lower())
                column_value = row[column_index].lower()

                counts[column_value] = counts.get(column_value, 0) + 1

            if invalid_format_error:
                return

            unique_words = sorted(counts, key=lambda x: (-counts[x], x))
            print("[OK]")
            for word in unique_words:
                print(word)

    except FileNotFoundError:
        print("[ERROR] - file not found")
    except IOError:
        print("[ERROR] - IO error while reading the file")
    except Exception as e:
        print(f"[ERROR] - {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: csvparser.py <path_to_csv_file> <column_name>")
    else:
        file_path = sys.argv[1]
        column_name = sys.argv[2]
        parse_csv(file_path, column_name)
