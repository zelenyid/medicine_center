import 'package:dio/dio.dart';
import 'package:get/get.dart';
import 'package:medecine_app/data/models/disease_history_model.dart';
import 'package:medecine_app/data/models/patient_model.dart';
import 'package:medecine_app/data/provider/api.dart';

class PatientRepository extends GetxService {
  ApiClient _apiClient = Get.find<ApiClient>();
  RxList patient;
  RxList diseaseHistories = [].obs;


  Future uploadHistoryFile(historyId, {filePath, bytes, String extention}) async {
    if (filePath != null) {
      return await _apiClient.uploadHistoryFileFromPath(filePath, historyId);
    } else if (bytes != null) {
      return await _apiClient.uploadHistoryFileFromBytes(bytes, historyId, extention);
    }
  }

  Future downloadHistoryFile(String historyId) async {
    Response response = await _apiClient.downloadHistoryFile(historyId);
    print(response.data);
    return response;
  }

  Future getDiseaseHistoryByUserId(String userId) async {
    Response response = await _apiClient.getDiseaseHistoriesById(userId);
    if (response != null) {
      print(response.data);
      Map data = response.data;
      print(data);
      if (data['result'] == true) {
        response = await _apiClient.getPatientByID(userId);
        List historiesData = data['data'];
        print(data);
        diseaseHistories.clear();
        for (Map history in historiesData) {
          diseaseHistories.add(DiseaseHistoryModel.fromJson(history).obs);
        }
        return diseaseHistories;
      }
    }
  }

  getPatientById(String userId) async {
    Response response = await _apiClient.getPatientByID(userId);
    print(response.data);
    if (response != null) {
      Map data = response.data;
      print('response data: $data');
      if (data["result"] == true) {
        final Map user = data['data'];
        return PatientModel.fromJson(user).obs;
      }
    }
  }
}
