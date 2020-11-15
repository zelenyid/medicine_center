import 'package:flutter/material.dart';
import 'package:medecine_app/ui/appbar/base_appbar.dart';

class PatientScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: BaseAppBar(),
      body: SingleChildScrollView(
        child: Container(
          padding: EdgeInsets.symmetric(horizontal: 24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              buildDoctorHeadInfo(context),
              SizedBox(
                height: 26,
              ),
              Text(
                "About",
                style: TextStyle(fontSize: 22),
              ),
              SizedBox(
                height: 16,
              ),
              Text(
                "Kiyv.",
                style: TextStyle(color: Colors.grey, fontSize: 16),
              ),
              Text(
                "20 years old.",
                style: TextStyle(color: Colors.grey, fontSize: 16),
              ),
              SizedBox(
                height: 24,
              ),
              buildAddress(context),
              buildActivityLayout(context),
              SizedBox(
                width: 16,
              ),
            ],
          ),
        ),
      ),
    );
  }

  Column buildActivityLayout(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Text(
          "Activity",
          style: TextStyle(
            color: Color(0xff242424),
            fontSize: 28,
          ),
        ),
        SizedBox(
          height: 22,
        ),

        Card(
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(20.0),
            ),
            color: Color(0xFF73AEF5),
            child: new InkWell(
              borderRadius: BorderRadius.circular(20),
              onTap: () => print("tapped"),
              child: Container(
                padding: EdgeInsets.symmetric(vertical: 24, horizontal: 16),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    Container(
                        padding: EdgeInsets.all(8),
                        decoration: BoxDecoration(
                            color: Color.fromRGBO(144, 202, 249, 1),
                            borderRadius: BorderRadius.circular(16)),
                        child: Icon(Icons.list_alt)),
                    SizedBox(
                      width: 16,
                    ),
                    Container(
                      width: MediaQuery.of(context).size.width / 2,
                      child: Text(
                        "Disease History",
                        style: TextStyle(color: Colors.white, fontSize: 17),
                      ),
                    )
                  ],
                ),
              ),
            )),
        // )
      ],
    );
  }

  Row buildAddress(BuildContext context) {
    return Row(
      children: <Widget>[
        Column(
          children: <Widget>[
            Row(
              children: <Widget>[
                // Image.asset("assets/mappin.png"),

                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: <Widget>[
                    Row(children: [
                      Text(
                        "Address",
                        style: TextStyle(
                            color: Colors.black87.withOpacity(0.7),
                            fontSize: 20),
                      ),
                      Icon(Icons.location_city),
                      SizedBox(
                        width: 15,
                      ),
                    ]),
                    SizedBox(
                      height: 3,
                    ),
                    Container(
                        width: MediaQuery.of(context).size.width - 268,
                        child: Text(
                          "Bulvar Koltsova 19, Kyiv",
                          style: TextStyle(color: Colors.grey),
                        ))
                  ],
                )
              ],
            ),
            SizedBox(
              height: 20,
            ),
//
          ],
        ),
        Image.asset(
          "assets/map.png",
          width: 180,
        )
      ],
    );
  }

  Row buildDoctorHeadInfo(BuildContext context) {
    return Row(
      children: <Widget>[
        Expanded(
            child: Icon(
          Icons.account_circle,
          size: 100,
        )),
        SizedBox(
          width: 20,
        ),
        Expanded(
          child: Container(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: <Widget>[
                Text(
                  "Nazar Kostetskiy",
                  style: TextStyle(fontSize: 24),
                ),
                Text(
                  "Student",
                  style: TextStyle(fontSize: 18, color: Colors.grey),
                ),
                SizedBox(
                  height: 40,
                ),
                Row(
                  children: <Widget>[
                    IconTile(
                      backColor: Color.fromRGBO(144, 202, 249, 1),
                      iconButton: IconButton(
                          icon: Icon(Icons.email),
                          onPressed: () => print('pressed mail')),
                    ),
                  ],
                )
              ],
            ),
          ),
        )
      ],
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
