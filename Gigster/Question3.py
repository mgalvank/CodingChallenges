import Queue
def solution(a,b,floors,max_capacity,max_weight):
    q = Queue.Queue()


    weight = 0
    people = 0

    no_of_trips = []
    trip = []
    no_of_stops = 0

    #Populate the queue
    for i in range(0,len(a)):
        q.put((i,a[i],b[i]))

    #Assuming that the weight of one person will always be lower than the max weight that the elevator can carry

    #Loop through the queue
    while not q.empty():
        #Peek at the head
        temp = q.queue[0]
        weight += temp[1]
        people += 1

        #Check if the capacity and weight condition passes
        if weight <= max_weight and people <= max_capacity:
            temp = q.get()
            floor = temp[2]
            trip.append(floor)

        else:
            if q.queue[0][1] > max_capacity:
                print "Weight too muhc. Please use stairs"
                q.get()

            no_of_trips.append(trip)
            weight = 0
            people = 0
            trip = []

    no_of_trips.append(trip)
    no_of_trips_update = [x for x in no_of_trips if x != []]
    for i in no_of_trips:
       no_of_stops += len(list(set(i)))

    no_of_stops += len(no_of_trips)
    print no_of_trips_update
    return no_of_stops





# a = [40,40,100,80,20]
# b = [3,3,2,2,3]
# print "No of stops", solution(a,b,3,5,200)


a = [260,80,40]
b = [2,3,3]


print "No of stops", solution(a,b,5,2,200)