import 'package:get/get.dart';
import 'package:medecine_app/data/models/user_model.dart';
import 'package:medecine_app/data/repository/user_repository.dart';

class LoginController extends GetxController{
  UserRepository _userRepository = Get.find<UserRepository>();

  final String title = 'Login';
  UserModel get userModel => _userRepository.userModel;

  @override
  void onInit() {
    super.onInit();
    _userRepository.login('test', 'test');
  }
}