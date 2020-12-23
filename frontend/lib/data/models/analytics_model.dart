class AnalyticsModel {
  Map<String, dynamic> illnessCount;
  Map<String, dynamic> statusCount;

  AnalyticsModel(this.illnessCount, this.statusCount);

  factory AnalyticsModel.fromJson(Map json) {
    final illnessCount = json['illness_count'];
    print('illness_count $illnessCount');
    final statusCount = json['status_count'];
    print('status_count $statusCount');
    return AnalyticsModel(illnessCount, statusCount);
  }
}
