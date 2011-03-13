import os

def h(options, buildout):
    compile_dir=options["compile-directory"]
    cwd = os.getcwd()
    os.chdir(compile_dir)
    #os.system("cmake %s" % options["configure-options"])
    #fps = [os.path.join('core', 'sql', 'cmake_install.cmake'),
    #       'CMakeLists.txt']
    #for fp in fps:
    #    f = open(fp).read()
    #    content = f.replace('/usr/share/postlbs', '%s/share/postlbs' % options['location'])
    #    open(fp, 'w').write(content)
    print "Running cmake %s" % options["cmake-options"]
    os.system("cmake %s" % options["cmake-options"])
    os.chdir(cwd)

