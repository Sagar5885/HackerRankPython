from multiprocessing import Pool

def process_line(line):
    return "FOO: %s" % line

if __name__ == "__main__":
    pool = Pool(4)
    with open('test1.csv') as source_file:
        # chunk the work into batches of 4 lines at a time
        results = pool.map(process_line, source_file, 4)

    for res in results:
        print(res)