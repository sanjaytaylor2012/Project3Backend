import csv
from temp_graph import temp_graph
import time
        
CONST_NUM_ITEMS = 1500
CONST_SIMILARITY_THRESHOLD = 0.75
CONST_MAX_ADJACENT = 10
CONST_INTIAL_ADJACENT = 5

def jsim(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    similarity = len(intersection) / len(union)
    return similarity

def create_name_brand_neighbors():
    
    # TODO: read in the data to fully create the graph first.
    # loop through all of the graph and add the neighbors to a new sheet (name+brand, neighbors)
    # create a final sheet template (needs name+brand) and then append the neighbors to it (use a set for name+brand)
    # (test on 1k nodes first)
    # thinkg about the trader joe's problem (name+brand set for the final sheet (check entries for sanity))

    with open('src/final_data.csv', mode='r', encoding="utf8") as file:
        csvFile = csv.reader(file)

        # start the graph creation here:
        first_line = True
        count = 0
        
        for row in csvFile:
            count += 1
            if count > CONST_NUM_ITEMS:
                break
            if first_line:
                first_line = False
            else:
                nameplusbrand = row[0]
                name = row[1]

                food_graph.addVertex(nameplusbrand, name)
                count_of_neighbors = 0

                for key, val in food_graph.graph.items():
                    if len(food_graph.graph[key][1]) < CONST_MAX_ADJACENT:
                        if (key != nameplusbrand and jsim(name, val[0]) > CONST_SIMILARITY_THRESHOLD):
                            food_graph.addEdge(key, nameplusbrand)
                            count_of_neighbors += 1
                    if (count_of_neighbors >= CONST_INTIAL_ADJACENT):
                        break  
            if count % 2000 == 0:
                print(count)

    # with open('src/final_data.csv' ,'w', encoding="utf8", newline='') as file:
    #     writer = csv.writer(file)

    #     for key, val in food_graph.graph.items():
    #         row = []
    #         row.append(key)
    #         for item in val[1]:
    #             row.append(item)
    #         writer.writerow(row)

food_graph = temp_graph()
create_name_brand_neighbors()

# parses through raw_data to 
def raw_data_parser():
    
    
    for item in food_graph:
        print(food_graph[item][1])

    with open('src/raw_data.csv', mode='r', encoding="utf8") as file:
        csvFile = csv.reader(file)
        twoD_array = list(csvFile)

        new_2D = []
        set_of_nameplusbrand = set() # set of "name+brand" keys

        arr = [12, 1, 40, 63, 65, 102, 111, 112, 117]

        for row in range(1, len(twoD_array)):
            new_row = []
            name = twoD_array[row][7]
            brand = twoD_array[row][12]

            if twoD_array[row][33] == "United States" and name != "" and len(name) < 32 and brand != "":
                if name[:7] == "Organic":
                    name = name[8:]    
                nameplusbrand = name + brand
                if nameplusbrand not in set_of_nameplusbrand:
                    new_row.append(nameplusbrand)
                    new_row.append(name)
                    for col in range(0, len(arr)):
                        if twoD_array[row][arr[col]] == '':
                            new_row.append("N/A")
                        else:
                            new_row.append(twoD_array[row][arr[col]])


                    for item in food_graph.graph[nameplusbrand][1]:
                        print(item)
                        new_row.append(item)
                    
                    new_2D.append(new_row)
                    set_of_nameplusbrand.add(nameplusbrand)
        
    with open('src/final_data.csv' ,'w', encoding="utf8", newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["name+brand", "name", "brand", "url", "serving_size", "energy_100g", "fat_100g", "sugar_100g", "protein_100g", "fiber_100g", "sodium_100g", "Adjacent nodes:"])

        for row in new_2D:
            writer.writerow(row)

def main():
    
    start_time = time.time()
    raw_data_parser()
    #create_name_brand_neighbors()
    end_time = time.time()

    print(end_time-start_time)
    
#entry point:
if __name__ == "__main__":
    main()