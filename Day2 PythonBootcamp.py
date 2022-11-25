num_of_ppl = 1
print("Welcome to the tip calculator!")
total_bill = input("How much was the total bill?\n$")
split_ot_not = input("would you like to split the bill? y/n\n") 
if(split_ot_not == "y"):
  num_of_ppl = input("how much people where you?\n")

bill_for_each = float(total_bill)/float(num_of_ppl)
  
tip_precent = input("10%, 12%, 15%?\n")

bill_for_each += (bill_for_each/float(tip_precent))
print(str(bill_for_each) + " from each, thank you.")