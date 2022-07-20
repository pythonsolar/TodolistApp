from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TodolistSerializer
from .models import Todolist

@api_view(['GET'])
def all_todolist(request):
    alltodolist = Todolist.objects.all()
    serializer = TodolistSerializer(alltodolist,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def post_todolist(request):
    if request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_todolist(request,TID):
    todo = Todolist.objects.get(id=TID)

    if request.method == 'PUT':
        data = {}
        serializer = TodolistSerializer(todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'updated'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_todolist(request,TID):
    todo = Todolist.objects.get(id=TID)

    if request.method == 'DELETE':
        delete = todo.delete()
        data = {}
        if delete:
            data['status'] = 'deleted'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST
        return Response(data=data, status=statuscode)




data = [
    {
        "title":"อินเวอร์เตอร์ คืออะไร?",
        "subtitle":"คอมพิวเตอร์ คือ อุปกรณ์ที่ใช้สำหรับการคำนวณและทำงานอื่นๆ?",
        "image_url":"https://raw.githubusercontent.com/pythonsolar/BasicAPI/main/home-office-1867761_960_720.jpg",
        "detail":"การเดินทางตลอดหนึ่งปีที่ผ่านมา เราต้องเจอกับเรื่องราวมากมาย เผชิญหน้ากับเหตุการณ์ไม่คาดคิด และรับมือกับหลายความรู้สึกที่เกาะกุมอยู่ในใจ \n\nด้วยเหตุนี้ ยิ่งใกล้ช่วงท้ายปี หลายคนเลยอยากปล่อยให้ ‘ปีเก่า’ เป็นเรื่องราวของ ‘ปีเก่า’ พร้อมทิ้งเรื่องราวเดิมๆ ไว้ข้างหลังและมุ่งหน้าสู่การเดินทางใหม่ที่กำลังจะมาถึงแต่แทนที่จะโยนทิ้งและปล่อยให้เป็นเรื่องราวในอดีตเฉยๆ อย่าลืมว่าจริงๆ แล้วการเดินทางอันยาวนานตลอด 1 ปีที่ผ่านมาให้อะไรเรามากมาย  มาร่วมส่งท้ายปีเก่าด้วยการรู้จักตัวเอง ย้อนมองบทเรียน และรับกำลังใจดีๆ ผ่าน 12 บทความให้กำลังใจจาก Mission To The Moon"
    },
    {
        "title":"ชาร์จเจอร์ คืออะไร?",
        "subtitle":"บทความนี้จะแนะนำการเริ่มต้นเขียนโปรแกรม",
        "image_url":"https://raw.githubusercontent.com/pythonsolar/BasicAPI/main/bluiding-office-1867761_960_720.jpg",
        "detail":"เชื่อว่าเราหลายคนเคยมีทุกอย่างพอ.. แล้วหลงคิดว่าไม่พอ ดิ้นรน ไขว่คว้า อาจได้สิ่งหนึ่งมา แต่ก็เสียสิ่งอื่น หรือสิ่งที่เคยมีไป แล้วก็มีที่ไม่ได้ดิ้นรนไขว่คว้า ไม่ได้พยายามเปลี่ยนแปลงอะไร แต่ก็รักษาสิ่งที่มีไว้ไม่ได้เหมือนกัน"
    },
    {
        "title":"Python คือ?",
        "subtitle":"Tools สำหรับออกแบบ UI ของ Google",
        "image_url":"https://raw.githubusercontent.com/pythonsolar/BasicAPI/main/phone-292994_960_720.jpg",
        "detail":"การที่เรารู้สึกดี อยู่ในอารมณ์พึงพอใจอย่างที่สุด ไม่ว่าการได้เป็นที่รัก เป็นที่ยอมรับ หรือแค่มีจิตอันแจ่มใส เหล่านี้ล้วนเกิดทาง จิตใจ"
    },
    {
        "title":"ลูกชาวนาครับาผม",
        "subtitle":"บทความนี้จะแนะนำการเริ่มต้นเขียนโปรแกรม",
        "image_url":"https://raw.githubusercontent.com/pythonsolar/BasicAPI/main/bluiding-office-1867761_960_720.jpg",
        "detail":"เชื่อว่าเราหลายคนเคยมีทุกอย่างพอ.. แล้วหลงคิดว่าไม่พอ ดิ้นรน ไขว่คว้า อาจได้สิ่งหนึ่งมา แต่ก็เสียสิ่งอื่น หรือสิ่งที่เคยมีไป แล้วก็มีที่ไม่ได้ดิ้นรนไขว่คว้า ไม่ได้พยายามเปลี่ยนแปลงอะไร แต่ก็รักษาสิ่งที่มีไว้ไม่ได้เหมือนกัน"
    },
    {
        "title":"แผงโซล่าเซลล์คืออะไร?",
        "subtitle":"คอมพิวเตอร์ คือ อุปกรณ์ที่ใช้สำหรับการคำนวณและทำงานอื่นๆ?",
        "image_url":"https://raw.githubusercontent.com/pythonsolar/BasicAPI/main/home-office-1867761_960_720.jpg",
        "detail":"การเดินทางตลอดหนึ่งปีที่ผ่านมา เราต้องเจอกับเรื่องราวมากมาย เผชิญหน้ากับเหตุการณ์ไม่คาดคิด และรับมือกับหลายความรู้สึกที่เกาะกุมอยู่ในใจ \n\nด้วยเหตุนี้ ยิ่งใกล้ช่วงท้ายปี หลายคนเลยอยากปล่อยให้ ‘ปีเก่า’ เป็นเรื่องราวของ ‘ปีเก่า’ พร้อมทิ้งเรื่องราวเดิมๆ ไว้ข้างหลังและมุ่งหน้าสู่การเดินทางใหม่ที่กำลังจะมาถึงแต่แทนที่จะโยนทิ้งและปล่อยให้เป็นเรื่องราวในอดีตเฉยๆ อย่าลืมว่าจริงๆ แล้วการเดินทางอันยาวนานตลอด 1 ปีที่ผ่านมาให้อะไรเรามากมาย  มาร่วมส่งท้ายปีเก่าด้วยการรู้จักตัวเอง ย้อนมองบทเรียน และรับกำลังใจดีๆ ผ่าน 12 บทความให้กำลังใจจาก Mission To The Moon"
    }
]

def Home(request):
    return JsonResponse(data=data,safe=False,json_dumps_params={'ensure_ascii':False})