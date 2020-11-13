import 'package:get/get.dart';
import 'package:medecine_app/data/models/user_model.dart';
import 'package:medecine_app/data/repository/user_repository.dart';
import 'package:medecine_app/data/utils/exceptions.dart';

class LoginController extends GetxController {
  UserRepository _userRepository = Get.find<UserRepository>();

  final String title = 'Login';
  UserModel get userModel => _userRepository.userModel;

  @override
  void onInit() {
    super.onInit();
    // _userRepository.login('test', 'test');
  }

  Future<UserModel> login(String email, String password) async {
    try {
      UserModel userModel = await _userRepository.login(email, password);
      if (userModel != null) {
        return userModel;
      }
    } on NotAuthorizedException catch (e) {
      print(e.message);
      Get.snackbar('Session expired', 'Login to your account');
    } catch (e) {
      print(e.message);
      Get.snackbar('Error', 'Connection troubles...');
    }
  }
}
