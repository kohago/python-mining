for i  in range(1,80):
    try:
        print(i)
        if(i == 10):
            raise  Exception
    except Exception:
        print("this is a exception!")
