import ConfigParser
''' Merge as many as ConfigParser as you want'''

def Config_Append(SRC_Config ,DST_Config):
    import tempfile
    temp_src = tempfile.NamedTemporaryFile(delete=True)
    temp_dst = tempfile.NamedTemporaryFile(delete=True)
    with open(temp_src.name,'wb') as src, open(temp_dst.name,'wb') as dst:
        SRC_Config.write(src)
        DST_Config.write(dst)
    DST_Config.read([temp_src.name,temp_dst.name])
    return DST_Config


if __name__ == '__main__':
        # initial
        config_one = ConfigParser.RawConfigParser()
        config_two = ConfigParser.RawConfigParser()
        config_three = ConfigParser.RawConfigParser()
            :
            :
            :
        # read config    
        config_one.read('one.ini')
        config_two.read('two.ini')
        config_three.read('three.ini')
            :
            :
            :
            
        # data manipulation
        blah blah
        
        # config merge
        config_final = reduce(Config_Append, (config_one ,config_two, config_three, ...))
        
        # show
        for i in config_final.sections():
                print '[',i,']'
                print config_final.items(i)
