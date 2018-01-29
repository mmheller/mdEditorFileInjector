# Description:  Edits mdEditor Files
# Created By:  Matt Heller, GNLCC/USFWS
# Date:        11/26/2017
# Updated:     1/23/2018
import socket
import os, errno
import collections
import datetime
import base64
import sys,getopt
import time
import ast
import json

str_mdJSON2InjectFile = ""
str_mdEditorFolderPath = ""
strElement2Edit = ""
blnProcessContacts = ""
strUpdateOption = "1" #default option
strJSON2FINDFile = ""

try:
  opts, args = getopt.getopt(sys.argv[1:],
                    "hu:C:F:D:T:O:f:",
                    ["smdEditorFolderPath=", "smdJSON2InjectFile", "sElement2Edit", "bProcessContacts", "bUpdateOption", "smdJSON2FINDFile"])

except getopt.GetoptError:
  print '-C <smdEditorFolderPath> -F <smdJSON2Inject> -D <sElement2Edit> -T <bProcessContacts> -O <bUpdateOption> -f <smdJSON2FINDFile>'
  sys.exit(2)
for opt, arg in opts:
  if opt == '-h':
     print '-u <username> -p <pwd>'
     sys.exit()
  elif opt in ("-C", "--smdEditorFolderPath"):
     str_mdEditorFolderPath = arg.upper()
  elif opt in ("-F", "--smdJSON2InjectFile"):
     str_mdJSON2InjectFile = arg
  elif opt in ("-D", "--sElement2Edit"):
     strElement2Edit = arg
  elif opt in ("-T", "--bProcessContacts"):
     blnProcessContacts = json.loads(arg.lower())
  elif opt in ("-O", "--bUpdateOption"):
     strUpdateOption = arg
  elif opt in ("-f", "--smdJSON2FINDFile"):
     strJSON2FINDFile = arg

#def removekey(d, key):
#    r = dict(d)
#    del r[key]
#    return r

def CreateBlankASCIIFile (strFileNamePath):
    try:
        os.remove(strFileNamePath)
    except OSError:
        pass
    open(strFileNamePath,"w+")

    return strFileNamePath

def Process_mdEditorInsert(strFileNamePath, strElement2Edit, json_mdJSON2Inject, blnArgContactItem, json_FindContent, strUpdateOption):

  #json_mdJSON2Inject = "testAdmin"
  #json_FindContent = "u'adminstrativeArea"


  try:
      with open(strFileNamePath) as json_data:  #read the mdEditor file
          dic_mdJSON = json.load(json_data)     #grab the json

          blnAddTheContact = False
          if (blnArgContactItem == True) and (strUpdateOption != "3"):
             blnAddTheContact = True
             json_mdJSONTemp = json.loads(json_mdJSON2Inject["attributes"]["json"])
             strContactID2PotentiallyAdd = json_mdJSONTemp["contactId"]

          arrayFinalContent = []
          ii = 0
          for mdEditorItem in dic_mdJSON["data"]:
            ii+=1
            blnIsContactItem = False
            if (blnArgContactItem == True):
                blnAddTheOriginalContact = True

            if ("type" in mdEditorItem):
                if (mdEditorItem["type"] == "contacts"):
                    blnIsContactItem = True

            blnIsContactProjectProduct = False
            if ("json" in  mdEditorItem["attributes"]):#determine if a Contact, Project, or Product element
                blnIsContactProjectProduct = True

            if (blnIsContactItem == True) & (blnIsContactItem == blnArgContactItem) & (blnIsContactProjectProduct == True) & (strUpdateOption != "3"):                        #if contact argument TRUE and passed equals item yes/no type
                json_mdJSON = json.loads(mdEditorItem["attributes"]["json"])  #grab the json within the product/project
                strContactIDTemp = json_mdJSON["contactId"]
                if (strContactID2PotentiallyAdd == strContactIDTemp):
                    if (strUpdateOption == "2"):
                      blnAddTheOriginalContact = False
                    else:
                      blnAddTheContact = False

            elif (blnIsContactItem == True) & (blnIsContactItem == blnArgContactItem) & (blnIsContactProjectProduct == True) & (strUpdateOption == "3"):                        #if contact argument FALSE and  passed equals item yes/no type
                 print "*****************************************************************************************************************"
                 json_mdJSON = json.loads(mdEditorItem["attributes"]["json"])  #grab the json within the contacts
                 arrayElement2Edit = strElement2Edit.split("|")  # convert the path of the element to edit to array
                 iE = 0

                 json_mdJSONTMP = json_mdJSON  #probably don't need to set this tmp var

                 for JSONElement in arrayElement2Edit:
                    print "looking for element:" + JSONElement
                    iE += 1

                    if (JSONElement in json_mdJSONTMP):
                        json_mdJSONTMP = json_mdJSONTMP[JSONElement]

                        if(iE == len(arrayElement2Edit)):
                            for pFindReplaceItem in json_mdJSONTMP:
                                for pPossibleFineGrainItemExistence in pFindReplaceItem:
                                    if (json_FindContent == pPossibleFineGrainItemExistence):
                                        pFindReplaceItem[json_mdJSON2Inject] = pFindReplaceItem[json_FindContent] #get the value
                                        del pFindReplaceItem[json_FindContent] #get the value
                        else:
                            print ""
                    elif(iE == len(arrayElement2Edit)): #if cannot find the element AND the last element in the search array, then assume inject edit.
                        json_mdJSONTMP[JSONElement] = [json_mdJSON2Inject]
                    else:
                        print "issue!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                    print json.dumps(json_mdJSON, indent=4)  #json_mdJSONTMP = json_mdJSON
                    print "*****************************************************************************************************************"
                    mdEditorItem["attributes"]["json"] = json.dumps(json_mdJSON, indent=4)  #json_mdJSONTMP = json_mdJSON

            elif (blnIsContactItem == False) & (blnIsContactItem == blnArgContactItem) & (blnIsContactProjectProduct == True) & (strUpdateOption != 3):                        #if contact argument FALSE and  passed equals item yes/no type
                 print "*****************************************************************************************************************"
                 json_mdJSON = json.loads(mdEditorItem["attributes"]["json"])  #grab the json within the product/project
                 arrayElement2Edit = strElement2Edit.split("|")  # convert the path of the element to edit to array
                 iE = 0

                 json_mdJSONTMP = json_mdJSON  #probably don't need to set this tmp var

                 for JSONElement in arrayElement2Edit:
                    print "looking for element:" + JSONElement
                    iE += 1

                    if (JSONElement in json_mdJSONTMP):
                        json_mdJSONTMP = json_mdJSONTMP[JSONElement]

                        if(iE == len(arrayElement2Edit)):
                            blnAddContent = True
                            for pPossibleFineGrainItemExistence in json_mdJSONTMP:
                                if (strUpdateOption == "4"):
                                    blnAddContent = False
                                if (pPossibleFineGrainItemExistence == json_mdJSON2Inject):
                                    blnAddContent = False
                                if (pPossibleFineGrainItemExistence == json_FindContent):
                                    json_mdJSONTMP.remove(pPossibleFineGrainItemExistence)  # for this find/replace scenario remove the original that matches the find
                                    blnAddContent = False
                            if (blnAddContent) and (json_mdJSON2Inject <> ""):
                                json_mdJSONTMP.append(json_mdJSON2Inject)
                        else:
                            print ""
                    elif(iE == len(arrayElement2Edit)): #if cannot find the element AND the last element in the search array, then assume inject edit.
                        json_mdJSONTMP[JSONElement] = [json_mdJSON2Inject]
                    else:
                        print "issue!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                    print json.dumps(json_mdJSON, indent=4)
                    print "*****************************************************************************************************************"
                    mdEditorItem["attributes"]["json"] = json.dumps(json_mdJSON, indent=4)

            if ((blnArgContactItem == True) and (blnAddTheOriginalContact == True)):
                arrayFinalContent.append(mdEditorItem)
            elif ((blnArgContactItem == True) and (blnAddTheOriginalContact == False)):
                print "skipping adding contact, will replace with another"
            else:
                arrayFinalContent.append(mdEditorItem)

      if (blnAddTheContact == True):
        arrayFinalContent.append(json_mdJSON2Inject)

      dic_mdJSON["data"] = arrayFinalContent
      json_data2 = json.dumps(dic_mdJSON, indent=4)
      print json_data2
      return json_data2


  except Exception, e:
      import traceback, sys# If an error occurred, print line number and error message
      tb = sys.exc_info()[2]
      print "Process_mdEditorInsert: Line %i" % tb.tb_lineno
      print e.message
      pass

