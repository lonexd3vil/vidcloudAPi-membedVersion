try:
    import json
    import os
    import platform
    import httpx
    from bs4 import BeautifulSoup
    import jmespath
except Exception as inpError:
    print(f"Module Error: {inpError}")
    print("trying to install missing modules manually.")
    try:
        os.system("pip install -r req.txt")
    except Exception as dumb:
        print(f"Error: {dumb}")
        exit()
url = "https://membed.net/"
fileName = "homePageData.json"
fileName2 = "searchResults.json"
filename3 = "relatedPostResults.json"
try:
    def main():
        try:
            hostOS = platform.system()
            if hostOS == "Linux":
                os.system("clear")
            elif hostOS == "Windows":
                os.system("cls")
            else:
                pass
            print(f"Detected Host Operating System: {hostOS}")
            if os.path.exists(fileName):
                os.remove(fileName)
            else:
                pass
            if os.path.exists(fileName2):
                os.remove(fileName2)
            else:
                pass
            if os.path.exists(filename3):
                os.remove(filename3)
            else:
                pass
            inpt = input(
                "1. Show Homepage Content\n2. Search Content\nEnter a number: ")
            if inpt == "1" or inpt == "1 ":
                homePage(url)
            elif inpt == "2" or inpt == "2 ":
                userinput = input("Enter the name: ")
                searchPage(url, userinput)
            elif inpt == "exit" or inpt == "exit ":
                exit()
            else:
                myOS = platform.system()
                if myOS == "Linux":
                    os.system("clear")
                    print("Please Enter a valid value.")
                elif myOS == "Windows":
                    os.system("cls")
                    print("Please Enter a valid value.")
                else:
                    print("Unable to detect host operating system.")
                    main()
        except KeyboardInterrupt as duh:
            print("\nExiting")
    def searchPage(url, userinput):
        try:
            lookup = httpx.get(url+"search.html?keyword="+userinput)
            # print(lookup, lookup.url)
            pageData = BeautifulSoup(lookup.content, "html.parser")
            finder = pageData.find_all('li', class_='video-block')
            pageContent = []
            for i in finder:
                data = {}
                data['name'] = i.img['alt']
                data['url'] = i.a['href']
                data['image'] = i.img['src']
                pageContent.append(data)
            myOS = platform.system()
            if myOS == "Linux":
                os.system("clear")
            elif myOS == "Windows":
                os.system("cls")
            else:
                print("Unable to detect host operating system.")
            # pprint.pprint(pageContent)
            totalContent = len(pageContent)
            try:
                jsonString = json.dumps(pageContent)
                jsonFile = open("searchResults.json", "w")
                jsonFile.write(jsonString)
                jsonFile.close()
                print(f"total number of items fetched: {totalContent}")
                if totalContent < 1:
                    print("No search Results Found, Try with different search term.")
                    newInput = input("Enter the name: ")
                    searchPage(url, newInput)
                elif totalContent > 0:
                    with open(fileName2, "r") as homeDataRead:
                        read_data = json.load(homeDataRead)
                        allNames = jmespath.search("[*].name", read_data)

                        contentNames = allNames
                        # indexing = contentNames.index(1)
                        totalNames = len(contentNames)
                        indexing = 0
                        intValue = "1"
                        counter = 1
                        # print(f"Indexing Value Before: {indexing}")
                        while indexing < totalNames:
                            perValue = contentNames[indexing]
                            # print(perValue)
                            newValue = intValue+" - "+perValue
                            indexing = indexing+1
                            counter = counter+1
                            intValue = ""
                            intValue = f"{intValue}{counter}"
                            # print(f"New Modified Names: {newValue}")
                            print(newValue)

                        # pprint.pprint(allNames)
                        try:
                            getName = int(input("Select: "))
                            if type(getName) == str:
                                print("Not a INT")
                            elif type(getName) == int:
                                print("Value is a INT")
                            getName = getName-1
                            userChoice = jmespath.search(
                                f"[{getName}].url", read_data)
                            userChoiceName = jmespath.search(
                                f"[{getName}].name", read_data)
                            print(
                                f"Content Name: {userChoiceName}\nContent URL: {userChoice}")
                            print("Forwarding it to content lookup function!")
                            hostOS = platform.system()
                            if hostOS == "Linux":
                                os.system("clear")
                            elif hostOS == "Windows":
                                os.system("cls")
                            else:
                                pass
                            homeDataRead.close()
                            contentPage(userChoice)
                        except UnboundLocalError as Eint:
                            print(
                                f"Something wrong in search selector function: {Eint}")
                else:
                    pass
            except Exception as EH:
                print(EH)
        except Exception as e:
            print(f"Something Wrong: {e}")

    def homePage(url):
        try:
            lookup = httpx.get(url)
            # print(lookup, lookup.url)
            pageData = BeautifulSoup(lookup.content, "html.parser")
            finder = pageData.find_all('li', class_='video-block')
            pageContent = []
            for i in finder:
                data = {}
                data['name'] = i.img['alt']
                data['url'] = i.a['href']
                data['image'] = i.img['src']
                data['addition-time'] = i.span.text
                pageContent.append(data)
            myOS = platform.system()
            if myOS == "Linux":
                os.system("clear")
            elif myOS == "Windows":
                os.system("cls")
            else:
                print("Unable to detect host operating system.")
                exit()
            totalContent = len(pageContent)
            jsonString = json.dumps(pageContent)
            jsonFile = open("homePageData.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
            # print(f"total number of items fetched: {totalContent}")
            with open(fileName, "r") as homeDataRead:
                read_data = json.load(homeDataRead)
                allNames = jmespath.search("[*].name", read_data)

                contentNames = allNames
                # indexing = contentNames.index(1)
                totalNames = len(contentNames)
                indexing = 0
                intValue = "1"
                counter = 1
                # print(f"Indexing Value Before: {indexing}")
                while indexing < totalNames:
                    perValue = contentNames[indexing]
                    # print(perValue)
                    newValue = intValue+" - "+perValue
                    indexing = indexing+1
                    counter = counter+1
                    intValue = ""
                    intValue = f"{intValue}{counter}"
                    # print(f"New Modified Names: {newValue}")
                    print(newValue)

                # pprint.pprint(allNames)
                getName = int(input("Select: "))
                getName = getName-1
                userChoice = jmespath.search(f"[{getName}].url", read_data)
                userChoiceName = jmespath.search(
                    f"[{getName}].name", read_data)
                # print(
                #     f"Content Name: {userChoiceName}\nContent URL: {userChoice}")
                # print("Forwarding it to content lookup function!")
                hostOS = platform.system()
                if hostOS == "Linux":
                    os.system("clear")
                elif hostOS == "Windows":
                    os.system("cls")
                else:
                    pass
                homeDataRead.close()
                contentPage(userChoice)
        except Exception as e:
            print(f"Something Wrong: {e}")

    def contentPage(mainUrl):
        baseURL = f"https://membed.net{mainUrl}"
        mediaLookup = httpx.get(baseURL)
        mediaData = BeautifulSoup(mediaLookup.content, "html.parser")
        # nameFinder = mediaData.find('div', class_='video-info-left')
        nameFinder = mediaData.find('h1').text
        descFinder = mediaData.find('div', class_='content-more-js').text
        videoFinder = mediaData.find_all('iframe')
        for iframe in videoFinder:
            iframeLocation = iframe['src']
            print(
                f"""
Media Name: {nameFinder}
---------------------------------------------------------------------------------------------------------------------
Media Page Link: https://membed.net{mainUrl}
---------------------------------------------------------------------------------------------------------------------
Media Streaming Link: https:{iframeLocation}
---------------------------------------------------------------------------------------------------------------------
Media Description: {descFinder}
---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------

""")
        print("1. Go one to search menu\n2. Go back to home menu\n3. Load related content\n\n\nPress any other key to go back to start menu")
        print("---------------------------------------------------------------------------------------------------------------------")
        choiceFromContentPage = input("Select: ")
        if choiceFromContentPage == "1":
            userData = input("Enter the name: ")
            searchPage(url, userData)
        elif choiceFromContentPage == "2":
            homePage(url)
        elif choiceFromContentPage == "3":
            relatedPost(mainUrl)
        else:
            pass
    def relatedPost(postUrl):
        Rurl = f"{url}{postUrl}"
        RLookup = httpx.get(Rurl)
        Rmedia = BeautifulSoup(RLookup.content, "html.parser")
        Rlocator = Rmedia.find('ul', class_='listing items lists')
        finder2 = Rlocator.find_all('li', class_='video-block')
        relatedContent = []
        for r in finder2:
            Rdata = {}
            Rdata['name'] = r.img['alt']
            Rdata['url'] = r.a['href']
            Rdata['image'] = r.img['src']
            Rdata['addition-time'] = r.span.text
            relatedContent.append(Rdata)
        myOS = platform.system()
        if myOS == "Linux":
            os.system("clear")
        elif myOS == "Windows":
            os.system("cls")
        else:
            print("Unable to detect host operating system.")
            exit()
        totalrelatedContent = len(relatedContent)
        RjsonString = json.dumps(relatedContent)
        RjsonFile = open(filename3, "w")
        RjsonFile.write(RjsonString)
        RjsonFile.close()
        # print(f"total number of items fetched: {totalContent}")
        with open(filename3, "r") as relatedPostRead:
            Rread_data = json.load(relatedPostRead)
            RallNames = jmespath.search("[*].name", Rread_data)
            RcontentNames = RallNames
            # indexing = contentNames.index(1)
            RtotalNames = len(RcontentNames)
            Rindexing = 0
            RintValue = "1"
            Rcounter = 1
            # print(f"Indexing Value Before: {indexing}")
            while Rindexing < RtotalNames:
                RperValue = RcontentNames[Rindexing]
                # print(perValue)
                RnewValue = RintValue+" - "+RperValue
                Rindexing = Rindexing+1
                Rcounter = Rcounter+1
                RintValue = ""
                RintValue = f"{RintValue}{Rcounter}"
                # print(f"New Modified Names: {newValue}")
                print(RnewValue)

            # pprint.pprint(allNames)
            RgetName = int(input("Select: "))
            RgetName = RgetName-1
            userChoice2 = jmespath.search(f"[{RgetName}].url", Rread_data)
            userChoiceName2 = jmespath.search(
                f"[{RgetName}].name", Rread_data)
            # print(
            #     f"Content Name: {userChoiceName2}\nContent URL: {userChoice2}")
            # print("Forwarding it to content lookup function!")
            hostOS = platform.system()
            if hostOS == "Linux":
                os.system("clear")
            elif hostOS == "Windows":
                os.system("cls")
            else:
                pass
        relatedPostRead.close()
        contentPage(userChoice2)
        
except KeyboardInterrupt as ki:
    print(f"okei, closing the programm")
main()
