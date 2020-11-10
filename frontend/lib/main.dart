import 'package:flutter/material.dart';
import 'package:get/get.dart';

void main() {
  runApp(
    GetMaterialApp(
        debugShowCheckedModeBanner: false,
        initialRoute: '/',
        // theme: appThemeData,
        defaultTransition: Transition.fade,
        // getPages: AppPages.pages,
        home: HomePage(),
            )
          );
        }
        
class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar:AppBar(title:Text('Medecine app')),
      body: Column(children: <Widget>[Text('Medecine application')]));
  }
}

