def main():
    from views.biodinamica import vp_start_gui
    from mongoengine import connect

    connect(db="tea-db",host="172.17.0.2",port=27017)
    vp_start_gui()

if __name__ == "__main__":
    main()