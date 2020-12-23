import 'package:flutter/material.dart';
// import 'package:flutter/rendering.dart';
import 'package:flutter_icons/flutter_icons.dart';
import 'package:get/get.dart';
import 'package:graphic/graphic.dart' as graphic;
import 'package:medecine_app/ui/appbar/base_appbar.dart';
import 'package:medecine_app/ui/drawer/base_drawer.dart';
import 'package:medecine_app/data/models/analytics_model.dart';

import 'analytics_controller.dart';


class AnalyticsScreen extends GetView<AnalyticsController> {
  Map<String, dynamic> _statusCount;
  Map<String, dynamic> _illnessCount;
  List<Map<String, dynamic>> illnessesData = [];
  List<Map<String, dynamic>> statusesData = [];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // appBar: BaseAppBar(),
      // endDrawer: BaseDrawer(),
      body: SingleChildScrollView(
        child: Center(
          child: _getAnalyticsContent(),
        ),
      ),
    );
  }

  Widget _getAnalyticsContent() {
    return FutureBuilder(
      future: controller.getAnalytics(),
      builder: (context, snapshot) {
        return (snapshot.connectionState == ConnectionState.waiting)
          ? CircularProgressIndicator()
          : _analyticsContent();
      },
    );
  }

  Widget _analyticsContent() {
    return Column(
      children: <Widget>[
        Padding(
          child: Text('Analytics', style: TextStyle(fontSize: 25)),
          padding: EdgeInsets.fromLTRB(0, 40, 0, 0),
        ),
        SizedBox(
          height: 16,
        ),
        Padding(
          child: Text('Illnesses (Radius Rect)', style: TextStyle(fontSize: 20)),
          padding: EdgeInsets.fromLTRB(0, 40, 0, 0),
        ),
        Container(
          width: 350,
          height: 300,
          child: Obx(() {
            print('controller.analyticsModel?.value: ${controller.analyticsModel?.value}');

            _illnessCount = controller.analyticsModel?.value?.illnessCount;
            print('controller.analyticsModel?.value?._illnessCount: ${controller.analyticsModel?.value?.illnessCount}');
            List<Map<String, dynamic>> illnessesData = [];
            _illnessCount?.forEach((illness, count) =>
                illnessesData.add({
                  'illness': illness,
                  'count': count,
                })
            );
            return illnessesData.isEmpty
              ? _noDataText('illness')
              : graphic.Chart(
                  data: illnessesData,
                  scales: {
                    'illness': graphic.CatScale(
                      accessor: (map) => map['illness'] as String,
                    ),
                    'count': graphic.LinearScale(
                      accessor: (map) => map['count'] as num,
                      nice: true,
                    )
                  },
                  geoms: [graphic.IntervalGeom(
                    position: graphic.PositionAttr(field: 'illness*count'),
                    shape: graphic.ShapeAttr(values: [
                      graphic.RectShape(radius: Radius.circular(5))
                    ]),
                  )],
                  axes: {
                    'illness': graphic.Defaults.horizontalAxis,
                    'count': graphic.Defaults.verticalAxis,
                  },
                );
          }),
        ),

        Padding(
          child: Text('Statuses (Bublik Graph)', style: TextStyle(fontSize: 20)),
          padding: EdgeInsets.fromLTRB(0, 40, 0, 0),
        ),
        Container(
          width: 350,
          height: 300,
          child: Obx(() {
            _statusCount = controller.analyticsModel?.value?.statusCount;
            print('controller.analyticsModel?.value?._statusCount: ${controller.analyticsModel?.value?.statusCount}');
            
            _statusCount?.forEach((status, count) =>
                statusesData.add({
                  'status': status,
                  'count': count,
                })
            );
            return graphic.Chart(
              data: statusesData,
              scales: {
                'status': graphic.CatScale(
                  accessor: (map) => map['status'] as String,
                ),
                'count': graphic.LinearScale(
                  accessor: (map) => map['count'] as num,
                  nice: true,
                )
              },
              coord: graphic.PolarCoord(transposed: true, innerRadius: 0.5),
              geoms: [graphic.IntervalGeom(
                position: graphic.PositionAttr(field: 'status*count'),
                color: graphic.ColorAttr(field: 'status'),
              )],
              padding: EdgeInsets.zero,
              margin: EdgeInsets.all(20),
            );
          }),
        ),

        // Padding(
        //   child: Text('Statuses (Polar Coord)', style: TextStyle(fontSize: 20)),
        //   padding: EdgeInsets.fromLTRB(0, 40, 0, 0),
        // ),
        // Container(
        //   width: 350,
        //   height: 300,
        //   child: Obx(() {
        //     _statusCount = controller.analyticsModel?.value?.statusCount;
        //     print('controller.analyticsModel?.value?._statusCount: ${controller.analyticsModel?.value?.statusCount}');
            
        //     _statusCount?.forEach((status, count) =>
        //         statusesData.add({
        //           'status': status,
        //           'count': count,
        //         })
        //     );
        //     return statusesData.isEmpty
        //       ? _noDataText('status')
        //       : graphic.Chart(
        //           data: statusesData,
        //           scales: {
        //             'status': graphic.CatScale(
        //               accessor: (map) => map['status'] as String,
        //             ),
        //             'count': graphic.LinearScale(
        //               accessor: (map) => map['count'] as num,
        //               nice: true,
        //             )
        //           },
        //           coord: graphic.PolarCoord(),
        //           geoms: [graphic.IntervalGeom(
        //             position: graphic.PositionAttr(field: 'status*count'),
        //             color: graphic.ColorAttr(field: 'status'),
        //           )],
        //           axes: {
        //             'status': graphic.Defaults.circularAxis,
        //             'count': graphic.Defaults.radialAxis
        //               ..label = null,
        //           },
        //         );
        //   }),
        // ),
        Obx(() => Column(
            children: _statusesTextList(
              controller.analyticsModel?.value?.statusCount
            )
          ),
        ),
      ],
    );
  }

  List<Widget> _statusesTextList(Map statusMap) {
    List<Widget> _statusesList = [];
        
    statusMap?.forEach((status, count) =>
        _statusesList.add(
          Padding(
            child: Text(
              '$status: $count',
              style: TextStyle(
                fontSize: 15, fontWeight: FontWeight.bold
              )
            ),
            padding: EdgeInsets.fromLTRB(0, 2, 0, 6),
          )
        )
    );
    return _statusesList;
  }

  Widget _noDataText(String param) {
    return Center(
      child: Text('No analytic $param data'),
    );
  }
}
