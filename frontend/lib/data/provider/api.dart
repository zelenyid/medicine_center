


import 'package:dio/dio.dart';

const String baseUrl = 'http://127.0.0.1:8000';

enum http_method {GET, POST}

class ApiClient{
  static BaseOptions _baseOptions = BaseOptions(baseUrl: baseUrl, headers: {"Accept": "application/json",
      "Content-Type": "application/json",  "Access-Control-Allow-Origin": "*"}, connectTimeout: 10, validateStatus: (status) { return status < 500; });
  final Dio _dio = Dio(_baseOptions);

  String _accessToken;
  String _refreshToken;
  // Todo: get access token from some store
  get accessToken => _accessToken;
  get refreshToken => _refreshToken;

  get authHeaderOptions => Options(headers: <String, String>{'Authorization': 'Authorization-Token $accessToken'});
  get refreshHeaderOptions => Options(headers: <String, String>{'Authorization': 'Authorization-Token $refreshToken'});
  

  Future login(email, password) async {
    try{
      Response response = await _dio.post('/login', data: {'email': email, 'password': password},
    );
       if(response.statusCode==200){
        print(response.data);
        if(response.data["result"]==true){
          final access = response.data['access_token'];
          final refresh = response.data['refresh_token'];
          if(access!=null && refresh!=null){
            this._accessToken = access;
            this._refreshToken = refresh;
            return response;  
          }
        }
      }
    }
    catch(e){
      print(e);
    }
  }

  Future _authenticatedRequest(path, {method = http_method.POST, data = const {}}) async {
    Function request;
    if(method==http_method.GET){
      request = () => _dio.get(path, options: authHeaderOptions);
    } 
    else if(method==http_method.POST){
      request = () => _dio.post(path, data:data, options: authHeaderOptions);
    }

    try{
      Response response = await request();
      if(response.statusCode==200){
        return response;
      }
      // If access token is not fresh
      else if(response.statusCode==401){
        // Trying to refresh tokens and send request again
        Response response = await refreshTokens();
        if(response.statusCode==200){
          return await request();
        }
        else{
          // Go to login
        }
      }
    }
    catch(e){
      print(e);
    }
  }

  Future protected() async {
    await _authenticatedRequest('/protected', data: {});
  }


  Future refreshTokens() async {
    try{
      Response response = await _dio.get('/auth/refresh', options: refreshHeaderOptions);
      if(response.statusCode==200){
        if(response.data["result"]==true){
          final access = response.data['access_token'];
          final refresh = response.data['refresh_token'];
          if(access!=null && refresh!=null){
            this._accessToken = access;
            this._refreshToken = refresh;
          }
        }
      }
      return response;
    }
    catch(e){
      print(e);
    }
  }
}
