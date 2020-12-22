import 'package:get/get.dart';

import 'patient_search_controller.dart';

class PatientScreenSearchBinding implements Bindings {
  @override
  void dependencies() {
    Get.put(PatientSearchController());
  }
}
