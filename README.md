# mdEditorFileInjector
Purpose: to perform bulk edits to mdEditor files by injecting, replacing, or deleting mdJSON content.  mdEditor files are files exported from the mdEditor web application (mdeditor.org).  More information on mdJSON can be found at https://github.com/adiwg/mdJson-schemas.

System Requirements: Python.exe (tested with Python 2.7)

Setup: Copy the file GNLCC_mdEditorFileInject.py to a location where python.exe can access it, along with mdEditor files.  Verify Python is installed.

Arguments:

-O
(Example -O 2)
Sets the inject option.
Projects/Products (Non-Contacts) Option Descriptions:
Option Default:  Write if field does not exist OR exact same value of field does not exist
Option Default with Find File (-f) Specified:  Overwrite the field value if exists (not append)
Option 4: Do nothing if anything exists in the JSON location (-D), else inject
Option 5: Delete JSON content specified in Find file (-f)
Contacts Option Descriptions:
Option Default: if contact ID exists, does not replace or add the contact.
Option 2: if contact ID exists, will replace.  If does not exists, then will add.
Option 3: will utilize the find file (-f) and replace any field name found.

-C 
(Example -C C:\GNLCCmdEditorInject\Demo)
Folder/Directory path to the location of the mdEditor files (with .json extension).  Do not include files that have the .json extension that should not be processed.  An output folder/directory (mdEditorfiles #date/time#) will be created in this provided folder/directory path and all output files will be placed in this new folder/directory.

-D
(Example -D "metadata|resourceInfo|pointOfContact")
JSON location where to inject the mdJSON.  mdEditor files contain one or many items and some of the items house mdJSON.  JSON locations more than one level should be delimited (separated) by a “|” character.  This argument is not needed for injecting contacts mdJSON.  To determine the JSON location, use the JSON preview in the list view of the mdEditor web application (mdeditor.org).

-F
(Example -F C:\GNLCCmdEditorInject\inject_Contact_SRLCC.txt)
Full file path of a text file containing mdJSON to inject.  All valid mdJSON content that goes into a mdJSON array, corresponding with the JSON location (argument –D) or a contact identification number, is designed to work.  

Tips for creating the mdJSON injector content file:
When creating the non-Contacts injector files, copy/paste content in the preview of the mdEditor web application (mdeditor.org) and remove extraneous “-“ dashes that start some lines.  When copying content, copy the content within the brackets but include the curly braces.  Content within the brackets represent items within an array.  Refrain from copying more than one item at a time.  Arrays within an item are fine to include.  See the attached injector files as examples for use or comparison.
Basic JSON formatting can be verified with http://jsoneditoronline.org/.  Click the format button and the right arrow button to verify and aid perusing of JSON.
For creating the Contacts injector files,  Contacts can be manually created using the mdEditor web application (mdeditor.org) or loading exising mdEditor files with contacts (i.e. the LCC contact seed file https://drive.google.com/open?id=0B37ma8FpyQLpdkVGMVFKT285WkE)
Refine the number of contacts by clicking the Contacts list view button ? delete all contacts except the one you want to work with.  Only include one contact per injector file.
Export to mdEditor file ? open the exported file with a text editor or open with http://jsoneditoronline.org/
If not in http://jsoneditoronline.org/, copy/paste the mdEditor text into a fresh http://jsoneditoronline.org/ session ? click the Format JSON… button ? click the right arrow
Copy the text from the curly brace under the data: key To the 2nd curly brace past “export: true” and paste into a new text file and save.
Note: MS Wordpad seems to hold indenting and breaklines better than MS Notepad

-T
(Example -T True)
Indicates whether injecting contact mdJSON or not.  If the argument is True, the script will treat as a contact.  If the argument is False, the script will not treat as a contact.

-f
(Example -f C:\mdEditorFileInjectorWS\find_RepoSCIcatalog.txt)
If updating a project or product (not contact) and using the default option, enter content to find for replacement.  Content can be copied from the mdJSON preview button and removing “-“ dashes.
If a contact and using Option 3. Enter the field name (key name) inside double quotes.

Files:
args_examples.txt: MS Dos prompt command line usage examples
find_AdmistrativeAreaContacts.txt:  Find text file example to find incorrect spelling once entered for the AdministrativeArea area field of contacts.
find_delete_DeprecatedStatus.txt: Find text file example to locate a particular status and delete the value
find_delete_GCMD_Landscape.txt: Find text file example to locate a particular keyword/thesaurus entry and delete the value
find_RepoSCIcatalog.txt: Find text file example to locate a repository entry
find_Status.txt: Find text file example to locate a particular status
FindReplace_Contact_LCCNetworkDataSteward.txt:  Text file example to find a contact based on contactId and replace with content in this text file
inject_Contact_LCCNetwork.txt: Contacts injector file example
inject_Contact_LCCNetworkDataSteward.txt: Contacts injector file example
inject_Contact_SRLCC.txt: Contacts injector file example
inject_GCMD_Landscape.txt: GCMD Keyword injector file example
inject_ISO_Env.txt:  Keyword inject sample text to add the ISO keyword “environment”
inject_ISO_EnvTest.txt:  Test keyword inject sample text to add the ISO keyword “extraTerrestrial”
inject_LCCMetadataContact.txt: Metadata contact element injector file example 
inject_LCCResponsibleParty.txt: Responsible party element injector file example
inject_POC_LCC.txt: Point of Contact injector file example
inject_POC_LCCDataSteward.txt: Point of Contact injector file example
inject_RepoSCIcatalog.txt: Repository injector file example
mdEditorFileInjector_v1.py: Python script mdEditor inject script.
Readme_with_Screenshots_v1.pdf: Help document with screenshot
replace_AdmistrativeAreaContacts.txt:  Replacement inject field name text for contacts
replace_RepoSCIcatalog.txt:  Replacement inject value for the repository field
replace_Status.txt:  Replacement inject value for the status field

Troubleshooting
If appears that no updates happening, verify there are no subfolders in the file path given for the –C argument and try again.  The script will look for files in subfolders and processing duplicate filenames may present version issues.



