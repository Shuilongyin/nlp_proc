# --*--coding: utf-8 --*--
"""
@Author              :    谋杀电视机
@Contact            :    739228954@qq.com
@DateTime        :    2020-07
@Desc                  :    该code主要用来处理aclmdb数据及nlp7294,具体数据介绍见README.md
"""
import os


class AclImdb_processing():

    def __init__(self, dirname):
        self.root = dirname
        self.train_dirname = os.path.join(dirname, 'train')  # train数据的地址
        self.test_dirname = os.path.join(dirname, 'test')  # test数据地址
        self.file_merge(self.train_dirname, 'train')  # 将train数据进行合并
        self.file_merge(self.test_dirname, 'test')  # 将test数据进行合并

    def file_merge(self, dir, result_name):
        """将aclimdb数据文件进行整合,生成2个文件,分别是test/train-pos/neg

        Args:
            dir: String 即目录地址;
            result_name: String 即train或test文件夹;
        Return:
            None;
        """
        all_files = {}
        for root, dirs, files in os.walk(dir, topdown=False):
            self.dirs = dirs  # 子目录
            all_files["all"] = dirs  # [pos,neg unsup]
        for i in range(len(self.dirs)):
            for _, _, files in os.walk(os.path.join(dir, self.dirs[i]), topdown=False):
                all_files[self.dirs[i]] = files  # 将pos,neg unsup文件名称汇总

        if result_name == 'train':
            file = os.path.join(self.root, "train.txt")
            #neg_file = os.path.join(self.root, "train_neg.txt")
        else:
            file = os.path.join(self.root, "test.txt")
            #neg_file = os.path.join(self.root, "test_neg.txt")

        with open(file, "w+", encoding='utf8') as f:
            num = 0
            for i in all_files["pos"]:  # 取pos文件夹下的文件
                num += 1
                if num % 100 == 0:
                    print(result_name, ' pos:', num)
                with open(os.path.join(os.path.join(dir, "pos"), i), encoding="utf8") as fe:  # 打开需要读取的文件
                    f.write(fe.read()+"\t"+"1"+"\n")  # 写入pos总文件中 每个文件进行换行
        #with open(neg_file, "w+", encoding='utf8') as f:
            num = 0
            for i in all_files["neg"]:
                num += 1
                if num % 100 == 0:
                    print(result_name, ' neg:', num)
                with open(os.path.join(os.path.join(dir, "neg"), i), encoding="utf8") as fe:
                    f.write(fe.read()+"\t"+"0"+"\n")


if __name__ == "__main__":
    root = os.getcwd()
    aclimdb_dir = os.path.join(root, 'aclImdb')
    acl_pre = AclImdb_processing(aclimdb_dir)
