#-------------------------------------------------------------------------------
# Name:        start environmnet
# Purpose:
#
# Author:      L0h1th4
#
# Created:     11/07/2013
# Copyright:   (c) bot 2013
# Licence:     <GPL>
# Testtttttttttt by Lorr
#-------------------------------------------------------------------------------
import os,subprocess,sys
class env:



    def check_path(self):

    ##Chek Mongo Home is set
        if(os.getenv('mongo_home') == None):
                    print("Mongo Home is not set !")
                    self.mongo_home = 0
        else:
                    self.mongo_home = os.getenv('mongo_home')
                    print 'Mongo Home is set to :',self.mongo_home

    ##Check Node Home is set
        if(os.getenv('node_backend_home') == None):
            print("Node Backend Home is not set !")
            self.node_backend_home = 0
        else:
            self.node_backend_home = os.getenv('node_backend_home')
            print "Node Backend Home is set to :",self.node_backend_home

    ##Check Glassfish Home is set
        if(os.getenv('glassfish_home') == None):
            print("Glassfish Home is not set !")
            self.glassfish_home = 0
        else:
            self.glassfish_home = os.getenv('glassfish_home')
            print "Glassfish Home is set to :",self.glassfish_home

    ##Starting Mongo Database
    def start_mongo(self):
        if self.mongo_home !=0:
            start_cmd = self.mongo_home+'\\bin\mongod ' + "--dbpath " +self.mongo_home+'\\data'
            os.system("start cmd /c"+start_cmd)
        else: pass


    ##Starting Node Backends
    def start_node(self):
            if self.node_backend_home!=0:
               start_cmd = "node "+self.node_backend_home+"\\dist\\server.js"
               os.system("start cmd /c"+start_cmd)
            else: pass


    ##Starting Glassfish Server
    def start_glassfish(self):
        if self.glassfish_home!=0:
            start_cmd ="asadmin start-domain --verbose domain1"
            os.chdir(self.glassfish_home+"\\bin")
            os.system(start_cmd)
        else: pass



    ##Check Glassfish is running


    def glassfish_status(self):
        a = service_status()
        check_command = "asadmin list-domains"

       
        os.chdir(self.glassfish_home+"\\bin")
        for index, self.lines in enumerate(a.run_command(check_command)):
            s=self.lines.split()
            if ((index == 0) and ((s[0]+s[1])=="domain1running")):
                self.glassfish_run = 1

            elif((index == 0) and ((s[0]+s[1])=="domain1not")):
                self.glassfish_run = 0

            else:pass

            break



class service_status:
     def run_command(self,command1):
        self.c = command1
        p = subprocess.Popen(self.c, shell = True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
        return iter(p.stdout.readline, b'')


a = env()
a.check_path()
a.start_mongo()
a.start_node()
a.glassfish_status()
if a.glassfish_run!=1:
    print a.glassfish_run
    a.start_glassfish()

sys.exit()
