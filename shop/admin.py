from django.contrib import admin
from .models import (
    Category,
    Product,
    Phone,
    Tablet,
    PC,
    Monitor,
    Laptop,
    GamingLaptop,
    Headphones,
    Modem,
    FlashDrive,
    HardDrive,
    HDD,
    SSD,
    ExternalHardDrive,
    NVMeSSD,
    GameConsole,
    PowerBank,
    Printer,
    SmartWatch,
    AppleWatch,
    Mouse,
    Keyboard,
)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'category', 'price', 'discount', 'counts', 'rate', 'seller')
    list_filter = ('category', 'brand', 'seller')
    search_fields = ('title', 'brand', 'slug', 'seller')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('price', 'discount', 'counts')


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'model', 'ram', 'internal_storage', 'price', 'counts')
    list_filter = ('brand', 'os')
    search_fields = ('title', 'brand', 'model')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tablet)
class TabletAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'model', 'screen_size', 'has_pen', 'price', 'counts')
    list_filter = ('brand', 'has_pen', 'cellular')
    search_fields = ('title', 'brand', 'model')
    prepopulated_fields = {'slug': ('title',)}



@admin.register(PC)
class PCAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'cpu', 'ram', 'gpu', 'price', 'counts')
    list_filter = ('brand', 'ram_type', 'storage_type')
    search_fields = ('title', 'brand', 'cpu', 'gpu')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'screen_size', 'screen_resolution', 'refresh_rate', 'price')
    list_filter = ('brand', 'panel_type')
    search_fields = ('title', 'brand')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'cpu', 'ram', 'screen_size', 'price', 'counts')
    list_filter = ('brand', 'touchscreen', 'convertible')
    search_fields = ('title', 'brand', 'cpu')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(GamingLaptop)
class GamingLaptopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'dedicated_gpu', 'cpu', 'ram', 'price', 'counts')
    list_filter = ('brand', 'rgb_keyboard', 'mux_switch')
    search_fields = ('title', 'brand', 'dedicated_gpu')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Headphones)
class HeadphonesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'model', 'connection_type', 'noise_cancellation', 'price')
    list_filter = ('brand', 'connection_type', 'noise_cancellation', 'form_factor')
    search_fields = ('title', 'brand', 'model')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Modem)
class ModemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'model', 'modem_type', 'wifi_standard', 'price')
    list_filter = ('brand', 'modem_type', 'sim_support')
    search_fields = ('title', 'brand', 'model')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(FlashDrive)
class FlashDriveAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'capacity', 'interface', 'read_speed', 'price')
    list_filter = ('brand', 'interface', 'waterproof')
    search_fields = ('title', 'brand', 'model')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(HardDrive)
class HardDriveAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'capacity', 'interface', 'form_factor', 'price')
    list_filter = ('brand', 'interface', 'form_factor')
    search_fields = ('title', 'brand', 'model')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(HDD)
class HDDAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'capacity', 'rpm', 'form_factor', 'price')
    list_filter = ('brand', 'rpm')
    search_fields = ('title', 'brand', 'model')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(SSD)
class SSDAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'capacity', 'nand_type', 'read_speed', 'price')
    list_filter = ('brand', 'nand_type', 'pcie_generation')
    search_fields = ('title', 'brand', 'model')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ExternalHardDrive)
class ExternalHardDriveAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'capacity', 'drive_type', 'connection', 'price')
    list_filter = ('brand', 'drive_type', 'portable', 'waterproof')
    search_fields = ('title', 'brand', 'model')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(NVMeSSD)
class NVMeSSDAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'capacity', 'read_speed', 'heatsink', 'price')
    list_filter = ('brand', 'pcie_generation', 'heatsink')
    search_fields = ('title', 'brand', 'model')
    prepopulated_fields = {'slug': ('title',)}



@admin.register(GameConsole)
class GameConsoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'model', 'storage', 'resolution_support', 'price')
    list_filter = ('brand', 'generation', 'ray_tracing')
    search_fields = ('title', 'brand', 'model')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(PowerBank)
class PowerBankAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'capacity', 'max_output_power', 'wireless_charging', 'price')
    list_filter = ('brand', 'pd_support', 'wireless_charging')
    search_fields = ('title', 'brand', 'model')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'printer_type', 'color_printing', 'duplex_printing', 'price')
    list_filter = ('brand', 'printer_type', 'color_printing', 'scanner')
    search_fields = ('title', 'brand', 'model')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(SmartWatch)
class SmartWatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'model', 'os', 'battery_life', 'price')
    list_filter = ('brand', 'os', 'cellular')
    search_fields = ('title', 'brand', 'model')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(AppleWatch)
class AppleWatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'series', 'chip', 'always_on_display', 'price', 'counts')
    list_filter = ('series', 'ecg', 'titanium_case')
    search_fields = ('title', 'series', 'model')
    prepopulated_fields = {'slug': ('title',)}



@admin.register(Mouse)
class MouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'model', 'connection_type', 'dpi', 'price')
    list_filter = ('brand', 'connection_type', 'rgb', 'ergonomic')
    search_fields = ('title', 'brand', 'model')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Keyboard)
class KeyboardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'model', 'keyboard_type', 'layout', 'price')
    list_filter = ('brand', 'keyboard_type', 'rgb', 'backlight')
    search_fields = ('title', 'brand', 'model')
    prepopulated_fields = {'slug': ('title',)}