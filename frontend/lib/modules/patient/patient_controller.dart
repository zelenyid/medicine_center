import 'dart:io';

import 'package:dio/dio.dart';
import 'package:get/get.dart';
import 'package:medecine_app/data/models/patient_model.dart';
import 'package:medecine_app/data/repository/patient_repository.dart';
import 'package:medecine_app/data/repository/user_repository.dart';
import 'package:file_picker/file_picker.dart';

// import 'package:medecine_app/data/utils/exceptions.dart';

class PatientController extends GetxController {
  UserRepository userRepository = Get.find<UserRepository>();
  PatientRepository _patientRepository = Get.find<PatientRepository>();

  final String title = 'Login';
  Rx<PatientModel> userModel = PatientModel().obs;
  get diseaseHistories => _patientRepository.diseaseHistories;

  @override
  void onInit() async {
    super.onInit();
    print('params: ${Get.parameters['userId']}');
    await patientById(Get.parameters['userId']);
    await _patientRepository.getDiseaseHistoryByUserId(userModel?.value?.id);
  }

  Future patientById(String userId) async {
    Rx<PatientModel> res = await _patientRepository.getPatientById(userId);
    print('res:${res.toJson()}');
    if (res != null) {
      userModel?.value = res.value;
      print('email: ${res?.value?.email}');
      userModel?.refresh();
      print('user model: ${userModel.value.name}');

      return userModel;
    }
  }

  uploadFile(String historyId) async {
    FilePickerResult result = await FilePicker.platform.pickFiles(
      type: FileType.custom,
      allowedExtensions: ['pdf', 'doc'],
    );

    if (result != null) {
      print(result.files);
      PlatformFile ourFile = result.files.first;
      print(ourFile.extension);
      Response response = GetPlatform.isWeb
          ? await _patientRepository.uploadHistoryFile(historyId,
              bytes: ourFile.bytes, extention: ourFile.extension)
          : await _patientRepository.uploadHistoryFile(historyId,
              filePath: File(ourFile.path).path);
      if (response.statusCode == 200) {
        if (response.data['result'] == true) {
          Get.snackbar('Success', 'File downloaded');
        } else {
          Get.snackbar('Fail', response.data['description']);
        }
      }
    } else {
      // User canceled the picker
    }
  }

  downloadHistoryFile(String historyId) async {
    await _patientRepository.downloadHistoryFile(historyId);
  }

  // Future<UserModel> login(String email, String password) async {
  //   try {
  //     UserModel userModel = await _userRepository.login(email, password);
  //     if (userModel != null) {
  //       return userModel;
  //     } else {
  //       Get.snackbar(
  //           'Invalid credentials', 'Please enter correct email and password');
  //     }
  //   } on NotAuthorizedException catch (e) {
  //     print(e.message);
  //     Get.snackbar('Session expired', 'Login to your account');
  //   } catch (e) {
  //     if (e is DioError) {
  //       Get.snackbar('Error', 'Connection troubles...');
  //       print('Dio Error: ${e.message}');
  //     }
  //     // print(e.message);
  //   }
  // }
}
