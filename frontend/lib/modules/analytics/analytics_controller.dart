import 'package:dio/dio.dart';
import 'package:get/get.dart';

import 'package:medecine_app/data/repository/analytics_repository.dart';
import 'package:medecine_app/data/models/analytics_model.dart';
import 'package:medecine_app/data/utils/exceptions.dart';


class AnalyticsController extends GetxController {
  AnalyticsRepository _analyticsRepository = Get.find<AnalyticsRepository>();

  final String title = 'Analytics';
  get analyticsModel => _analyticsRepository.analyticsModel;

  @override
  void onInit() {
    super.onInit();
  }

  Future getAnalytics() async {
    try {
      AnalyticsModel analyticsModel = await _analyticsRepository.getAnalytics();
      print('analyticsModel - $analyticsModel');
      if (analyticsModel != null) {
        return analyticsModel;
      } else {
        Get.snackbar(
            'No analytics data', 'Disease histories is absent');
      }
    } on DioError catch (e) {
      Get.snackbar('Error', 'Connection troubles...');
      print('Dio Error: ${e.message}');
    } catch (e) {
      print(e);
    }
  }
}
