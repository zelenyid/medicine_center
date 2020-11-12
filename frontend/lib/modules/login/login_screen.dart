import 'package:flutter/material.dart';
import 'package:get/get.dart';

import 'login_controller.dart';

class LoginScreen  extends GetView<LoginController>{
  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: Text('Login')),body: Column(children: [Text('Some login form'), Text(controller.title)]),);
  }
  
  
}