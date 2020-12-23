import 'package:dio/dio.dart';
import 'package:get/get.dart';
import 'package:medecine_app/data/models/analytics_model.dart';
import 'package:medecine_app/data/provider/api.dart';


class AnalyticsRepository extends GetxService {
  ApiClient _apiClient = Get.find<ApiClient>();
  Rx analyticsModel = null.obs;

  Future getAnalytics() async {
    Response response = await _apiClient.getAnalytics();
    
    if (response != null) {
      this.analyticsModel = AnalyticsModel.fromJson(response.data).obs;
      return analyticsModel;
    }
  }
}
