import 'package:dio/dio.dart';
import 'package:get/get.dart';
import 'package:medecine_app/data/models/hospital_model.dart';
import 'package:medecine_app/data/provider/api.dart';

class HospitalsRepository extends GetxService {
  ApiClient _apiClient = Get.find<ApiClient>();
  RxList hospitals = [].obs;

  Future get() async {
    Response response = await _apiClient.getAllHospitals();
    if (response != null) {
      Map data = response.data;
      if (data != null) {
        if (data["result"]) {
          List hospitals = data["data"];
          List newHospitals = [];
          for (var hospital in hospitals) {
            newHospitals.add(HospitalModel.fromJson(data));
          }
          hospitals = newHospitals.obs;
          return hospitals;
        }
      }
    }
  }
}
