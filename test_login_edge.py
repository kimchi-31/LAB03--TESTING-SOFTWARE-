import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
import os

os.makedirs("screenshots", exist_ok=True)

class LoginTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.use_chromium = True
        service = Service()
        self.driver = webdriver.Edge(service=service, options=options)
        self.driver.get("http://127.0.0.1:5500/test/login.html")
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

    def test_login_success(self):
        print("📍 Đang chạy: test_login_success")
        self.driver.find_element(By.NAME, "username").send_keys("sv1@ptit.edu.vn")
        self.driver.find_element(By.NAME, "pass").send_keys("P@ssw0rd")
        self.driver.find_element(By.CLASS_NAME, "login100-form-btn").click()
        time.sleep(1)
        print("📍 URL sau login:", self.driver.current_url)
        self.driver.save_screenshot("screenshots/login_success.png")
        print("✅ Đăng nhập thành công")

    def test_login_wrong_password(self):
        print("📍 Đang chạy: test_login_wrong_password")
        self.driver.find_element(By.NAME, "username").send_keys("sv1@ptit.edu.vn")
        self.driver.find_element(By.NAME, "pass").send_keys("sai_mat_khau")
        self.driver.find_element(By.CLASS_NAME, "login100-form-btn").click()
        time.sleep(1)
        self.driver.save_screenshot("screenshots/wrong_password.png")
        print("❌ Sai mật khẩu → đã chụp màn hình")

    def test_login_empty_fields(self):
        print("📍 Đang chạy: test_login_empty_fields")
        self.driver.find_element(By.CLASS_NAME, "login100-form-btn").click()
        time.sleep(1)
        self.driver.save_screenshot("screenshots/empty_fields.png")
        print("⚠️ Bỏ trống trường → đã chụp màn hình")

    def test_forgot_password_link(self):
        print("📍 Đang chạy: test_forgot_password_link")
        self.driver.find_element(By.LINK_TEXT, "Forgot password?").click()
        time.sleep(1)
        print("📍 URL sau click:", self.driver.current_url)
        self.driver.save_screenshot("screenshots/forgot_password.png")
        print("🔗 Đã click link quên mật khẩu")

    def test_sign_up_link(self):
        print("📍 Đang chạy: test_sign_up_link")
        time.sleep(1)
        try:
            element = self.driver.find_element(By.XPATH, "//a[text()='Sign Up']")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
            time.sleep(1)
            print("📍 URL sau click:", self.driver.current_url)
            self.driver.save_screenshot("screenshots/sign_up.png")
            print("📝 Đã click link đăng ký")
        except Exception as e:
            print("❌ Không tìm thấy phần tử Sign Up:", e)
            self.driver.save_screenshot("screenshots/sign_up_error.png")

    def test_social_login_buttons(self):
        print("📍 Đang chạy: test_social_login_buttons")
        socials = self.driver.find_elements(By.CLASS_NAME, "login100-social-item")
        self.assertEqual(len(socials), 3)
        self.driver.save_screenshot("screenshots/social_buttons.png")
        print("🌐 Đã chụp màn hình các nút social login")

if __name__ == "__main__":
    unittest.main()