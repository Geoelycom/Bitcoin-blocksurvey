#  Des Fermes code test 
#  get node 1 to mine another block, send it to node 2, and check that node 2 received it.
 
#****SOLUTION TO THE QUESTION ASKED BELLOW****

#  To get Node 2 to be connected to Node 1 and 0
#  I have to Delete the setup_network() implented in example_test.py
#  in the run_test() function i will go ahead and call .generate()
#  with any of the nodes and block would be synced to all other nodes.  

#  **def run_test** would look like the following code snippet below

def run_test(self):
    self.nodes[0].generate(1)
    self.sync_blocks()



# to  check and make sure that Node 2 recieve it
# we can write the below test


assert_equal(self.nodes[1].getbestblockhash(), self.nodes[2].getbestblockhash())