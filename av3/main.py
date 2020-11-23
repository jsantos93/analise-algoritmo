import inputs
import algorithms
import csv
import time

SELECTION = "Selection Sort"
BUBBLE = "Bubble Sort"
PANCAKE = "Pancake Sort"
SHELL = "Shell Sort"
CASES_HEAD = ["Values", "Best Case","Worst Case","Average Case"]
RUN_TIME_HEAD = ["Algoritmos", "1000","10000","20000","50000","75000","100000"]
TEST_CASES = ["1000","10000","20000","50000", "75000", "100000"]

def create_time_file(filename, head, data):
    with open(f'cases_time/{filename}.csv', 'a+') as file:
        filewriter = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        file.seek(0)
        line = file.readline()
        line = line.replace("\n", "").split(",")
        if line == head:
            filewriter.writerow(data)
        else:    
            filewriter.writerow(head)
            filewriter.writerow(data)
        file.close()

if __name__ == "__main__":
    selection_process_time = ["Selection Sort"]
    bubble_process_time = ["Bubble Sort"]
    pancake_process_time = ["Pancake Sort"]
    shell_process_time = ["Shell Sort"]
    entries = inputs.get_entries()
    for values in entries:

        # SELECTION SORT
        start = time.process_time()
        algorithms.selection_sort(entries[values][:])
        selection_process_time.append(time.process_time() - start)
        print(f"{selection_process_time[0]} processing time with {values} values: {time.process_time() - start}")
       
        # BUBBLE SORT
        start = time.process_time()
        result = algorithms.bubble_sort(entries[values][:])
        bubble_process_time.append(time.process_time() - start)
        print(f"{bubble_process_time[0]} processing time with {values} values: {time.process_time() - start}")

        # PANCAKE SORT
        start = time.process_time()
        result = algorithms.pancake_sort(entries[values][:])
        pancake_process_time.append(time.process_time() - start)
        print(f"{pancake_process_time[0]} processing time with {values} values: {time.process_time() - start}")

        # SHELL SORT
        start = time.process_time()
        algorithms.shell_sort(entries[values][:])
        shell_process_time.append(time.process_time() - start)
        print(f"{shell_process_time[0]} processing time with {values} values: {time.process_time() - start}")

    with open('cases_time/processing_time.csv', 'a') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(["Algoritmos", "1000","10000","20000","50000","75000","100000"])
        filewriter.writerow(selection_process_time)
        filewriter.writerow(bubble_process_time)
        filewriter.writerow(pancake_process_time)
        filewriter.writerow(shell_process_time)
        csvfile.close()
    
    for cases in TEST_CASES:
        entries = inputs.generate_inputs(int(cases))
        selection_cases_time = [cases]
        bubble_cases_time = [cases]
        pancake_cases_time = [cases]
        shell_cases_time = [cases]
        for values in entries:
            
            # SELECTION SORT
            start = time.process_time()
            algorithms.selection_sort(entries[values][:])
            selection_cases_time.append(time.process_time() - start)
            print(f"{selection_process_time[0]} processing time with {cases} {values} values: {time.process_time() - start}")

            # BUBBLE SORT
            start = time.process_time()
            result = algorithms.bubble_sort(entries[values][:])
            bubble_cases_time.append(time.process_time() - start)
            print(f"{bubble_process_time[0]} processing time with {values} values: {time.process_time() - start}")

            # PANCAKE SORT
            start = time.process_time()
            result = algorithms.pancake_sort(entries[values][:])
            pancake_cases_time.append(time.process_time() - start)
            print(f"{pancake_process_time[0]} processing time with {values} values: {time.process_time() - start}")

            # SHELL SORT
            start = time.process_time()
            algorithms.shell_sort(entries[values][:])
            shell_cases_time.append(time.process_time() - start)
            print(f"{shell_process_time[0]} processing time with {values} values: {time.process_time() - start}")

        create_time_file(SELECTION, CASES_HEAD, selection_cases_time)
        create_time_file(BUBBLE, CASES_HEAD, bubble_cases_time)
        create_time_file(PANCAKE, CASES_HEAD, pancake_cases_time)
        create_time_file(SHELL, CASES_HEAD, shell_cases_time)
