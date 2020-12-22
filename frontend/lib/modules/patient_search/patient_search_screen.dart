import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:medecine_app/data/models/patient_model.dart';
import 'package:medecine_app/data/repository/user_repository.dart';
import 'package:medecine_app/ui/appbar/base_appbar.dart';
import 'package:medecine_app/ui/drawer/base_drawer.dart';
import 'package:medecine_app/ui/styles.dart';

import '../../routes.dart';
import 'patient_search_controller.dart';

class PatientSaerchScreen extends GetView<PatientSearchController> {
  final TextEditingController searchingNameController = TextEditingController();
  final TextEditingController searchingSurnameController =
      TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: BaseAppBar(title: 'Search Patient'),
        // endDrawer: Get.find<UserRepository>().userModel.value.runtimeType ==
        //         PatientModel
        //     ? PatientDrawer()
        //     : DoctorsDrawer(),
        body: Padding(
            padding: EdgeInsets.all(18),
            child: Column(children: [
              buildNameFilterTextInput(),
              buildSurnameFilterTextInput(),
              buildSearchButton(),
              Obx(() => Expanded(
                  child: ListView.builder(
                      itemCount: controller.searchResult.length,
                      itemBuilder: (context, index) {
                        return Padding(
                            padding: EdgeInsets.all(10),
                            child: Card(
                                shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(20.0),
                                ),
                                child: new InkWell(
                                    onTap: () => Get.toNamed(
                                        Routes.Patient.replaceFirst(
                                            ':userId',
                                            controller
                                                .searchResult[index]?.userId)),
                                    child: Row(children: [
                                      Padding(
                                          padding: EdgeInsets.only(left: 10),
                                          child: Icon(Icons.account_box)),
                                      Expanded(
                                          child: Container(
                                              child: Column(children: [
                                        Text(
                                          controller
                                                  .searchResult[index]?.name ??
                                              '',
                                          overflow: TextOverflow.visible,
                                        ),
                                        Text(
                                          controller.searchResult[index]
                                                  ?.address ??
                                              '',
                                          overflow: TextOverflow.visible,
                                        )
                                      ])))
                                    ]))));
                      })))
            ])));
  }

  Row buildNameFilterTextInput() {
    return Row(children: [
      Text(
        'Name',
        style: kLabelStyleBlack,
      ),
      SizedBox(width: 10.0),
      Expanded(
          child: SizedBox(
              width: 400,
              child: TextFormField(
                textInputAction: TextInputAction.next,
                controller: searchingNameController,
                style: TextStyle(
                  fontFamily: 'OpenSans',
                  color: Colors.black,
                ),
                decoration: InputDecoration(
                  border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(5.0),
                      borderSide: BorderSide(
                        color: Colors.amber,
                        style: BorderStyle.solid,
                      )),
                  contentPadding: EdgeInsets.only(top: 14.0),
                  hintText: 'Enter name',
                  hintStyle: kHintTextStyle,
                ),
              )))
    ]);
  }

  buildSearchButton() {
    return RaisedButton(
        onPressed: () => controller.searchPatient(
              searchingNameController.text,
              searchingSurnameController.text,
            ),
        child: Text('Search patient'));
  }

  buildSurnameFilterTextInput() {
    return Row(children: [
      Text(
        'Surname',
        style: kLabelStyleBlack,
      ),
      SizedBox(width: 10.0),
      Expanded(
          child: SizedBox(
              width: 400,
              child: TextFormField(
                textInputAction: TextInputAction.next,
                controller: searchingSurnameController,
                style: TextStyle(
                  fontFamily: 'OpenSans',
                  color: Colors.black,
                ),
                decoration: InputDecoration(
                  border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(5.0),
                      borderSide: BorderSide(
                        color: Colors.amber,
                        style: BorderStyle.solid,
                      )),
                  contentPadding: EdgeInsets.only(top: 14.0),
                  hintText: 'Enter name',
                  hintStyle: kHintTextStyle,
                ),
              )))
    ]);
  }
}
