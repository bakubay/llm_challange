import sys
import llm_cli

if(len(sys.argv)>4):
    print("ERROR: too many arguments")
    exit()

if(sys.argv[1] == 'create_order'):
    if(len(sys.argv)==4):
        llm_from = sys.argv[2]
        llm_to = sys.argv[3]

        llm_cli.create_order(llm_from, llm_to)
    else:
        print("ERROR: create_order takes two arguments (create_order from to)")

elif(sys.argv[1] == 'list_orders'):
    if(len(sys.argv)==2):
        llm_cli.list_orders()
    else:
        print("ERROR: wrong number of args. list_orders takes no arguments")

elif(sys.argv[1] == 'take_order'):
    if(len(sys.argv)==3):
        order_id = sys.argv[2]
        llm_cli.take_order(order_id)
    else:
        print("ERROR: wrong number of args. take_order takes only one argument (take_order order_id)")
else:
    print(f'ERROR: unknown command \"{sys.argv[1]}\""')