import 'dart:io';
import 'package:path/path.dart' as Path;

class JsonFile {
  String _pathJson = "data.json";

  JsonFile._();

  static final JsonFile _instance = JsonFile._();
  factory JsonFile() => _instance;

  set pathToSave(String name) {
    _pathJson = "$name.json";
  }

  String get pathToSave => _pathJson;

  Future<String> saveContent(String content) async {
    final fileJson = File(pathToSave);

    await fileJson.writeAsString(content);

    return Path.absolute(fileJson.path);
  }
}
