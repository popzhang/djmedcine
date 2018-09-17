from django.shortcuts import render

# Create your views here.

from django.conf import settings
from django.http.response import HttpResponse
from ckeditor_uploader.views import ImageUploadView

from articles.models import *

def hello(request):
    #user = request.GET.get('user')
    #if not user: user = 'world'

    ls = Catalog.objects.filter(upperID = 1)
    dicts = {}
    dicts['ls'] = ls
    try:
        art = Article.objects.get(id=4)
        art_body = art.art_body
    except Article.DoesNotExist:
        art = Article(cataID='111',art_body=art_body,time='2018-06-04')
        art_body = "啥也没有"
    dicts['art_body'] = art_body
    if request.method == 'POST':
        art.art_body = request.POST.get("art_body", None)
        art.save()
    return render(request,'hello.html',dicts)

def index(request):
    #user = request.GET.get('user')
    #if not user: user = 'world'

    ls = Catalog.objects.filter(upperID = 1)
    dicts = {}
    dicts['ls'] = ls
    try:
        art = Article.objects.get(id=4)
        art_body = art.art_body
    except Article.DoesNotExist:
        art = Article(cataID='111',art_body=art_body,time='2018-06-04')
        art_body = "啥也没有"
    dicts['art_body'] = art_body
    if request.method == 'POST':
        art.art_body = request.POST.get("art_body", None)
        art.save()
    return render(request,'index.html',dicts)

def firstclass(request,cataID):
    print("firstclass")
    ls = Catalog.objects.filter(upperID = cataID)

    dicts = {}
    dicts['ls'] = ls

    return render(request,'medicinelist.html',dicts)

def secondclass(request,cataID,articleID):
    print("ssecondclass")
    lsleft = Catalog.objects.filter(upperID = cataID)
    lsarticle = Article.objects.filter(cataID = cataID)

    dicts = {}
    dicts['lsleft'] = lsleft
    dicts['lsarticle'] = lsarticle

    return render(request,'medicineview.html',dicts)

def article_list(request,cataID,articleID):
    print("ssecondclass")
    ls = Catalog.objects.filter(upperID = cataID)
    try:
        o = Catalog.objects.get(cataID = articleID)
    except Catalog.DoesNotExist:
        return render(request,'medicinelist.html')

    dicts = {}
    dicts['o'] = o
    dicts['ls'] = ls

    return render(request,'medicineview.html',dicts)

def cieditor(request):
    import time
    import sys
    if request.method == 'POST':
        uploader = ImageUploadView()
        return uploader.post(request)
    return render(request,'hello.html',{})



















'''
    print("cieditor----------------------------------")
    if request.method == 'POST':
        callback = request.GET.get('CKEditorFuncNum')
        try:
            # print("fdsafdagewafd----------------------------------")

            path = "uploads/" + time.strftime("%Y%m%d%H%M%S",time.localtime())   #还有这里，这里path修改你要上传的路径，我记得我是修改了的，这样就上传到了upload文件夹
            f = request.FILES["upload"]
            file_name = path + "_" + f.name
            #print('dfksajfie3333333333333333333333')
            des_origin_f = open(settings.MEDIA_ROOT+'/'+file_name,"wb+")
            #print(sys.getsizeof(des_origin_f))
            #print('dfksajfie4444444444444444444444')
            for chunk in f:              #我修改的是这里，因为python后期的版本放弃了chunk函数，直接遍历类文件类型就可以生成迭代器了。
                des_origin_f.write(chunk)
            des_origin_f.close()
            url = utils.get_media_url(saved_path)
        except Exception as e:
            print(e)
        # print(callback)
        # print(file_name)
        # res = r"<script>window.parent.CKEDITOR.tools.callFunction("+callback+",'/"+file_name+"',');</script>"
        # print("----------+++fdksajfkanfdskfndsklafjdsk----------------------------------")




        if callback:
            # Respond with Javascript sending ckeditor upload url.
            return HttpResponse("""
            <script type='text/javascript'>
                window.parent.CKEDITOR.tools.callFunction({0}, '{1}');
            </script>""".format(callback, url))
        else:
            retdata = {'url': url, 'uploaded': '1',
                       'fileName': uploaded_file.name}
            return JsonResponse(retdata)
    else:
        raise Http404()
'''