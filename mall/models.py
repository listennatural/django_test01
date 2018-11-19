from django.db import models


class Users(models.Model):
    nickname = models.CharField(max_length=255, help_text="昵称")
    account = models.CharField(max_length=255, help_text="账号", unique=True)
    password = models.CharField(max_length=255, help_text="密码")
    status = models.IntegerField(help_text="状态", default=0)
    createtime = models.CharField(max_length=255, help_text="创建时间")


class UserAddress(models.Model):
    user = models.ForeignKey("Users", on_delete=models.CASCADE, help_text="用户")
    name = models.CharField(max_length=255, help_text="联系人姓名")
    phone = models.CharField(max_length=255, help_text="联系人电话")
    national = models.CharField(max_length=255, help_text="国家")
    province = models.CharField(max_length=255, help_text="省")
    city = models.CharField(max_length=255, help_text="市")
    area = models.CharField(max_length=255, help_text="区")
    county = models.CharField(max_length=255, help_text="县/地级市")
    township = models.CharField(max_length=255, help_text="乡/镇")
    address = models.CharField(max_length=255, help_text="具体地址")
    createtime = models.CharField(max_length=255, help_text="创建时间")


class ShopCart(models.Model):
    user = models.ForeignKey("Users", on_delete=models.CASCADE, help_text="用户")
    good = models.ForeignKey("Goods", on_delete=models.CASCADE, help_text="商品")
    now_price = models.FloatField(help_text="添加时的价格")
    createtime = models.CharField(max_length=255, help_text="创建时间")


class UserOrders(models.Model):
    user = models.ForeignKey("Users", on_delete=models.CASCADE, help_text="用户")
    number = models.CharField(max_length=255, help_text="订单号", unique=True)
    status = models.IntegerField(help_text="状态", default=0)
    total_price = models.FloatField(help_text="总价格")
    actual_payment = models.FloatField(help_text="实际支付")
    coupon = models.ForeignKey("Coupons", on_delete=models.CASCADE)
    createtime = models.CharField(max_length=255, help_text="创建时间")


class OrderGoods(models.Model):
    user = models.ForeignKey("Users", on_delete=models.CASCADE, help_text="用户")
    order = models.ForeignKey("UserOrders", on_delete=models.CASCADE, help_text="订单")
    good = models.ForeignKey("Goods", on_delete=models.CASCADE, help_text="商品")
    original_price = models.FloatField(help_text="原价", default=0.00)
    actual_price = models.FloatField(help_text="实际价格")


class Goods(models.Model):
    name = models.CharField(max_length=255, help_text="商品名")
    merchant = models.ForeignKey("Merchants", on_delete=models.SET_NULL, null=True, help_text="商家")
    img = models.CharField(max_length=255, help_text="图片")
    original_price = models.FloatField(help_text="原价", default=0.00)
    actual_price = models.FloatField(help_text="实际价格")
    stock = models.IntegerField(help_text="库存", default=0)
    status = models.IntegerField(help_text="状态", default=0)
    createtime = models.CharField(max_length=255, help_text="创建时间")


class Merchants(models.Model):
    name = models.CharField(max_length=255, help_text="商家名称")
    city = models.CharField(max_length=255, help_text="所在城市")
    level = models.ForeignKey("Levels", on_delete=models.SET_DEFAULT, default=0)
    createtime = models.CharField(max_length=255, help_text="创建时间")


class Levels(models.Model):
    level = models.IntegerField(help_text="等级")
    name = models.CharField(max_length=255, help_text="等级名称")
    devide = models.IntegerField(help_text="抽成")


class Coupons(models.Model):
    name = models.CharField(max_length=255, help_text="优惠券名称")
    deleted = models.IntegerField(help_text="是否删除", default=0)


class Admin(models.Model):
    permission = models.IntegerField(help_text="权限")
    account = models.CharField(max_length=255, help_text="账号", unique=True)
    password = models.CharField(max_length=255, help_text="密码")
    createtime = models.CharField(max_length=255, help_text="创建时间")
