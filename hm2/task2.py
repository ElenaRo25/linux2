import zlib
import unittest

class TestHashCommand(unittest.TestCase):

    def test_crc32_hash(self):
        data = b'This is a test string.'
        calculated_crc = zlib.crc32(data)

        # Здесь вызовите вашу команду для получения хеша
        # Например, если у вас есть функция calculate_hash
        cmd_crc = calculate_hash(data) # type: ignore

        self.assertEqual(calculated_crc, cmd_crc)

if __name__ == '__main__':
    unittest.main()
