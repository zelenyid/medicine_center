import 'package:get/get.dart';
import 'analytics_controller.dart';

class AnalyticsBinding implements Bindings {
  @override
  void dependencies() {
    Get.put(AnalyticsController());
  }
}
