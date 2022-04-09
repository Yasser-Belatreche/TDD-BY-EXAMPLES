class TestCase():
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        exec("self." + self.name + "()")
        self.tearDown()


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def setUp(self):
        self.log = "setUp"

    def tearDown(self):
        self.log += " tearDown"

    def testMethod(self):
        self.log += " testMethod"


class TestCaseTest(TestCase):

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.log == "setUp testMethod tearDown")

    def tearDown():
        pass


TestCaseTest("testTemplateMethod").run()
