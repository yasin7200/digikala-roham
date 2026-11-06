
from django.contrib import admin
from .models import *


# نمایش تصاویر در صفحه محصول
class ImageProductInline(admin.TabularInline):
    model = ImageProduct
    extra = 1
    fields = ("image",)
    show_change_link = True


# تنظیمات مشترک تمام محصولات
class BaseProductAdmin(admin.ModelAdmin):
    inlines = [ImageProductInline]

    list_display = (
        "id",
        "title",
        "brand",
        "price",
        "discount",
        "counts",
    )

    list_filter = ("brand", "category")
    search_fields = ("title", "brand", "seller")
    prepopulated_fields = {"slug": ("title",)}
    list_per_page = 20


# دسته‌بندی
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)


# محصول اصلی
@admin.register(Product)
class ProductAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "brand", "category",
        "price", "discount", "counts", "seller"
    )
    list_editable = ("price", "discount", "counts")


# محصولات تخصصی
@admin.register(Phone)
class PhoneAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "brand", "model",
        "ram", "internal_storage", "price"
    )
    list_filter = ("brand", "os")


@admin.register(Tablet)
class TabletAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "brand", "model",
        "screen_size", "has_pen", "price"
    )
    list_filter = ("brand", "has_pen", "cellular")


@admin.register(PC)
class PCAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "brand", "cpu",
        "ram", "gpu", "price"
    )
    list_filter = ("brand", "ram_type", "storage_type")


@admin.register(Monitor)
class MonitorAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "brand", "screen_size",
        "screen_resolution", "refresh_rate", "price"
    )
    list_filter = ("brand", "panel_type")


@admin.register(Laptop)
class LaptopAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "brand", "cpu",
        "ram", "screen_size", "price"
    )
    list_filter = ("brand", "touchscreen", "convertible")


@admin.register(GamingLaptop)
class GamingLaptopAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "brand", "dedicated_gpu",
        "cpu", "ram", "price"
    )
    list_filter = ("brand", "rgb_keyboard", "mux_switch")


@admin.register(Headphones)
class HeadphonesAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "brand", "model",
        "connection_type", "price"
    )
    list_filter = ("brand", "connection_type", "noise_cancellation")


@admin.register(Modem)
class ModemAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "brand", "model",
        "modem_type", "wifi_standard", "price"
    )
    list_filter = ("brand", "modem_type", "sim_support")


@admin.register(FlashDrive)
class FlashDriveAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "brand", "capacity",
        "interface", "read_speed", "price"
    )
    list_filter = ("brand", "interface", "waterproof")


@admin.register(HardDrive)
class HardDriveAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "brand", "capacity",
        "interface", "form_factor", "price"
    )
    list_filter = ("brand", "interface", "form_factor")


@admin.register(HDD)
class HDDAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "brand", "capacity",
        "rpm", "form_factor", "price"
    )
    list_filter = ("brand", "rpm")


@admin.register(SSD)
class SSDAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "brand", "capacity",
        "nand_type", "read_speed", "price"
    )
    list_filter = ("brand", "nand_type", "pcie_generation")


@admin.register(ExternalHardDrive)
class ExternalHardDriveAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "brand", "capacity",
        "drive_type", "connection", "price"
    )
    list_filter = ("brand", "drive_type", "portable")


@admin.register(NVMeSSD)
class NVMeSSDAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "brand", "capacity",
        "read_speed", "heatsink", "price"
    )
    list_filter = ("brand", "pcie_generation", "heatsink")


@admin.register(GameConsole)
class GameConsoleAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "brand", "model",
        "storage", "resolution_support", "price"
    )
    list_filter = ("brand", "generation", "ray_tracing")


@admin.register(PowerBank)
class PowerBankAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "brand", "capacity",
        "max_output_power", "wireless_charging", "price"
    )
    list_filter = ("brand", "pd_support", "wireless_charging")


@admin.register(Printer)
class PrinterAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "brand", "printer_type",
        "color_printing", "duplex_printing", "price"
    )
    list_filter = ("brand", "printer_type", "color_printing")


@admin.register(SmartWatch)
class SmartWatchAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "brand", "model",
        "os", "battery_life", "price"
    )
    list_filter = ("brand", "os", "cellular")


@admin.register(AppleWatch)
class AppleWatchAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "series", "chip",
        "always_on_display", "price"
    )
    list_filter = ("series", "ecg", "titanium_case")


@admin.register(Mouse)
class MouseAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "brand", "model",
        "connection_type", "dpi", "price"
    )
    list_filter = ("brand", "connection_type", "rgb")


@admin.register(Keyboard)
class KeyboardAdmin(BaseProductAdmin):
    list_display = (
        "id", "title", "brand", "model",
        "keyboard_type", "layout", "price"
    )
    list_filter = ("brand", "keyboard_type", "rgb")
