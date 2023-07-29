# to start the venv: $ source project3_env/Scripts/activate
# to start flask server: flask run
# to start next.js: npm run dev
# project3/src/backend/
import csv
from AdjList import AdjList
from Food import Food
import heapq
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import collections
import random
import time


food_graph = AdjList()
vectorizer = TfidfVectorizer()

# function to return the cosine similarity of two strings


def cosine_sim(str1, str2):
    # Create vectors based of the strings
    vectors = vectorizer.fit_transform([str1, str2])
    # Compute the cosine similarity between the vectors
    cosine_sim = cosine_similarity(vectors[0], vectors[1])[0][0]
    return cosine_sim


def parse_csv():
    with open("Project3Backend/formatted_data.csv", mode="r", encoding="utf8") as file:
        csvFile = csv.reader(file)

        first_line = True
        count = 0

        for row in csvFile:
            count += 1
            if count > CONST_NUM_ITEMS:
                break
            if first_line:
                first_line = False
            else:
                food_node = Food(
                    row[0],
                    row[1],
                    # row[2],
                    # row[3],
                    # row[4],
                    # row[5],
                    # row[6],
                    # row[7],
                    # row[8],
                )
                print(food_node.name)

                food_graph.addVertex(food_node)
                count_nodes = 0
                for key in food_graph.graph:
                    if (
                        key != food_node.name
                        and cosine_sim(key, food_node.name) > CONST_SIMILARITY_THRESHOLD
                    ):
                        print("adding edge: from: ", food_node.name, " to: ", key)
                        food_graph.addEdge(key, food_node.name + food_node.brand)
                        food_graph.addEdge(food_node.name + food_node.brand, key)
                        count_nodes += 1
                    if count_nodes > CONST_MAX_ADJACENT:
                        break


# count = 0
# for key in food_graph.graph:
#     count += 1
#     print("Food: ", key, "adj nodes: ", print(food_graph.graph[key][1]))
#     if count > 10000:
#         break


def search(word):
    # [0.234234, peanut butter]
    heap = []
    maxCosine = None
    for food in food_graph.graph:
        food_name = food_graph.graph[food][0].getName()
        currCosine = max(
            cosine_sim(food_name, food_name),
            maxCosine if maxCosine else 0,
        )
        if currCosine != maxCosine and food_name != word:
            maxCosine = currCosine
            heapq.heappush(heap, [maxCosine, food])
            if len(heap) > 10:
                heapq.heappop(heap)
    return heap


def dfs(heap):
    print(heap)
    start_time = time.time()
    stack = [heapq.heappop(heap)]
    res = set()
    res_list = []

    while len(res) < 10:
        while stack:
            for i in range(len(stack)):
                node = stack.pop()
                res.add(node[1])
                res_list.append(node[1])
                if len(res) > 10:
                    end_time = time.time()
                    return res, end_time - start_time
                for adj_node in food_graph.graph[node[1]][1]:
                    if adj_node not in res:
                        stack.append([1, adj_node])
        if heap:
            stack.append(heapq.heappop(heap))
        else:
            heap = search(res_list[-1])
            stack.append(heap[-1])
    end_time = time.time()
    return res, end_time - start_time


# def bfs(heap):
#     start_time = time.time()
#     start = heapq.heappop(heap)
#     queue = collections.deque([start])
#     res = set()
#     res.add(start[1])
#     res_list = [start[1]]

#     while len(res) < 10:
#         while queue:
#             for i in range(len(queue)):
#                 node = queue.popleft()
#                 if len(res) > 10:
#                     end_time = time.time()
#                     return res, end_time - start_time
#                 for adj_node in food_graph.graph[node[1]][1]:
#                     if adj_node not in res and len(res) < 10:
#                         res.add(node[1])
#                         res_list.append(node[1])
#                         queue.append([1, adj_node])
#         if len(res) > 10:
#             end_time = time.time()
#             return res, end_time - start_time
#         if heap:
#             queue.append(heapq.heappop(heap))
#         else:
#             heap = search(res_list[random.randint(0, len(res_list) - 1)])
#             queue.append(heap[-1])
#     end_time = time.time()
#     return res, end_time - start_time

CONST_SIMILARITY_THRESHOLD = 0.4
CONST_NUM_ITEMS = 100
CONST_MAX_ADJACENT = 10
parse_csv()
node = search("Peanut butter")
print(dfs(node))
