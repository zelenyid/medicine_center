import 'package:dio/dio.dart';
import 'package:get/get.dart';

import 'package:medecine_app/data/models/disease_history_model.dart';
import 'package:medecine_app/data/models/doctor_model.dart';
import 'package:medecine_app/data/models/patient_model.dart';
import 'package:medecine_app/data/provider/api.dart';


class UserRepository extends GetxService {
  ApiClient _apiClient = Get.find<ApiClient>();
  Rx userModel;
  Rx<PatientModel> patientModel;

  Future register(
      String email,
      String password1,
      String password2,
      String name,
      String surname,
      String patronymic,
      String phone_number,
      String gender,
      String profession,
      String address,
      DateTime birthday) async {
      print('user_repository.dart: before _apiClient');
    Response response = await _apiClient.register(
        email,
        password1,
        password2,
        name,
        surname,
        patronymic,
        phone_number,
        gender,
        profession,
        address,
        birthday);
    if (response != null) {
      var model = PatientModel.fromJson(response.data).obs;
      if (model != null) {
        this.patientModel = model;
        return patientModel;
      }
    }
  }

  Future login(String email, String password) async {
    Response response = await _apiClient.login(email, password);
    if (response != null) {
      Map data = response.data;
      final String role = data['role'];
      final userID = data['user_id'];

      var model;
      if (role == "patient") {
        response = await _apiClient.getPatientByID(userID);
        data = response.data['data'];
        print(data);
        model = PatientModel.fromJson(data).obs;
      } else if (role == 'doctor') {
        response = await _apiClient.getDoctorByID(userID);
        data = response.data['data'];
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
