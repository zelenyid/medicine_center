import 'dart:async';

import 'package:dio/dio.dart';
import 'package:medecine_app/data/utils/exceptions.dart';

const String baseUrl = 'http://34.89.129.235/';

enum http_method { GET, POST }

class ApiClient {
  static BaseOptions _baseOptions = BaseOptions(
      baseUrl: baseUrl,
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
      },
      connectTimeout: 10000,
      validateStatus: (status) {
        return status < 500;
      });
  final Dio _dio = Dio(_baseOptions);

  String _accessToken;
  String _refreshToken;
  // Todo: get access token from some store
  get accessToken => _accessToken;
  get refreshToken => _refreshToken;

  get authHeaderOptions => Options(headers: <String, String>{
        'Authorization': 'Authorization-Token $accessToken'
      });
  get refreshHeaderOptions => Options(headers: <String, String>{
        'Authorization': 'Authorization-Token $refreshToken'
      });

  Future login(email, password) async {
    Response response = await _dio.post(
      '/login',
      data: {'email': email, 'password': password},
    );
    if (response.statusCode == 200) {
      print(response.data);
      if (response.data["result"] == true) {
        final access = response.data['access_token'];
        final refresh = response.data['refresh_token'];
        if (access != null && refresh != null) {
          this._accessToken = access;
          this._refreshToken = refresh;
          return response;
        }
      }
    }
  }

  Future _authenticatedRequest(path,
      {method = http_method.POST, data = const {}}) async {
    Function request;
    if (method == http_method.GET) {
      request = () => _dio.get(path, options: authHeaderOptions);
    } else if (method == http_method.POST) {
      request = () => _dio.post(path, data: data, options: authHeaderOptions);
    }
    print(accessToken);
    print('refresh : $_refreshToken');
    Response response = await request();
    if (response.statusCode == 200) {
      return response;
    }
    // If access token is not fresh
    else if (response.statusCode == 401 || response.statusCode == 422) {
      // Trying to refresh tokens and send request again
      Response response = await refreshTokens();
      if (response.statusCode == 200) {
        return await request();
      } else {
        print('GO TO LOGIN');
        throw NotAuthorizedException();
      }
    }
  }

  Future protected() async {
    return await _authenticatedRequest('/protected',
        data: {}, method: http_method.GET);
  }

  Future refreshTokens() async {
    Response response =
        await _dio.get('/auth/refresh', options: refreshHeaderOptions);
    if (response.statusCode == 200) {
      if (response.data["result"] == true) {
        final access = response.data['access_token'];
        final refresh = response.data['refresh_token'];
        if (access != null && refresh != null) {
          this._accessToken = access;
          this._refreshToken = refresh;
        }
      }
    }
    return response;
  }
}

main() async {
  final apiClient = ApiClient();
  Response response = await apiClient.login('test', 'test');
  print(response.data);
  response = await apiClient.protected();
  print(response?.data);
  Timer(Duration(seconds: 40), () async => print(await apiClient.protected()));
  Timer(Duration(seconds: 61 + 40),
      () async => print(await apiClient.protected()));
}
