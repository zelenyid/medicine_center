import 'package:flutter/material.dart';
import 'package:get/get.dart';

import '../../routes.dart';

class PatientDrawer extends StatelessWidget {
  const PatientDrawer({
    Key key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: SafeArea(
        child: ListView(
          padding: EdgeInsets.zero,
          children: <Widget>[
            ListTile(
              leading: Icon(Icons.account_circle),
              title: Text('Profile'),
            ),
            ListTile(
              leading: Icon(Icons.medical_services_outlined),
              title: Text('Hospitals'),
              onTap: () => Get.toNamed(Routes.Hospitals),
            ),
            ListTile(
              leading: Icon(Icons.analytics),
              title: Text('Analytics'),
              onTap: () => Get.toNamed(Routes.Analytics),
            ),
          ],
        ),
      ),
    );
  }
}

class DoctorsDrawer extends StatelessWidget {
  const DoctorsDrawer({
    Key key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: SafeArea(
        child: ListView(
          padding: EdgeInsets.zero,
          children: <Widget>[
            ListTile(
              leading: Icon(Icons.account_circle),
              title: Text('Profile'),
            ),
            ListTile(
              leading: Icon(Icons.medical_services_outlined),
              title: Text('Patients'),
              onTap: () => Get.toNamed(Routes.SearchPatient),
            ),
            ListTile(
              leading: Icon(Icons.medical_services_outlined),
              title: Text('Register patient'),
              onTap: () => Get.toNamed(Routes.Register),
            ),
            ListTile(
              leading: Icon(Icons.analytics),
              title: Text('Analytics'),
              onTap: () => Get.toNamed(Routes.Analytics),
            ),
          ],
        ),
      ),
    );
  }
}

class IconTile extends StatelessWidget {
  final IconButton iconButton;
  final Color backColor;

  IconTile({this.iconButton, this.backColor});

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.only(right: 16),
      child: Container(
        height: 45,
        width: 45,
        decoration: BoxDecoration(
            color: backColor, borderRadius: BorderRadius.circular(15)),
        child: iconButton),
    );
  }
}
