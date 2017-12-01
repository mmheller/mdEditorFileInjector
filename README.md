# mdEditorFileInjector
Script to perform bulk edits to mdEditor files by injecting mdJSON content

Date: 11/28/2017
Purpose: to perform bulk edits to mdEditor files by injecting mdJSON content.  mdEditor files are files exported from the mdEditor web application (mdeditor.org).  More information on mdJSON can be found at https://github.com/adiwg/mdJson-schemas.
System Requirements: Python.exe (tested with Python 2.7)
Setup: Copy the file GNLCC_mdEditorFileInject.py to a location where python.exe can access it, along with mdEditor files.  Verify Python is installed.

Arguments:
-C 
(Example -C C:\Apps_Programming\Data_Processing\GNLCCmdEditorInject\Demo)
Folder/Directory path to the location of the mdEditor files (with .json extension).  Do not include files that have the .json extension that should not be processed.  An output folder/directory (mdEditorfiles #date/time#) will be created in this provided folder/directory path and all output files will be placed in this new folder/directory.

-D
(Example -D "metadata|resourceInfo|pointOfContact")
JSON location where to inject the mdJSON.  mdEditor files contain one or many items and some of the items house mdJSON.  JSON locations more than one level should be delimited (separated) by a “|” character.  This argument is not needed for injecting contacts mdJSON.  To determine the JSON location, use the JSON preview in the list view of the mdEditor web application (mdeditor.org).

-F
(Example –F -F C:\Apps_Programming\Data_Processing\GNLCCmdEditorInject\inject_Contact_SRLCC.txt)
Full file path of a text file containing mdJSON to inject.  All valid mdJSON content that goes into a mdJSON array, corresponding with the JSON location (argument –D) or a contact identification number, is designed to work.  

Tips for creating the mdJSON injector content file:
When creating the non-Contacts injector files, copy/paste content in the preview of the mdEditor web application (mdeditor.org) and remove extraneous “-“ dashes that start some lines.  When copying content, copy the content within the brackets but include the curly braces.  Content within the brackets represent items within an array.  Refrain from copying more than one item at a time.  Arrays within an time are fine to include.  See the attached injector files as examples for use or comparison.

Basic JSON formatting can be verified with http://jsoneditoronline.org/.  Click the format button and the right arrow button to verify and aid perusing of JSON.

For creating the Contacts injector files,  Contacts can be manually created using the mdEditor web application (mdeditor.org) or loading exising mdEditor files with contacts (i.e. the LCC contact seed file https://drive.google.com/open?id=0B37ma8FpyQLpdkVGMVFKT285WkE)
Refine the number of contacts by clicking the Contacts list view button --> delete all contacts except the one you want to work with.

Export to mdEditor file --> open the exported file with a text editor or open with http://jsoneditoronline.org/

In not in http://jsoneditoronline.org/, copy/paste the mdEditor text into a fresh http://jsoneditoronline.org/ session --> click the Format JSON… button  click the right arrow

Copy the text from the curly brace under the data: key To the 2nd curly brace past export: true and paste into a new text file and save.
Note: MS Wordpad seems to hold indenting and breaklines better than MS Notepad
 
 
-T
(Example -T True)
Indicates whether injecting contact mdJSON or not.  If the argument is True, the script will treat as a contact.  If the argument is False, the script will not treat as a contact.
MS Dos Prompt Example Usage
 
Files:
mdEditorFileInjector_v1.py: Python script mdEditor inject script.

args_examples.txt: MS Dos prompt command line usage examples

inject_Contact_LCCNetwork.txt: Contacts injector file example

inject_Contact_LCCNetworkDataSteward.txt: Contacts injector file example

inject_Contact_SRLCC.txt: Contacts injector file example

inject_LCCMetadataContact.txt: Metadata contact element injector file example 

inject_LCCResponsibleParty.txt: Responsible party element injector file example

inject_POC_LCC.txt: Point of Contact injector file example

inject_POC_LCCDataSteward.txt: Point of Contact injector file example

inject_RepoSCIcatalog.txt: Repository injector file example
