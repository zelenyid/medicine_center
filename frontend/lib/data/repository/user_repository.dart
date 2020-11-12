import 'package:dio/dio.dart';
import 'package:get/get.dart';
import 'package:medecine_app/data/models/user_model.dart';
import 'package:medecine_app/data/provider/api.dart';

class UserRepository extends GetxService{
  ApiClient _apiClient = Get.find<ApiClient>();
  UserModel userModel;


  Future login(String email, String password) async{
    Response response = await _apiClient.login(email, password);
    if(response!=null){
      this.userModel = UserModel.fromJson(response.data);
    return userModel;
    }
    return false;
  }
  
  Future protected() async {
   Response response = await _apiClient.protected();
   print(response.data);
  }
}