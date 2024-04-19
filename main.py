import ultralytics,os,cv2,json

model = ultralytics.YOLO('yolov5s.pt')

for i in os.listdir('images/'):
    img = cv2.imread(f'images/{i}')
    #model.predict(i,save_text=True)
    result = model(img)
    r = json.loads(result[0].tojson())
    name = r[0]['name']
    print(name) #print the result -> name of detected object
    
