class AnalyticsModel {
  Map<String, int> illnessCount;
  Map<String, int> statusCount;

  AnalyticsModel(this.illnessCount, this.statusCount);

  factory AnalyticsModel.fromJson(Map json) {
    final illnessCount = json['illness_count'];
    final statusCount = json['status_count'];
    return AnalyticsModel(illnessCount, statusCount);
  }
}
