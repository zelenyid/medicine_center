import 'package:dio/dio.dart';
import 'package:get/get.dart';
import 'package:medecine_app/data/models/doctor_model.dart';
import 'package:medecine_app/data/models/patient_model.dart';
import 'package:medecine_app/data/provider/api.dart';

class UserRepository extends GetxService {
  ApiClient _apiClient = Get.find<ApiClient>();
  Rx userModel;

  Future login(String email, String password) async {
    Response response = await _apiClient.login(email, password);
    if (response != null) {
      print(response.data);
      Map data = response.data;
      final String role = data['role'];
      final userID = data['user_id'];

      var model;
      if (role == "patient") {
        response = await _apiClient.getPatientByID(userID);
        data = response.data;
        print(data);
        model = PatientModel.fromJson(data).obs;
      } else if (role == 'doctor') {
        response = await _apiClient.getDoctorByID(userID);
        data = response.data;
        print(data);
        model = DoctorModel.fromJson(data).obs;
      }
      if (model != null) {
        this.userModel = model;
        return userModel;
      }
    }
  }

  Future protected() async {
    Response response = await _apiClient.protected();
    print(response.data);
  }
}
