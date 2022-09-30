"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

"""Contract
Workers either have a salary contract or an hourly contract. Workers on a salary contract earn the monthly salary. The wage of a worker on on an hourly contract is their hourly wage * the number of hours worked.

Commission
Some but not all workers also receive a commission. There are two types of commission. Some workers receive a fixed bonus on top of their salary. Some workers receive a commission based on the number of contracts they have landed. Their commission is the number of contracts landed * the commission per contract.

Total pay
The total pay of worker is their contract pay + their commission (if any). There are six different types of worker in this scenario and pay is calculated differently for each one:

Workers on an salary contract without commission.
Workers on an hourly contract without commission.
Workers on an salary contract with a bonus commission.
Workers on an hourly contract with a bonus commission.
Workers on an salary contract with a contract commission.
Workers on an hourly contract with a contract commission."""


class Employee:
    def __init__(self, name, contract_type, contract_pay, hours_worked, commission_type, commission_pay, contracts_landed):
        self.name = name
        self.contract_type = contract_type
        self.contract_pay = contract_pay
        self.hours_worked = hours_worked
        self.commission_type = commission_type
        self.commission_pay = commission_pay
        self.contracts_landed = contracts_landed
        self.final_payout = 0

    def get_pay(self):
        if self.contract_type == "salary":
            contract_payout = self.contract_pay
        elif self.contract_type == "hourly":
            contract_payout = self.contract_pay * self.hours_worked
        else:
            contract_payout = 0

        if self.commission_type == "bonus":
            commission_payout = self.commission_pay
        elif self.commission_type == "contract":
            commission_payout = self.commission_pay * self.contracts_landed
        else:
            commission_payout = 0

        self.final_payout = contract_payout + commission_payout
        return self.final_payout
    def __str__(self):

        if self.contract_type == "salary" and self.commission_type == "bonus":
            return self.name + " works on a monthly salary of " + str(self.contract_pay) + " and receives a bonus commission of "+ str(self.commission_pay) +".  Their total pay is " + str(self.final_payout) + "."
        elif self.contract_type == "hourly" and self.commission_type == "bonus":
            return self.name + " works on a contract of " + str(self.hours_worked) + " hours at " + str(self.contract_pay) + "/hour and receives a bonus commission of "+ str(self.commission_pay) +".  Their total pay is " + str(self.final_payout) + "."
        elif self.contract_type == "salary" and self.commission_type == "contract":
            return self.name + " works on a monthly salary of " + str(self.contract_pay) + " and receives a commission for " + str(self.contracts_landed) + " contract(s) at " + str(self.commission_pay) +"/contract.  Their total pay is " + str(self.final_payout) + "."
        elif self.contract_type == "hourly" and self.commission_type == "contract":
            return self.name + " works on a contract of " + str(self.hours_worked) + " hours at " + str(self.contract_pay) + "/hour and receives a commission for " + str(self.contracts_landed) + " contract(s) at " + str(self.commission_pay) +"/contract.  Their total pay is " + str(self.final_payout) + "."
        elif self.contract_type == "salary" and self.commission_type == "none":
            return self.name + " works on a monthly salary of " + str(self.contract_pay) + ".  Their total pay is " + str(self.final_payout) + "."
        elif self.contract_type == "hourly" and self.commission_type == "none":
            return self.name + " works on a contract of " + str(self.hours_worked) + " hours at " + str(self.contract_pay) + "/hour.  Their total pay is " + str(self.final_payout) + "."
        else:
            raise ValueError("Invalid contract type or commission type.")


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'salary', 4000, 0, 'none', 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', 25, 100, 'none', 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'salary', 3000, 0, 'contract', 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'hourly', 25, 150, 'contract', 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'salary', 2000, 0, 'bonus', 1500, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'hourly', 30, 120, 'bonus', 600, 0)
