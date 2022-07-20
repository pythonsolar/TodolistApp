import 'package:flutter/material.dart';

// import 'dart:convert';
import 'package:http/http.dart' as http;
import 'dart:async';

class UpdatePage extends StatefulWidget {
  final v1, v2, v3;
  const UpdatePage(this.v1, this.v2, this.v3);

  @override
  State<UpdatePage> createState() => _UpdatePageState();
}

class _UpdatePageState extends State<UpdatePage> {
  var _v1, _v2, _v3;
  TextEditingController todo_title = TextEditingController();
  TextEditingController todo_detail = TextEditingController();

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    _v1 = widget.v1;
    _v2 = widget.v2;
    _v3 = widget.v3;
    todo_title.text = _v2;
    todo_detail.text = _v3;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('แก้ไข'),
          actions: [
            IconButton(
                onPressed: () {
                  print("Delete ID: $_v1");
                  deleteTodo();
                  Navigator.pop(context);
                },
                icon: Icon(
                  Icons.delete,
                  color: Colors.red,
                ))
          ],
        ),
        body: Padding(
          padding: const EdgeInsets.all(10.0),
          child: ListView(
            children: [
              TextField(
                controller: todo_title,
                decoration: InputDecoration(
                    labelText: 'รายการ', border: OutlineInputBorder()),
              ),
              SizedBox(height: 20),
              TextField(
                minLines: 4,
                maxLines: 8,
                controller: todo_detail,
                decoration: InputDecoration(
                    labelText: 'รายละเอียด', border: OutlineInputBorder()),
              ),
              SizedBox(height: 20),
              Padding(
                padding: const EdgeInsets.all(20.0),
                child: ElevatedButton(
                  onPressed: () {
                    print('-------------');
                    print('title: ${todo_title.text}');
                    print('detail: ${todo_detail.text}');
                    updateTodo();
                    final snackBar =
                        SnackBar(content: const Text('อัพเดทเรียบร้อยแล้ว'));
                    ScaffoldMessenger.of(context).showSnackBar(snackBar);
                  },
                  child: Text("แก้ไข"),
                  style: ButtonStyle(
                      backgroundColor: MaterialStateProperty.all(Colors.blue),
                      padding: MaterialStateProperty.all(
                          EdgeInsets.fromLTRB(20, 10, 20, 10)),
                      textStyle:
                          MaterialStateProperty.all(TextStyle(fontSize: 30))),
                ),
              ),
            ],
          ),
        ));
  }

  Future updateTodo() async {
    // var url = Uri.https('b823-49-230-60-225.ap.ngrok.io', '/api/post-todolist');
    var url = Uri.http('192.168.1.27:8000', '/api/update-todolist/$_v1');
    Map<String, String> header = {"Content-type": "application/json"};
    String jsondata =
        '{"title":"${todo_title.text}","detail":"${todo_detail.text}"}';
    var response = await http.put(url, headers: header, body: jsondata);
    print('----------result-----------');
    print(response.body);
  }

  Future deleteTodo() async {
    // var url = Uri.http('172.20.10.3:8000', '/api/delete-todolist/$_v1');
    var url = Uri.http('192.168.1.27:8000', '/api/post-todolist');
    Map<String, String> header = {"Content-type": "application/json"};
    var response = await http.delete(url, headers: header);
    print('----------result-----------');
    print(response.body);
  }
}
