import os

class DiskUsage:

    def disk_usage(self, path):
        total = os.path.getsize(path)
        if(os.path.isdir(path)):
            for filename in os.listdir(path):
                childpath = os.path.join(path, filename)
                if self.disk_usage(childpath) is None:
                    total += 0
                else:
                    total += self.disk_usage(childpath)

        print('{0:<7}'.format(total), path)
