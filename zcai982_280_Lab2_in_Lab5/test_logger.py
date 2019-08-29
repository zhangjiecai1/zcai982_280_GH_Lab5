# Zhangjie Cai zcai982
import unittest
from logger import Logger

#--------------------------------------------------

class Target:
    
    def targetset(self, a):
        self.__message = a
        
    def targetget(self):
        return self.__message
    
#--------------------------------------------------
    
class LoggerTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_info(self):
        #arrange
        mes = Target()
        log = Logger(mes.targetset)
        #act
        log.info("test message")
        #assert
        self.assertEqual(mes.targetget(), "[INFO] test message")

    def test_error(self):
        #arrange
        mes = Target()
        log = Logger(mes.targetset)
        #act
        log.error("test message")
        #assert
        self.assertEqual(mes.targetget(), "[WARNING] test message")


if __name__ == '__main__':
    unittest.main()
