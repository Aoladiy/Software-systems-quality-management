import unittest


def register_user(name, email, password, confirm_password):
    # Проверка наличия пустых значений
    if not name or not email or not password or not confirm_password:
        return False

    # Проверка валидности email
    if '@' not in email or '.' not in email:
        return False

    # Проверка соответствия паролей
    if password != confirm_password:
        return False

    # Все проверки пройдены, пользователь успешно зарегистрирован
    return True


class UserRegistrationTests(unittest.TestCase):

    def test_empty_name_field(self):
        result = register_user("", "example@example.com", "Password123", "Password123")
        self.assertFalse(result, "Empty name field should not allow registration")

    def test_valid_name(self):
        result = register_user("Иванов Иван Иванович", "example@example.com", "Password123", "Password123")
        self.assertTrue(result, "Valid name should allow registration")

    def test_invalid_name(self):
        result = register_user("123", "example@example.com", "Password123", "Password123")
        self.assertFalse(result, "Invalid name should not allow registration")

    def test_empty_email_field(self):
        result = register_user("Иванов Иван Иванович", "", "Password123", "Password123")
        self.assertFalse(result, "Empty email field should not allow registration")

    def test_valid_email(self):
        result = register_user("Иванов Иван Иванович", "example@example.com", "Password123", "Password123")
        self.assertTrue(result, "Valid email should allow registration")

    def test_invalid_email(self):
        result = register_user("Иванов Иван Иванович", "example.com", "Password123", "Password123")
        self.assertFalse(result, "Invalid email should not allow registration")

    def test_empty_password_field(self):
        result = register_user("Иванов Иван Иванович", "example@example.com", "", "")
        self.assertFalse(result, "Empty password field should not allow registration")

    def test_valid_password(self):
        result = register_user("Иванов Иван Иванович", "example@example.com", "Password123", "Password123")
        self.assertTrue(result, "Valid password should allow registration")

    def test_invalid_password(self):
        result = register_user("Иванов Иван Иванович", "example@example.com", "123", "123")
        self.assertFalse(result, "Invalid password should not allow registration")

    def test_empty_confirm_password_field(self):
        result = register_user("Иванов Иван Иванович", "example@example.com", "Password123", "")
        self.assertFalse(result, "Empty confirm password field should not allow registration")

    def test_matching_passwords(self):
        result = register_user("Иванов Иван Иванович", "example@example.com", "Password123", "Password123")
        self.assertTrue(result, "Matching passwords should allow registration")

    def test_non_matching_passwords(self):
        result = register_user("Иванов Иван Иванович", "example@example.com", "Password123", "Password321")
        self.assertFalse(result, "Non-matching passwords should not allow registration")