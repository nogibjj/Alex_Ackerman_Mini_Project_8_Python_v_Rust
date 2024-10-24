'''
    Main Python File
'''

from python_library.average import average, calculate_time_memory

data_path = "data/movie_ratings_16_17.csv"

if __name__ == "__main__":
    data_path = "data/movie_ratings_16_17.csv"
    
    # critic_site can be metascore, imdb, tmeter, audience, fandango 
    critic_site = "tmeter"

    critic_avg_score = average(data_path, critic_site)
    print(f"Average Critic Rating ({critic_site}) in 2016: {critic_avg_score:.2f}")

    end_mem_usage, elapsed_time = calculate_time_memory(data_path)

    print(f"Final Memory Usage: {end_mem_usage} kilobytes")
    print(f"Total Elapsed Time: {elapsed_time:.7f} seconds")