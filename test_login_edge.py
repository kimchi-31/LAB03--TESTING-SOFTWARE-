import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.use_chromium = True
        service = Service()
        self.driver = webdriver.Edge(service=service, options=options)
        self.driver.get("http://127.0.0.1:5500/test/login.html")
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(2)  # Giữ trình duyệt mở thêm chút để quan sát
        self.driver.quit()

    def test_login_success(self):
        self.driver.find_element(By.NAME, "username").send_keys("sv1@ptit.edu.vn")
        self.driver.find_element(By.NAME, "pass").send_keys("P@ssw0rd")
        self.driver.find_element(By.CLASS_NAME, "login100-form-btn").click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("dashboard"))
        self.driver.save_screenshot("screenshots/login_success.png")
        print("✅ Đăng nhập thành công")

    def test_login_wrong_password(self):
        self.driver.find_element(By.NAME, "username").send_keys("sv1@ptit.edu.vn")
        self.driver.find_element(By.NAME, "pass").send_keys("sai_mat_khau")
        self.driver.find_element(By.CLASS_NAME, "login100-form-btn").click()
        time.sleep(1)
        self.driver.save_screenshot("screenshots/wrong_password.png")
        print("❌ Sai mật khẩu → đã chụp màn hình")

    def test_login_empty_fields(self):
        self.driver.find_element(By.CLASS_NAME, "login100-form-btn").click()
        time.sleep(1)
        self.driver.save_screenshot("screenshots/empty_fields.png")
        print("⚠️ Bỏ trống trường → đã chụp màn hình")

    def test_forgot_password_link(self):
        self.driver.find_element(By.LINK_TEXT, "Forgot password?").click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("forgot"))
        self.driver.save_screenshot("screenshots/forgot_password.png")
        print("🔗 Link quên mật khẩu hoạt động")

    def test_sign_up_link(self):
        self.driver.find_element(By.LINK_TEXT, "Sign Up").click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("signup"))
        self.driver.save_screenshot("screenshots/sign_up.png")
        print("📝 Link đăng ký hoạt động")

    def test_social_login_buttons(self):
        socials = self.driver.find_elements(By.CLASS_NAME, "login100-social-item")
        self.assertEqual(len(socials), 3)
        self.driver.save_screenshot("screenshots/social_buttons.png")
        print("🌐 Đã chụp màn hình các nút social login")

if __name__ == "__main__":
    unittest.main()