def CheckInjectString(str_mdJSON2InjectFile):
  try:
      with open(str_mdJSON2InjectFile) as json_data:  #read the mdEditor file
          dic_mdJSON = json.load(json_data)

      return dic_mdJSON
  except Exception, e:
      import traceback, sys# If an error occurred, print line number and error message
      tb = sys.exc_info()[2]
      print "CheckInjectString: Line %i" % tb.tb_lineno
      print e.message
      return ""


DT_Start = datetime.datetime.now()
print "starting "  + str(DT_Start)
timeout = 60 # timeout in seconds
socket.setdefaulttimeout(timeout)

json_InjectContent = CheckInjectString(str_mdJSON2InjectFile)

json_FindContent = CheckInjectString(strJSON2FINDFile)


print "Looking for mdEditor (.JSON) files in: " + str_mdEditorFolderPath

strNewFolder = str_mdEditorFolderPath + "\\" + "mdEditorFiles" + str(datetime.datetime.now()).replace(" ","_").replace(":","_").replace(".","_")
if not os.path.exists(strNewFolder):
    os.makedirs(strNewFolder)

try:
    basedir = os.path.dirname(str_mdEditorFolderPath) + '\\'
    for pRoot, dirs, pFiles in os.walk(str_mdEditorFolderPath): #loop through the mdEditor
        for pFile in pFiles:
            pExtension = os.path.splitext(pFile)[1]
            if (pExtension == '.json'):
                strFileNamePath = pRoot + '\\' + pFile

                if (pRoot <> strNewFolder): #don't process the files that are processed during this session
                    print "processing file:" + strFileNamePath
                    strOutputText = Process_mdEditorInsert(strFileNamePath, strElement2Edit, json_InjectContent, blnProcessContacts, json_FindContent, strUpdateOption)
                    strOutputFileNamePath2 = CreateBlankASCIIFile(strNewFolder + '\\' + pFile)
                    with open(strOutputFileNamePath2, mode="wb") as outfile:
                        outfile.write(strOutputText)
                    outfile.close()
                else:
                    print "skipping " + strFileNamePath


except Exception, e:
    print "*****************************Start Script error:"  + e.message



