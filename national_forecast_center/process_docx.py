from docx import Document
from docx.shared import Inches
from django.db.models import Q
from .models.documents import *
from security.models import AppUser
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import activate

def handle_docx_file(request):
    filename = request.FILES['file']
    user     = request.user
    document = Document(filename)

    paragraphs = [paragraph for paragraph in document.paragraphs if paragraph.text != ""]

    print("PTTN" in str(filename))
     
    if "PTH"     in str(filename):
        return proccess_pth(user, paragraphs)
    elif "ACT"   in str(filename):
        return proccess_act(user, paragraphs)
    elif "DP10"  in str(filename):
        print("Hola2")
        return proccess_dp10(user, paragraphs)
    elif "EGT00" in str(filename):
        return proccess_egt00(user, paragraphs)
    elif "EGT12" in str(filename):
        return proccess_egt12(user, paragraphs)
    elif "P5"    in str(filename):
        return proccess_p5(user, paragraphs)
    elif "PTM"   in str(filename):
        return proccess_ptm(user, paragraphs)  
    elif "PTRD"  in str(filename):
        return proccess_ptrd(user, paragraphs)  
    elif "PTT"   in str(filename):
        return proccess_ptt(user, paragraphs)
    elif "PTTN"  in str(filename):
        print("Hola")
        #return proccess_pttn(user, paragraphs)
    else:
        pass
        
def proccess_pth(user, paragraphs):
    center  = paragraphs[2].text.split(",")[-1].lstrip().replace(".", "")
    authors = paragraphs[-1].text.split("/")
    author1 = find_userapp(authors[0].split(".")[1].lstrip(), center)
    author2 = find_userapp(authors[1].split(".")[1].lstrip(), center)
    content = str()

    if (author1.user == user or author2.user == user) and (author1.forecast_center.name == author2.forecast_center.name == center):
        for i in range(8, len(paragraphs)-1):
            content += paragraphs[i].text + "\n"
        
        data = {
            #"emision_date":paragraphs[4].text,
            "title":paragraphs[6].text,
            "content":content,
            "notes":paragraphs[5].text,
            "author1":author1,
            "author2":author2,
        }

        pthoy = PTHOY(
            title=data["title"],
            content=data["content"],
            notes=data["notes"],
            author1=data["author1"],
            author2=data["author2"])

        pthoy.save()
        
        return True
    else:
        return None

def proccess_act(user, paragraphs):
    center  = paragraphs[2].text.split(",")[-1].lstrip().replace(".", "")
    authors = paragraphs[-1].text.split("/")
    author1 = find_userapp(authors[0].split(".")[1].lstrip(), center)
    author2 = find_userapp(authors[1].split(".")[1].lstrip(), center)
    content = str()

    for i in range(8, len(paragraphs)-1):
        content += paragraphs[i].text + "\n"
    
    #print(author1.name)
    #print(author2.name)

    data = {
        #"emision_date":paragraphs[4].text,
        "title":paragraphs[6].text,
        "content":content,
        "notes":paragraphs[5].text,
        "author1":author1,
        "author2":author2,
    }

    act = ACT(
        title=data["title"],
        content=data["content"],
        notes=data["notes"])
    #print(notice.title)
    act.save()

    return data 
    return None 

def proccess_dp10(user, paragraphs):
    center  = paragraphs[2].text.split(",")[-1].lstrip().replace(".", "")
    authors = paragraphs[-1].text.split("/")
    author1 = find_userapp(authors[0].split(".")[1].lstrip(), center)
    author2 = find_userapp(authors[1].split(".")[1].lstrip(), center)
    content = str()

    if (author1.user == user or author2.user == user) and (author1.forecast_center.name == author2.forecast_center.name == center):
        for i in range(10, len(paragraphs)-1):
            content += paragraphs[i].text + "\n"
        
        data = {
            #"emision_date":paragraphs[4].text,
            "title":paragraphs[6].text,
            "content":content,
            "notes":paragraphs[5].text,
            "author1":author1,
            "author2":author2,
        }

        dp10 = DP10(
            content=data["content"],
            notes=data["notes"],
            author1=data["author1"],
            author2=data["author2"])

        dp10.save()
        
        return True
    else:
        return None

def proccess_egt00(user, paragraphs):
    center  = paragraphs[2].text.split(",")[-1].lstrip().replace(".", "")
    authors = paragraphs[-1].text.split("/")
    author1 = find_userapp(authors[0].split(".")[1].lstrip(), center)
    author2 = find_userapp(authors[1].split(".")[1].lstrip(), center)
    content = str()

    if (author1.user == user or author2.user == user) and (author1.forecast_center.name == author2.forecast_center.name == center):
        for i in range(10, len(paragraphs)-1):
            content += paragraphs[i].text + "\n"
        
        data = {
            #"emision_date":paragraphs[4].text,
            "title":paragraphs[6].text,
            "content":content,
            "notes":paragraphs[5].text,
            "author1":author1,
            "author2":author2,
        }

        dp10 = DP10(
            content=data["content"],
            notes=data["notes"],
            author1=data["author1"],
            author2=data["author2"])

        dp10.save()
        
        return True
    else:
        return None

def proccess_egt12(user, paragraphs):
    return None 

def proccess_p5(user, paragraphs):
    return None 

def proccess_ptm(user, paragraphs):
    center  = paragraphs[2].text.split(",")[-1].lstrip().replace(".", "")
    authors = paragraphs[-1].text.split("/")
    author1 = find_userapp(authors[0].split(".")[1].lstrip(), center)
    author2 = find_userapp(authors[1].split(".")[1].lstrip(), center)
    content = str()

    if (author1.user == user or author2.user == user) and (author1.forecast_center.name == author2.forecast_center.name == center):
        for i in range(8, len(paragraphs)-1):
            content += paragraphs[i].text + "\n"
        
        data = {
            #"emision_date":paragraphs[4].text,
            "title":paragraphs[6].text,
            "content":content,
            "notes":paragraphs[5].text,
            "author1":author1,
            "author2":author2,
        }

        ptm = PTM(
            title=data["title"],
            content=data["content"],
            notes=data["notes"],
            author1=data["author1"],
            author2=data["author2"])

        ptm.save()
        
        return True
    else:
        return None

def proccess_ptrd(user, paragraphs):
    return None 

def proccess_ptt(user, paragraphs):
    return None 

def proccess_pttn(user, paragraphs):
    center  = paragraphs[2].text.split(",")[-1].lstrip().replace(".", "")
    authors = paragraphs[-1].text.split("/")
    author1 = find_userapp(authors[0].split(".")[1].lstrip(), center)
    author2 = find_userapp(authors[1].split(".")[1].lstrip(), center)
    content = str()
    print("\n")
    print(center)
    print(author1)
    print(author2)
    print(user)
    print("\n")
    if (author1.user == user or author2.user == user) and (author1.forecast_center.name == author2.forecast_center.name == center):
        for i in range(10, len(paragraphs)-1):
            content += paragraphs[i].text + "\n"
        
        data = {
            #"emision_date":paragraphs[4].text,
            "title":paragraphs[6].text,
            "content":content,
            "notes":paragraphs[5].text,
            "author1":author1,
            "author2":author2,
        }

        pttn = PTTN(
            content=data["content"],
            notes=data["notes"],
            author1=data["author1"],
            author2=data["author2"])

        pttn.save()
        
        return True
    else:
        return None 

def find_userapp(lastname, center):
    try:
        return AppUser.objects.get(
            Q(forecast_center__name=center), 
            Q(lastname1=lastname) | Q(lastname2=lastname))
    except:
        return None
     