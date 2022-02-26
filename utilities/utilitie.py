import softest


class utlit(softest.TestCase):
    def assertlistitems(self,list,value):
        for stop in list:
            self.soft_assert(self.assertEqual,stop.text,value)
            if stop.text ==value:
                print("test passed")
        else:
                print("test failed")
        self.assert_all()