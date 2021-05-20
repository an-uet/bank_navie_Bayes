# bank_navie_Bayes
bank navie bayes
sử dụng mô hình Navie Bayes để xác định khách hàng X có khả năng đăng ký một khoản tiền gửi có kỳ hạn (biến y) hay không?

dữ liệu tham khảo tại :http://archive.ics.uci.edu/ml/datasets/Bank+Marketing
dữ liệu gồm 17 trường sau :
1: age
2: job : 'admin','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown'
3: marital: 'divorced','married','single','unknown'
4. education: 'basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown'
5. default( có nợ tín dụng hay không) :'no','yes','unknown'
6. balance : số dư tài khoản.
7. housing( có khoản vay mua nhà hay không): 'no','yes','unknown'
8. loan( có khoản vay cá nhân hay không):'no','yes','unknown'
9. contact: hình thức liên hệ 'cellular','telephone','unknown'
10. day: ngày liên hệ
11. month: tháng liên hệ
12. duration: độ dài cuộc gọi, tính bằng giây
13. campaign: số lần liên hệ
14. pdays: số ngày trôi qua tính từ lần liên lạc cuối với khách hàng
15. previous: số lần liên hệ cho khách hàng này trong những chiến dịch marketing trước
16. poutcome: kết quả của chiến dịch marketing trước đó : 'failure','nonexistent','success','other' 
17. y : khách hàng đã đăng ký tiền gửi có kỳ hạn chưa? 


sử dụng mô hình navie bayes tính và so sánh
p(yes/X) và p(no/X) => đưa ra kết luận khách hàng ấy có tiềm năng hay không.