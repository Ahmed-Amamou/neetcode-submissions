class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        chef_time = customers[0][0]
        customers_wait = 0
        for arrival, order in customers:
            chef_time = max(chef_time,arrival) + order
            # print("chef_time",chef_time)
            customers_wait += (chef_time - arrival)
            # print("customers_wait", customers_wait)
        return customers_wait/len(customers)