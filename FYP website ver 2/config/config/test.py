from arachni import *
import xml.etree.ElementTree as ET
import webbrowser

def start_scan(in_client,auth):
    jsonOpen = open('./input/input.json', 'r')
    data = json.load(jsonOpen)
    url = data["url"]
    profile = data["profile"]
    jsonOpen.close()

    if(auth):
        in_client.profile('./profiles/Authenticated/'+ get_Profile() + '.json')
        in_client.target(url) # set target url
        container = in_client.start_scan()
        jsonOpen2 = open('./input/input.json', 'w')
        _id = container.get("id")
        data["scan_id"] = _id
        json.dump(data, jsonOpen2, indent=4)
        jsonOpen2.close()
    else:
        in_client.profile('./profiles/Non-authenticated/'+ get_Profile() + '.json')
        in_client.target(url) # set target url
        container = in_client.start_scan()
        jsonOpen2 = open('./input/input.json', 'w')
        _id = container.get("id")
        data["scan_id"] = _id
        json.dump(data, jsonOpen2, indent=4)
        jsonOpen2.close()


def auth_scan_parameters(URL, user, _pass):
    file1 = open('./profiles/Authenticated/' + get_Profile() + '.json', 'r') #open to get data from the json file
    data = json.load(file1)
    file1.close()
    data["plugins"]["autologin"]["url"] = URL
    data["plugins"]["autologin"]["parameters"] = 'email='+user+'&password='+_pass
    file1 = open('./profiles/Authenticated/' + get_Profile() + '.json', 'w') #open file to update the values
    json.dump(data, file1, indent=4)
    file1.close()

def userInput(URL):
    jsonOpen = open('./input/input.json', 'r')
    data = json.load(jsonOpen)
    jsonOpen.close()

    #userinput inserted into the json file
    data["url"] = URL
    jsonOpen = open('./input/input.json', 'w')
    json.dump(data, jsonOpen, indent=4)
    jsonOpen.close
    return URL

def get_ID():
    jsonOpen = open('./input/input.json', 'r')
    data = json.load(jsonOpen)
    jsonOpen.close()
    if(data["scan_id"] != None):
        _id = data["scan_id"]
        return _id
    else:
        print('No Scan ID found !')

def get_Profile():
    file = open('./input/input.json', 'r')#open input json file 
    data = json.load(file)
    profile_Data = data["profile"]  #input selected profile
    file.close()
    return profile_Data

def edit_profile(insert_prof):
    file = open('./input/input.json', 'r')#open input json file 
    data = json.load(file)
    data["profile"] = insert_prof #input selected profile
    file.close()

    file = open('./input/input.json', 'w')
    json.dump(data,file, indent = 4)#write into json file
    file.close()


# def ArachniScan(request):
#     scan_type = "non_authenticated_scan"
#     target_website = request.POST.get('target_website')
#     scan_select = request.POST.get('scan_select')
#     target_username = request.POST.get('target_username')
#     target_password = request.POST.get('target_password')
#     if (target_password == "" and target_username == "" ):
#         #non authenticated scan
#         print(scan_type)
#         return render(request,'arachni_form.html',{'data1':scan_type})
#     else:
#         scan_type= "authenticated_scan"
#         print(scan_type)
#         return render(request,'arachni_form.html',{'data1':scan_type})

def url_in(insert_url):
    URL = insert_url
    #open json file to get data
    jsonOpen = open('./input/input.json', 'r')
    data = json.load(jsonOpen)
    jsonOpen.close()

    #userinput inserted into the json file
    data["url"] = URL
    jsonOpen = open('./input/input.json', 'w')
    json.dump(data, jsonOpen, indent=4)
    jsonOpen.close
    return URL

