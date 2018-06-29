__author__ = 'Administrator'

import paramiko
# from fabric.api import env, put, get


class SSHAction(object):

    def __init__(self, ip, user, password):

        self.user = user
        self.ip = ip
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(ip, 22, user, password)
        self.sftp = self.ssh.open_sftp()

    def run_ssh_command(self, cmd):

        try:
            tdin, stdout, stderr = self.ssh.exec_command(cmd)
            print stderr.read()
        except Exception, ex:
            print ex

    def mkdirs(self,file_path):

        try:
            tdin, stdout, stderr = self.ssh.exec_command('mkdir -p ' + file_path)
            print stderr.read()
        except Exception, ex:
            print ex

    def zipfiles(self, dest_file_name, orig_path):

        try:
            cmd = ' '.join(['zip -r', dest_file_name, orig_path])
            tdin, stdout, stderr = self.ssh.exec_command(cmd)
            print stderr.read()
        except Exception, ex:
            print ex

    def upload_file(self, orig_file, remote_file):

        try:
            self.sftp.put(orig_file, remote_file)
        except Exception, ex:
            print ex

    def download_file(self, orig_file, dest_file):

        try:
            self.sftp.get(orig_file, dest_file)
        except Exception, ex:
            print ex

    # def upload(self, src, dst):
    #
    #     env.user = self.user
    #     env.password = self.password
    #     env.host_strin = self.ip
    #     put(src, dst)

    # def download(self, src, dst):
    #
    #     env.user = self.user
    #     env.password = self.password
    #     env.host_strin = self.ip
    #     get(src, dst)

    def close(self):

        self.ssh.close()

if __name__ == '__main__':

    temp = SSHAction('192.168.1.230', 'root', 'vlifeqa')
    temp.mkdirs('/diskb/picture/test1/test2')
    temp.upload_file(r'F:\photos\europe\IMG_9739.jpg', '/diskb/picture/test1/test2/IMG_9739.jpg')
    print 'complete'