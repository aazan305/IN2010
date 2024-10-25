import time
from sorting_algorithms import insertion_sort, merge_sort, quick_sort, bubble_sort

TIME_LIMIT_MS = 100  # definere en tidsgrense på 100 millisekunder

def lese_input(file_name):
    with open(file_name, 'r') as file:
        return [int(line.strip()) for line in file]

def skrive_output(file_name, data):
    algorithms = ['insertion', 'merge', 'quick', 'bubble']
    
    with open(file_name, 'w') as file:
        header = ['n']
        for alg in algorithms:
            header.extend([f'{alg}_cmp', f'{alg}_swaps', f'{alg}_time'])
        file.write(','.join(header) + '\n')

        for i in range(len(data['insertion_cmp'])):
            row = [str(i)]
            for alg in algorithms:
                row.append(str(data[f'{alg}_cmp'][i]))
                row.append(str(data[f'{alg}_swaps'][i]))
                row.append(str(data[f'{alg}_time'][i]))
            file.write(','.join(row) + '\n')

def skrive_sorted_output(file_name, sorted_list):
    with open(file_name, 'w') as file:
        for item in sorted_list:
            file.write(f'{item}\n')

def main(file_name):
    arr = lese_input(file_name)
    results = {
        'insertion_cmp': [],
        'insertion_swaps': [],
        'insertion_time': [],
        'merge_cmp': [],
        'merge_swaps': [],
        'merge_time': [],
        'quick_cmp': [],
        'quick_swaps': [],
        'quick_time': [],
        'bubble_cmp': [],
        'bubble_swaps': [],
        'bubble_time': []
    }

    sorted_list_insertion = []
    sorted_list_merge = []
    sorted_list_quick = []
    sorted_list_bubble = []

    discarded_algorithms = set()

    for i in range(len(arr) + 1):
        sub_arr = arr[:i]

        def run_sorting_alg(alg_fn, alg_name, sub_arr):
            if alg_name in discarded_algorithms:
                results[f'{alg_name}_cmp'].append(0)
                results[f'{alg_name}_swaps'].append(0)
                results[f'{alg_name}_time'].append(0)
                return None

            arr_copy = sub_arr.copy()
            start_time = time.time()
            if alg_name == 'merge':
                sorted_arr, cmp, swaps = alg_fn(arr_copy)
            else:
                cmp, swaps = alg_fn(arr_copy)
                sorted_arr = arr_copy
            elapsed_time_ms = (time.time() - start_time) * 1000  # Konverter til millisekunder

            if elapsed_time_ms > TIME_LIMIT_MS:
                discarded_algorithms.add(alg_name)
                print(f'\nGiving up on {alg_name} due to time limit\n')

            results[f'{alg_name}_cmp'].append(cmp)
            results[f'{alg_name}_swaps'].append(swaps)
            results[f'{alg_name}_time'].append(elapsed_time_ms * 1000)  # Konverter til mikrosekunder

            return sorted_arr

        insertion_sorted = run_sorting_alg(insertion_sort, 'insertion', sub_arr)
        if insertion_sorted and i == len(arr):
            sorted_list_insertion = insertion_sorted

        merge_sorted = run_sorting_alg(merge_sort, 'merge', sub_arr)
        if merge_sorted and i == len(arr):
            sorted_list_merge = merge_sorted

        quick_sorted = run_sorting_alg(quick_sort, 'quick', sub_arr)
        if quick_sorted and i == len(arr):
            sorted_list_quick = quick_sorted

        bubble_sorted = run_sorting_alg(bubble_sort, 'bubble', sub_arr)
        if bubble_sorted and i == len(arr):
            sorted_list_bubble = bubble_sorted

    skrive_output(file_name.split('.')[0] + '_results.csv', results)

    skrive_sorted_output(file_name.split('.')[0] + '_insertion_out.txt', sorted_list_insertion)
    skrive_sorted_output(file_name.split('.')[0] + '_merge_out.txt', sorted_list_merge)
    skrive_sorted_output(file_name.split('.')[0] + '_quick_out.txt', sorted_list_quick)
    skrive_sorted_output(file_name.split('.')[0] + '_bubble_out.txt', sorted_list_bubble)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python main.py <inputfile>")
    else:
        main(sys.argv[1])