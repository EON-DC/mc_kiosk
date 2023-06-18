-- tb_satae 채우기
insert into tb_state(name) VALUES ('Ordered'),
('Preparing'), ('Checking'), ('Prepared'), ('Delivering'), ('TakenOver'), ('Cancelled');

-- tb_location
insert into tb_location(name, description) VALUES ('광주인력개발원점', '가상의 테스트용 지점')

-- tb_menu
insert into tb_menu(classification_id, name, is_morning_service, is_lunch_service, is_full_service
, is_happy_meal, ordinary_price, morning_discount_amount, morning_min_price, lunch_discount_amount, lunch_min_price, is_set)
VALUES ('')

-- tb_classification
insert into tb_classification(name) VALUES ('단품메뉴'), ('세트메뉴'), ('맥런치 세트'), ('해피 스낵'),('사이드'),('디저트'),('맥카페'),('음료'), ('해피밀')