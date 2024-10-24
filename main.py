'''
    Main Python File
'''

from python_library.average import average, calculate_time_memory

data_path = "data/movie_rating_16_17.csv"

if __name__ == "__main__":
    data_path = "data/movie_rating_16_17.csv" 

    avg_weight = average(data_path)
    print(f"Average weight: {avg_weight:.5}")

    end_mem_usage, elapsed_time = calculate_time_memory(data_path)

    print(f"Final Memory Usage: {end_mem_usage} kilobytes")
    print(f"Total Elapsed Time: {elapsed_time:.7} seconds")