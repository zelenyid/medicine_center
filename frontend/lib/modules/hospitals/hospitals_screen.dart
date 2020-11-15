import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:medecine_app/routes.dart';
import 'package:medecine_app/ui/appbar/base_appbar.dart';

class HospitalsScreen extends StatelessWidget {
  final hospitalsData = [
    {
      'name': 'Hospital №3',
      'address': 'Symerenka street 10, Kiyv',
      'image': 'assets/hospital3.jpg'
    },
    {
      'name': 'Hospital №5',
      'address': 'Bulvar Lesi Ukrainky 102, Kiyv',
      'image': 'assets/hospital4.jpg'
      // 'image': 'assets/doctp.jpg'
    },
    {
      'name': 'Hospital №10',
      'address': 'Bulvar Tarasa Schevchenka 7, Kiyv',
      'image': 'assets/hospital5.jpg'
    },
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: BaseAppBar(),
        body: ListView.builder(
            itemCount: hospitalsData.length,
            itemBuilder: (context, index) {
              return Card(
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(20.0),
                  ),
                  child: new InkWell(
                      onTap: () => Get.toNamed(Routes.Doctor),
                      child: Row(children: [
                        Padding(
                            padding: EdgeInsets.only(left: 10),
                            child: Image.asset(
                              hospitalsData[index]['image'],
                              height: 220,
                              width: 150,
                            )),
                        Column(children: [
                          Text(hospitalsData[index]['name']),
                          Text(
                            hospitalsData[index]['address'],
                            overflow: TextOverflow.ellipsis,
                          )
                        ])
                      ])));
            }));
  }
}
