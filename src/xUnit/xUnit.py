
class TestCase():
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self, result):
        result.testStarted()

        self.setUp()
        try:
            exec("self." + self.name + "()")
        except Exception:
            result.testFailed()
        self.tearDown()

        return result


class TestSuite():
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)


class TestResult():
    def __init__(self):
        self.runCount = 0
        self.failedCount = 0

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.failedCount += 1

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.failedCount)


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def setUp(self):
        self.log = "setUp"

    def tearDown(self):
        self.log += " tearDown"

    def testMethod(self):
        self.log += " testMethod"

    def testBrokenTest(self):
        raise Exception


class TestCaseTest(TestCase):
    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert(test.log == "setUp testMethod tearDown")

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenTest")
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())

    def testFailedResultFormatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert("1 run, 1 failed" == self.result.summary())


suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testFailedResult"))
result = TestResult()
suite.run(result)
print(result.summary())
