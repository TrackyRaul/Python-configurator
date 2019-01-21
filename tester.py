import configurator, json


if __name__ == "__main__":
    ''' Example usage of the configurator '''
    conf = configurator.configure("config.json")
    print("User: %s\nPassword: %s\nHost: %s\nDatabase: %s"%(conf.db.user,conf.db.password,conf.db.host,conf.db.database))
    
