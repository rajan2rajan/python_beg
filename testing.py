 # if this is the main folder then we have to import things to run the program

#-------------------------------------------------
# if we have folder name admin it contain two file name service and product each contain function of same name 
# service contain function admin_service()
# product contain function admin_product()


    #foldername     file_name
from Admin import service , product
    #filename.function_name
service.admin_service()
product.admin_product()

# all import of hello_world
import hello_world 

#-------------------------------------------------

#if we have to import multiple class then

from hello_world import divisible , adding

from hello_world import *  # and have to  make __all__=['name', 'name']
 