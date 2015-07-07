from ProxmoxDriver import ProxmoxDriver


class TestProxmoxDriver:

    def test_init(self):
        driver = ProxmoxDriver('localhost')
        assert driver.host == 'localhost'
        assert driver.port == 8006
        assert driver.cookie == {}
        assert driver.root == 'https://localhost:8006/api2/json'
        assert driver.headers is not None

    def test_get(self):
        driver = ProxmoxDriver('localhost')
        response = driver.get('cluster/nextid')
        assert response['data'] == 100
