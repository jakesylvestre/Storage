import ConfigParser
def configSetup():
    config = ConfigParser.RawConfigParser()
    config.add_section('Files')
    for
    config.set('Files','file1','png')
    config.set('Files','file2','mp3')
    config.set('Files','file3','mp4')
    config.set('Files','file1','jpg')
    config.set('Files','file1','jpeg')
    config.set('Files','file1','jfif')
    config.set('Files','file1','jpeg2000')
    config.set('Files','file1','ani')
    config.set('Files','file1','amnim')
    config.set('Files','file1','apng')
    config.set('Files','file1','art')
    config.set('Files','file1','bmp')
    config.set('Files','file1','psd')
    config.set('Files','file1','bsave')
    config.set('Files','file1','cal')
    config.set('Files','file1','cin')
    config.set('Files','file1','cpc')

    with open('example.cfg', 'wb') as configfile:
    config.write(configfile)