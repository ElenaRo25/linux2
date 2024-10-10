import unittest
import os

class TestFileCommands(unittest.TestCase):

    def test_list_files(self):
        # Создаем временную директорию и файлы для теста
        os.makedirs('test_dir', exist_ok=True)
        with open('test_dir/test_file1.txt', 'w') as f:
            f.write('Test file 1')
        with open('test_dir/test_file2.txt', 'w') as f:
            f.write('Test file 2')

        # Здесь вызовите вашу команду для вывода списка файлов
        files = os.listdir('test_dir')
        
        self.assertIn('test_file1.txt', files)
        self.assertIn('test_file2.txt', files)

    def test_extract_files(self):
        # Здесь добавьте код для разархивирования и проверку путей
        pass

if __name__ == '__main__':
    unittest.main()
