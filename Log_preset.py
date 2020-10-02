import sys
import logging
import subprocess

#checking directory
subprocess.run('if not exist "LOG" MD LOG', shell = True)

#logger & handlers
logger = logging.getLogger('LOG')
console = logging.StreamHandler()
LGFile = logging.FileHandler(filename = 'LOG\\Log_helper.log', mode = 'w')

#set level
logger.setLevel(logging.DEBUG)
LGFile.setLevel(logging.DEBUG)
console.setLevel(logging.WARNING)

#writing type
formatter = logging.Formatter('[%(asctime)s] %(name)s: %(levelname)s: %(message)s')
LGFile.setFormatter(formatter)
console.setFormatter(formatter)

#add handler
logger.addHandler(console)
logger.addHandler(LGFile)

#naming
LGDebug = logger.debug
LGInfo = logger.info
LGWarning = logger.warning
LGError = logger.error
LGCritical= logger.critical


#Example
LGDebug('This is a debug message')
LGInfo('This is an info message')
LGWarning('This is a warning message')
LGError('This is an error message')
LGCritical('This is a critical message')
LGFile.close()

sys.exit()
