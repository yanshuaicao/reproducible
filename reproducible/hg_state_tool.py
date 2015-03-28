import hglib
import os
__all__ = ['HGState']

class HGState(object):
    def __init__(self, path):
        self.client, self.hg_root_path = self.find_hg_root(path)


    def find_hg_root(self, path):
        input_path = path
        found_root = False
        while not found_root:
            try:
                client = hglib.open(path)
                found_root = True
            except hglib.error.ServerError:
                ppath = os.path.abspath(os.path.join(path, os.pardir))
                if ppath == path:
                    raise ValueError('No hg repo at %s' % input_path)
                
                path = ppath

        return client, os.path.abspath(path)

    @property
    def has_addmodr(self):
        return '+' in self.client.identify()

    @property
    def has_untracked(self):
        return len(self.client.status()) > 0

    @property
    def is_clean(self):
        return not self.has_untracked and not self.has_addmodr

    @property
    def id_str(self):
        return '-'.join([self.client.branch()] + self.client.identify().split())

    def get_state(self):
        return {'version': self.client.identify(), 
                'status':self.client.status(),
                'branch':self.client.branch()}
        
    
    

        
        
