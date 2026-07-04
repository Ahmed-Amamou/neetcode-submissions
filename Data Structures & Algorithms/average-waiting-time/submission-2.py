class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        chef_time = customers[0][0]
        customers_wait = 0
        for customer in customers:
            chef_time = (chef_time + customer[1]) if customer[0] <= chef_time else customer[0]+customer[1]
            # print("chef_time",chef_time)
            customers_wait += (chef_time - customer[0])
            # print("customers_wait", customers_wait)
        return customers_wait/len(customers)