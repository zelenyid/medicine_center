import 'package:dio/dio.dart';
import 'package:flutter/cupertino.dart';
import 'package:get/get.dart';
import 'package:medecine_app/data/models/patient_model.dart';
import 'package:medecine_app/data/provider/api.dart';

// import 'package:medecine_app/data/utils/exceptions.dart';

class PatientSearchController extends GetxController {
  ApiClient _apiClient = Get.find<ApiClient>();

  final String title = 'Login';

  RxString searchTextController = ''.obs;
  RxList searchResult = [].obs;

  // @override
  // void onInit() async {
  //   super.onInit();
  // }

  Future searchPatient(String name, String surname) async {
    List relatedPatients = [];
    Map filter = {'name': name, 'surname': surname};
    if (name == '') {
      filter.remove('name');
    }
    if (surname == '') {
      filter.remove('surname');
    }
    Response response = await _apiClient.searchPatientByFilter(filter);

    print(response);
    if (response != null) {
      Map data = response.data;
      print('response data: $data');
      if (data["result"] == true) {
        final List allPatients = data['data'];
        for (var doctor in allPatients) {
          relatedPatients.add(PatientModel.fromJson(doctor));
        }
      }
    }
    print('allPatients: $relatedPatients');
    searchResult.value = relatedPatients.obs;
    return relatedPatients;
  }
}
