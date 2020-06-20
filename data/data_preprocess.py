# --*--coding: utf-8 --*--
"""

"""
import os


class AclImdb_processing():

    def __init__(self, dirname):
        self.root = dirname
        self.train_dirname = os.path.join(dirname, 'train')
        self.test_dirname = os.path.join(dirname, 'test')
        self.file_merge(self.train_dirname, 'train')
        self.file_merge(self.test_dirname, 'test')

    def file_merge(self, dir, result_name):
        all_files = {}
        for root, dirs, files in os.walk(dir, topdown=False):
            self.dirs = dirs  # 子目录
            all_files["all"] = dirs
        for i in range(len(self.dirs)):
            for _, _, files in os.walk(os.path.join(dir, self.dirs[i]), topdown=False):
                all_files[self.dirs[i]] = files  # 将pos,neg文件名称汇总

        if result_name == 'train':
            pos_file = os.path.join(self.root, "train_pos.txt")
            neg_file = os.path.join(self.root, "train_neg.txt")
        else:
            pos_file = os.path.join(self.root, "test_pos.txt")
            neg_file = os.path.join(self.root, "test_neg.txt")

        with open(pos_file, "w+", encoding='utf8') as f:
            num = 0
            for i in all_files["pos"]:
                num += 1
                if num % 100 == 0:
                    print(result_name, ' pos:', num)
                with open(os.path.join(os.path.join(dir, "pos"), i), encoding="utf8") as fe:
                    f.write(fe.read()+"\n")  # 写入pos总文件中
        with open(neg_file, "w+", encoding='utf8') as f:
            num = 0
            for i in all_files["neg"]:
                num += 1
                if num % 100 == 0:
                    print(result_name, ' neg:', num)
                with open(os.path.join(os.path.join(dir, "neg"), i), encoding="utf8") as fe:
                    f.write(fe.read()+"\n")


if __name__ == "__main__":
    root = os.getcwd()
    aclimdb_dir = os.path.join(root, 'aclImdb')
    acl_pre = AclImdb_processing(aclimdb_dir)
