from oauth2client import tools,file
from oauth2client.client import OAuth2WebServerFlow
import httplib2,inspect
from apiclient.discovery import build

Lables = ['angular','ansible','apache','API','AWS',
        'eclipse','front','gcp','git','grunt','HTTP','infra','javaScript'
        'java','linux','log','mysql','nginx','perl','PHP','Python','redis',
        'ruby','scala,spring boot,spring,gcp','svn',
         'tomcat','windows','チューニング','経済','自転車',
         '自動化','所感','不動産','負荷試験'
]

def add_labels():
    
    client_id     = ''
    client_secret = ''
    scope         = 'https://www.googleapis.com/auth/blogger'
    redirect_uri  = 'urn:ietf:wg:oauth:2.0:oob'

    flow = OAuth2WebServerFlow(client_id=client_id,client_secret=client_secret,scope=scope,redirect_uri=redirect_uri)

    storage = file.Storage(__file__ + '.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = tools.run_flow(flow,storage)
    
    http = credentials.authorize(http = httplib2.Http())
    service = build('blogger','v3',http=http)
    posts = service.posts()
    ## great!!
    #print(inspect.getsource(posts.update))
    # #inspect it 
    # for x in inspect.getmembers(posts,inspect.ismethod or inspect.isfunction):
    #     print(x)
    #     #print(inspect.getsource(x))
    #     #print(inspect.signature(x))
    request = posts.list(blogId='3223831016241344918')
    while request !=None:
        post_doc = request.execute()
        if 'items' in post_doc and not (post_doc['items'] is None):
            for post in post_doc['items']:
                #use type to see type
                #print(type(post['labels'])) ==>list
                #print(len(post['labels']))
                #print(type(len(post['labels'])))
                if not ('labels' in post and not (post['labels'] is None) and len(post['labels']) > 0):
                    new_labels =[]
                    title = post['title'].upper()
                    for label in Lables:
                        if label.upper() in title:
                            new_labels.append(label)
                    if(len(new_labels) == 0 ):        
                        if ("JAVA" in title or "JVM" in title or "JAR" in title or "HIBERNATE" in title or "SPRING" in title):
                            new_labels.append("java")
                        if ("BASH" in title or "IO" in title or "SSH" in title):
                            new_labels.append("linux")
                        if ("ANT" in title or "MAVEN" in title or "CHIEF" in title):
                            new_labels.append("devOps")
                    if(len(new_labels) > 0 ):
                        print("change!")
                        post['labels'] = new_labels    
                        update=posts.update(blogId='3223831016241344918',postId=post['id'],body=post)
                        update.execute()

        request= posts.list_next(request,post_doc)

add_labels()