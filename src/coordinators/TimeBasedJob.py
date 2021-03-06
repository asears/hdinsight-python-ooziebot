# DISCLAIMER: © 2016 Microsoft Corporation. All rights reserved. Sample scripts in this guide are not supported under any
# Microsoft standard support program or service. The sample scripts are provided AS IS without warranty of any kind.
# Microsoft disclaims all implied warranties including, without limitation, any implied warranties of merchantability or
# of fitness for a particular purpose. The entire risk arising out of the use or performance of the sample scripts and
# documentation remains with you. In no event shall Microsoft, its authors, or anyone else involved in the creation,
# production, or delivery of the scripts be liable for any damages whatsoever (including, without limitation, damages
# for loss of business profits, business interruption, loss of business information, or other pecuniary loss) arising
# out of the use of or inability to use the sample scripts or documentation, even if Microsoft has been advised of the
# possibility of such damages.

from lxml import etree
import os
import sys
import datetime

global frequency, timeReturned

def addProperty(name, value):
    result=name+"="+value+"\n";
    return result

def getTime(period):
    if period == "start":
        timeReturned = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
        timeReturned = timeReturned.strftime("%Y-%m-%dT%H:%MZ")
    else:
        timeReturned = datetime.datetime.utcnow()+datetime.timedelta(days=1)
        timeReturned = timeReturned.strftime("%Y-%m-%dT%H:%MZ")
    return timeReturned

numArgs=len(sys.argv)

if(numArgs > 1 ):
    frequency = sys.argv[1]
else:
    frequency = 5

configuration = ""
configuration += addProperty("startTime", getTime("start"))
configuration += addProperty("endTime", getTime("end"))
configuration += addProperty("timeZone", "UTC")
configuration += addProperty("concurrency", "1")
configuration += addProperty("frequency", frequency)
configuration += addProperty("workflowRoot", "${oozie.coord.application.path}")

#Write properties to file
directory = "../target/coordinator"
if not os.path.exists(directory):
    os.makedirs(directory)
jobFileName=directory+"/"+"coordinator.properties"
jobFile=open(jobFileName, "w")
jobFile.write(configuration)
jobFile.close()