def generateReport():
    report_tree = ET.parse('reporthtml.xml')
    report_root = report_tree.getroot()
    solution_tree = ET.parse('solution.xml')
    solution_root = solution_tree.getroot()
    today = date.today()
    reportName = str(today)+"_ScanningReport.html"

    if (report_root.text == 'None'):
        f = open(reportName,"w")
        f.write("<html lang='en'>")
        f.write("<head>")
        f.write("<link rel='stylesheet' href='mystyle1.css'>")
        f.write("</head>")
        f.write("<body>")
        f.write("<div class='report'>")
        f.write("<h1>Scanning Report</h1>")
        f.write("<p class='name'>None</p>")
        f.write("</div>")
        f.write("</body>")
        f.write("</html>")
        f.close()
    else:
        f = open(reportName,"w")
        f.write("<html lang='en'>")
        f.write("<head>")
        f.write("<link rel='stylesheet' href='mystyle1.css'>")
        f.write("</head>")
        f.write("<body>")
        f.write("<div class='report'>")
        f.write("<h1>Scanning Report</h1>")
        f.write("<p class='name'>Issue(s) Found</p>")
        f.write("<p class='description'>Issue(s) Description</p>")
        f.write("<p class='solution'>Remedy Guidance</p>")
        f.write("<p class='url'>Issue(s) Site</p>")

        for report1 in report_root:
            for report2 in report1:
                for report3 in report2:
                    for report4 in report2.findall('description'):
                        for report5 in report3.findall('name'):
                            report_description = report4.text
                            report_name = report5.text
                            for report6 in report2.findall('vector'):
                                for report7 in report6.findall('url'):
                                    report_url = report7.text
                                    for solution1 in solution_root.findall('select'):
                                        for solution2 in solution1.findall('name'):
                                            for solution3 in solution1.findall('description'):
                                                for solution4 in solution1.findall('solution'):
                                                    solution_name = solution2.text
                                                    solution_description = solution3.text
                                                    solution_solution = solution4.text
                                                    if (solution_name == report_name):
                                                        f.write("<p class='container'>----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</p>")
                                                        f.write("<p class='name'>"+solution_name+"</p>")
                                                        f.write("<p class='description'>"+report_description+"</p>")
                                                        f.write("<p class='solution'>"+solution_solution+"</p>")
                                                        f.write("<p class='url'>"+report_url+"</p>")
                                                        
                                                


        f.write("</div>")
        f.write("</body>")
        f.write("</html>")  
        f.close()

    webbrowser.open_new_tab(reportName)

def main():
    client = ArachniClient()
    URL = url_in("http://testphp.vulnweb.com/")
    auth = 0
    username = ""
    password = ""
    profile = edit_profile("sql_injection")

    if(auth):
        auth_scan_parameters(URL, username, password)
        start_scan(client, auth)
        while(1):
            if(client.get_report(get_ID(), 'xml') == None and client.get_status(get_ID())["busy"] == True):
                 continue
            else: 
                scan_id = get_ID() 
                print(client.get_status(scan_id))
                print(client.get_report(get_ID(), 'xml'))
                b = client.get_report(get_ID(), 'xml')
                if (type(b) == bytes):
                    b = b.decode("utf-8")
                elif (b == None):
                    b = "<?xml version='1.0'?><report>None</report>"
                c = open("reporthtml.xml","w")
                c.write(b)
                c.close()
                generateReport()
                break
    else:
        start_scan(client, auth)
        while(1):
            if(client.get_report(get_ID(), 'xml') == None and client.get_status(get_ID())["busy"] == True):
                continue
            else: 
                scan_id = get_ID() 
                print(client.get_status(scan_id))
                print(client.get_report(get_ID(), 'xml'))
                b = client.get_report(get_ID(), 'xml')
                if (type(b) == bytes):
                    b = b.decode("utf-8")
                elif (b == None):
                    b = "<?xml version='1.0'?><report>None</report>"
                c = open("reporthtml.xml","w")
                c.write(b)
                c.close()
                generateReport()
                break
        


main()