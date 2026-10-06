from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/products')
    price = models.PositiveIntegerField()
    seller = models.CharField(max_length=100)
    weight = models.PositiveSmallIntegerField(null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    counts = models.PositiveSmallIntegerField()
    discount = models.PositiveSmallIntegerField(default=0)
    rate = models.FloatField(default=0)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Phone(Product):
    model = models.CharField(max_length=250)
    cpu = models.CharField(max_length=100)
    cpu_frequency = models.CharField(max_length=25)
    ram = models.CharField(max_length=25)
    screen_type = models.CharField(max_length=50)
    screen_size = models.CharField(max_length=25)
    screen_resolution = models.CharField(max_length=25)
    refresh_rate = models.CharField(max_length=25)
    os = models.CharField(max_length=25)
    android = models.CharField(max_length=25, null=True, blank=True)
    update_support = models.CharField(max_length=25, null=True, blank=True)
    camera = models.CharField(max_length=25)
    battery = models.CharField(max_length=25)
    internal_storage = models.CharField(max_length=25)
    sim = models.CharField(max_length=10)
    net_interface = models.CharField(max_length=25)
    bluetooth = models.CharField(max_length=25)
    gps = models.CharField(max_length=100)
    usb_interface = models.CharField(max_length=25)
    speaker = models.CharField(max_length=150)
    charge_port = models.CharField(max_length=25)


class Tablet(Phone):
    has_pen = models.BooleanField(default=False)
    pen_type = models.CharField(max_length=50, null=True, blank=True)
    keyboard_support = models.BooleanField(default=False)
    cellular = models.BooleanField(default=False)
    speakers_count = models.PositiveSmallIntegerField(null=True, blank=True)
    face_unlock = models.BooleanField(default=False)
    fingerprint = models.BooleanField(default=False)
    expand_storage = models.BooleanField(default=False)
    dimensions = models.CharField(max_length=50, null=True, blank=True)
    thickness = models.CharField(max_length=25, null=True, blank=True)


class PC(Product):
    cpu = models.CharField(max_length=100)
    cpu_cores = models.CharField(max_length=25)
    cpu_frequency = models.CharField(max_length=25)
    ram = models.CharField(max_length=25)
    ram_type = models.CharField(max_length=25)
    storage = models.CharField(max_length=50)
    storage_type = models.CharField(max_length=25)
    gpu = models.CharField(max_length=100)
    gpu_memory = models.CharField(max_length=25)
    motherboard = models.CharField(max_length=100)
    form_factor = models.CharField(max_length=25)
    case = models.CharField(max_length=100)
    psu = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    ports = models.CharField(max_length=200)
    wifi = models.CharField(max_length=50)
    bluetooth = models.CharField(max_length=25)


class Monitor(Product):
    screen_size = models.CharField(max_length=25)
    screen_resolution = models.CharField(max_length=25)
    panel_type = models.CharField(max_length=50)
    aspect_ratio = models.CharField(max_length=15)
    refresh_rate = models.CharField(max_length=25)
    response_time = models.CharField(max_length=25)
    brightness = models.CharField(max_length=25)
    contrast_ratio = models.CharField(max_length=25)
    color_gamut = models.CharField(max_length=50)
    hdr_support = models.CharField(max_length=50)
    adaptive_sync = models.CharField(max_length=50)
    ports = models.CharField(max_length=150)
    stand_adjustable = models.BooleanField(default=False)
    vesa_mount = models.BooleanField(default=False)
    speakers = models.BooleanField(default=False)


class Laptop(PC):
    
    screen_size = models.CharField(max_length=25)
    screen_resolution = models.CharField(max_length=25)
    panel_type = models.CharField(max_length=50)
    aspect_ratio = models.CharField(max_length=15)
    refresh_rate = models.CharField(max_length=25)
    response_time = models.CharField(max_length=25, null=True, blank=True)
    brightness = models.CharField(max_length=25, null=True, blank=True)
    contrast_ratio = models.CharField(max_length=25, null=True, blank=True)
    color_gamut = models.CharField(max_length=50, null=True, blank=True)
    hdr_support = models.CharField(max_length=50, null=True, blank=True)
    adaptive_sync = models.CharField(max_length=50, null=True, blank=True)

    battery = models.CharField(max_length=50)
    battery_life = models.CharField(max_length=50)
    charge_port = models.CharField(max_length=50)
    keyboard_backlight = models.BooleanField(default=False)
    keyboard_layout = models.CharField(max_length=50)
    touchpad = models.CharField(max_length=50)
    webcam = models.CharField(max_length=50)
    speakers = models.CharField(max_length=100)
    microphone = models.CharField(max_length=50)
    touchscreen = models.BooleanField(default=False)
    convertible = models.BooleanField(default=False)
    fingerprint = models.BooleanField(default=False)
    face_unlock = models.BooleanField(default=False)
    thickness = models.CharField(max_length=25)
    dimensions = models.CharField(max_length=50)


class GamingLaptop(Laptop):
    cooling_system = models.CharField(max_length=100)
    rgb_keyboard = models.BooleanField(default=True)
    high_refresh_display = models.BooleanField(default=True)
    dedicated_gpu = models.CharField(max_length=100)
    mux_switch = models.BooleanField(default=False)
    advanced_audio = models.CharField(max_length=80, null=True, blank=True)
    gaming_ports = models.CharField(max_length=150, null=True, blank=True)


class Headphones(Product):
    model = models.CharField(max_length=100)
    connection_type = models.CharField(max_length=50)
    wireless_technology = models.CharField(max_length=50, null=True, blank=True)
    driver_size = models.CharField(max_length=25)
    frequency_response = models.CharField(max_length=50)
    impedance = models.CharField(max_length=25)
    sensitivity = models.CharField(max_length=25)
    noise_cancellation = models.BooleanField(default=False)
    microphone = models.BooleanField(default=False)
    battery_life = models.CharField(max_length=50, null=True, blank=True)
    charging_port = models.CharField(max_length=30, null=True, blank=True)
    water_resistance = models.CharField(max_length=30, null=True, blank=True)
    form_factor = models.CharField(max_length=50)


class Modem(Product):
    model = models.CharField(max_length=100)
    modem_type = models.CharField(max_length=50)
    wifi_standard = models.CharField(max_length=30)
    max_speed = models.CharField(max_length=50)
    frequency_bands = models.CharField(max_length=50)
    antennas = models.CharField(max_length=30)
    ports = models.CharField(max_length=150)
    sim_support = models.BooleanField(default=False)
    coverage_area = models.CharField(max_length=50, null=True, blank=True)
    security = models.CharField(max_length=100)


class FlashDrive(Product):
    model = models.CharField(max_length=100)
    capacity = models.CharField(max_length=30)
    interface = models.CharField(max_length=50)
    read_speed = models.CharField(max_length=30)
    write_speed = models.CharField(max_length=30)
    form_factor = models.CharField(max_length=50)
    waterproof = models.BooleanField(default=False)
    shockproof = models.BooleanField(default=False)
    encryption = models.BooleanField(default=False)
    material = models.CharField(max_length=50, null=True, blank=True)


class HardDrive(Product):
    
    model = models.CharField(max_length=100)
    capacity = models.CharField(max_length=30)
    interface = models.CharField(max_length=50)
    form_factor = models.CharField(max_length=30)
    read_speed = models.CharField(max_length=40)
    write_speed = models.CharField(max_length=40)
    cache = models.CharField(max_length=30, null=True, blank=True)
    mtbf = models.CharField(max_length=40, null=True, blank=True)
    warranty = models.CharField(max_length=30, null=True, blank=True)


class HDD(HardDrive):
    
    rpm = models.CharField(max_length=20)
    platter_count = models.PositiveSmallIntegerField(null=True, blank=True)
    noise_level = models.CharField(max_length=30, null=True, blank=True)


class SSD(HardDrive):
    
    nand_type = models.CharField(max_length=40)
    controller = models.CharField(max_length=80, null=True, blank=True)
    dram_cache = models.BooleanField(default=True)
    tbw = models.CharField(max_length=30, null=True, blank=True)
    pcie_generation = models.CharField(max_length=20, null=True, blank=True)


class ExternalHardDrive(HardDrive):
    
    drive_type = models.CharField(max_length=20)
    connection = models.CharField(max_length=50)
    portable = models.BooleanField(default=True)
    power_source = models.CharField(max_length=40)
    encryption = models.BooleanField(default=False)
    waterproof = models.BooleanField(default=False)
    shockproof = models.BooleanField(default=False)


class NVMeSSD(SSD):
    
    heatsink = models.BooleanField(default=False)
    max_temperature = models.CharField(max_length=20, null=True, blank=True)


class GameConsole(Product):
    model = models.CharField(max_length=100)
    generation = models.CharField(max_length=30)
    storage = models.CharField(max_length=40)
    storage_type = models.CharField(max_length=30)
    expandable_storage = models.BooleanField(default=True)
    resolution_support = models.CharField(max_length=50)
    ray_tracing = models.BooleanField(default=False)
    cpu = models.CharField(max_length=80)
    gpu = models.CharField(max_length=80)
    ram = models.CharField(max_length=30)
    optical_drive = models.BooleanField(default=False)
    online_service = models.CharField(max_length=50, null=True, blank=True)
    controllers_included = models.PositiveSmallIntegerField(default=1)
    ports = models.CharField(max_length=150)
    wifi = models.CharField(max_length=40)
    bluetooth = models.CharField(max_length=30)
    dimensions = models.CharField(max_length=50, null=True, blank=True)
    power_consumption = models.CharField(max_length=30, null=True, blank=True)


class PowerBank(Product):
    model = models.CharField(max_length=100)
    capacity = models.CharField(max_length=30)
    output_ports = models.CharField(max_length=100)
    input_ports = models.CharField(max_length=80)
    max_output_power = models.CharField(max_length=30)
    fast_charge_support = models.BooleanField(default=True)
    pd_support = models.BooleanField(default=False)
    wireless_charging = models.BooleanField(default=False)
    number_of_ports = models.PositiveSmallIntegerField()
    battery_type = models.CharField(max_length=40)
    display = models.BooleanField(default=False)
    protection_features = models.CharField(max_length=150, null=True, blank=True)


class Printer(Product):
    model = models.CharField(max_length=100)
    printer_type = models.CharField(max_length=40)
    color_printing = models.BooleanField(default=True)
    print_speed = models.CharField(max_length=40)
    max_resolution = models.CharField(max_length=40)
    paper_size = models.CharField(max_length=50)
    duplex_printing = models.BooleanField(default=False)
    connectivity = models.CharField(max_length=100)
    scanner = models.BooleanField(default=False)
    copier = models.BooleanField(default=False)
    fax = models.BooleanField(default=False)
    monthly_duty_cycle = models.CharField(max_length=40, null=True, blank=True)
    ink_or_toner = models.CharField(max_length=50)
    automatic_document_feeder = models.BooleanField(default=False)
    touchscreen = models.BooleanField(default=False)


class SmartWatch(Product):
    model = models.CharField(max_length=100)
    display_type = models.CharField(max_length=50)
    display_size = models.CharField(max_length=25)
    resolution = models.CharField(max_length=30)
    os = models.CharField(max_length=40)
    battery_life = models.CharField(max_length=40)
    water_resistance = models.CharField(max_length=30)
    sensors = models.CharField(max_length=200)
    gps = models.BooleanField(default=True)
    heart_rate_monitor = models.BooleanField(default=True)
    blood_oxygen = models.BooleanField(default=False)
    sleep_tracking = models.BooleanField(default=True)
    connectivity = models.CharField(max_length=80)
    cellular = models.BooleanField(default=False)
    speaker = models.BooleanField(default=False)
    microphone = models.BooleanField(default=False)
    strap_material = models.CharField(max_length=50, null=True, blank=True)
    case_material = models.CharField(max_length=50, null=True, blank=True)
    compatibility = models.CharField(max_length=100)


class AppleWatch(SmartWatch):
    series = models.CharField(max_length=30)
    chip = models.CharField(max_length=40)
    always_on_display = models.BooleanField(default=True)
    ecg = models.BooleanField(default=False)
    temperature_sensor = models.BooleanField(default=False)
    crash_detection = models.BooleanField(default=False)
    fall_detection = models.BooleanField(default=True)
    digital_crown = models.BooleanField(default=True)
    action_button = models.BooleanField(default=False)
    titanium_case = models.BooleanField(default=False)


class Mouse(Product):
    model = models.CharField(max_length=100)
    connection_type = models.CharField(max_length=40)
    sensor_type = models.CharField(max_length=40)
    dpi = models.CharField(max_length=40)
    dpi_adjustable = models.BooleanField(default=True)
    buttons_count = models.PositiveSmallIntegerField()
    programmable_buttons = models.BooleanField(default=False)
    polling_rate = models.CharField(max_length=30, null=True, blank=True)
    rgb = models.BooleanField(default=False)
    ergonomic = models.BooleanField(default=False)
    battery_life = models.CharField(max_length=40, null=True, blank=True)
    hand_orientation = models.CharField(max_length=20, null=True, blank=True)


class Keyboard(Product):
    model = models.CharField(max_length=100)
    connection_type = models.CharField(max_length=40)
    keyboard_type = models.CharField(max_length=40)
    switch_type = models.CharField(max_length=50, null=True, blank=True)
    layout = models.CharField(max_length=30)
    language_layout = models.CharField(max_length=40)
    backlight = models.BooleanField(default=False)
    rgb = models.BooleanField(default=False)
    multimedia_keys = models.BooleanField(default=True)
    wrist_rest = models.BooleanField(default=False)
    n_key_rollover = models.BooleanField(default=False)
    wireless_technology = models.CharField(max_length=40, null=True, blank=True)
    battery_life = models.CharField(max_length=40, null=True, blank=True)
    keycap_material = models.CharField(max_length=40, null=True, blank=True)


class Refrigerator(Product):
    model = models.CharField(max_length=100)
    capacity = models.CharField(max_length=40)
    fridge_type = models.CharField(max_length=50)
    energy_grade = models.CharField(max_length=20)
    freezer = models.BooleanField(default=True)
    no_frost = models.BooleanField(default=False)
    doors_count = models.PositiveSmallIntegerField(default=2)
    dimensions = models.CharField(max_length=50)
    noise_level = models.CharField(max_length=30, null=True, blank=True)
    color_body = models.CharField(max_length=40, null=True, blank=True)


class AirConditioner(Product):
    model = models.CharField(max_length=100)
    ac_type = models.CharField(max_length=50)
    cooling_capacity = models.CharField(max_length=40)
    heating = models.BooleanField(default=False)
    energy_grade = models.CharField(max_length=20)
    inverter = models.BooleanField(default=False)
    area_coverage = models.CharField(max_length=40)
    noise_level = models.CharField(max_length=30, null=True, blank=True)
    refrigerant = models.CharField(max_length=30, null=True, blank=True)


class Sofa(Product):
    model = models.CharField(max_length=100)
    seats = models.PositiveSmallIntegerField()
    material = models.CharField(max_length=50)
    frame_material = models.CharField(max_length=50)
    reclining = models.BooleanField(default=False)
    dimensions = models.CharField(max_length=50)
    style = models.CharField(max_length=40, null=True, blank=True)


class Television(Product):
    model = models.CharField(max_length=100)
    screen_size = models.CharField(max_length=25)
    screen_resolution = models.CharField(max_length=30)
    panel_type = models.CharField(max_length=40)
    smart_tv = models.BooleanField(default=True)
    os = models.CharField(max_length=40, null=True, blank=True)
    hdr_support = models.CharField(max_length=50, null=True, blank=True)
    refresh_rate = models.CharField(max_length=25, null=True, blank=True)
    ports = models.CharField(max_length=150)
    speakers = models.CharField(max_length=50, null=True, blank=True)


class Speaker(Product):
    model = models.CharField(max_length=100)
    speaker_type = models.CharField(max_length=50)
    power_output = models.CharField(max_length=40)
    connection_type = models.CharField(max_length=50)
    channels = models.CharField(max_length=30, null=True, blank=True)
    wireless = models.BooleanField(default=False)
    battery_life = models.CharField(max_length=40, null=True, blank=True)
    waterproof = models.BooleanField(default=False)


class Bed(Product):
    model = models.CharField(max_length=100)
    size = models.CharField(max_length=40)
    material = models.CharField(max_length=50)
    storage = models.BooleanField(default=False)
    headboard = models.BooleanField(default=True)
    dimensions = models.CharField(max_length=50)
    style = models.CharField(max_length=40, null=True, blank=True)


class Pillow(Product):
    model = models.CharField(max_length=100)
    fill_material = models.CharField(max_length=50)
    cover_material = models.CharField(max_length=50)
    size = models.CharField(max_length=40)
    firmness = models.CharField(max_length=30, null=True, blank=True)
    washable = models.BooleanField(default=True)
    hypoallergenic = models.BooleanField(default=False)


class Mattress(Product):
    model = models.CharField(max_length=100)
    size = models.CharField(max_length=40)
    mattress_type = models.CharField(max_length=50)
    thickness = models.CharField(max_length=25)
    firmness = models.CharField(max_length=30)
    material = models.CharField(max_length=50)
    layers = models.CharField(max_length=80, null=True, blank=True)
    warranty = models.CharField(max_length=30, null=True, blank=True)


class Carpet(Product):
    model = models.CharField(max_length=100)
    size = models.CharField(max_length=40)
    material = models.CharField(max_length=50)
    carpet_type = models.CharField(max_length=40)
    thickness = models.CharField(max_length=25, null=True, blank=True)
    pattern = models.CharField(max_length=50, null=True, blank=True)
    washable = models.BooleanField(default=False)
    origin = models.CharField(max_length=40, null=True, blank=True)


class GasStove(Product):
    model = models.CharField(max_length=100)
    burners_count = models.PositiveSmallIntegerField()
    stove_type = models.CharField(max_length=40)
    oven = models.BooleanField(default=False)
    ignition = models.CharField(max_length=40)
    material = models.CharField(max_length=40)
    dimensions = models.CharField(max_length=50)
    safety_valve = models.BooleanField(default=True)


class Sink(Product):
    model = models.CharField(max_length=100)
    sink_type = models.CharField(max_length=40)
    material = models.CharField(max_length=40)
    bowls_count = models.PositiveSmallIntegerField(default=1)
    dimensions = models.CharField(max_length=50)
    mounting = models.CharField(max_length=40)
    faucet_included = models.BooleanField(default=False)


class WashingMachine(Product):
    model = models.CharField(max_length=100)
    capacity = models.CharField(max_length=30)
    machine_type = models.CharField(max_length=40)
    energy_grade = models.CharField(max_length=20)
    spin_speed = models.CharField(max_length=30)
    programs_count = models.PositiveSmallIntegerField(null=True, blank=True)
    inverter = models.BooleanField(default=False)
    dimensions = models.CharField(max_length=50)
    display = models.BooleanField(default=True)


class Dishwasher(Product):
    model = models.CharField(max_length=100)
    capacity = models.CharField(max_length=30)
    machine_type = models.CharField(max_length=40)
    energy_grade = models.CharField(max_length=20)
    programs_count = models.PositiveSmallIntegerField(null=True, blank=True)
    noise_level = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=50)
    display = models.BooleanField(default=True)
    water_usage = models.CharField(max_length=30, null=True, blank=True)


class PackageBoiler(Product):
    model = models.CharField(max_length=100)
    boiler_type = models.CharField(max_length=40)
    heating_capacity = models.CharField(max_length=40)
    energy_grade = models.CharField(max_length=20)
    fuel_type = models.CharField(max_length=30)
    dual_circuit = models.BooleanField(default=True)
    dimensions = models.CharField(max_length=50)
    efficiency = models.CharField(max_length=30, null=True, blank=True)


class Chandelier(Product):
    model = models.CharField(max_length=100)
    lights_count = models.PositiveSmallIntegerField()
    material = models.CharField(max_length=50)
    style = models.CharField(max_length=40)
    bulb_type = models.CharField(max_length=40)
    dimensions = models.CharField(max_length=50)
    dimmable = models.BooleanField(default=False)
    led = models.BooleanField(default=True)


class Table(Product):
    model = models.CharField(max_length=100)
    table_type = models.CharField(max_length=40)
    material = models.CharField(max_length=50)
    shape = models.CharField(max_length=30)
    dimensions = models.CharField(max_length=50)
    seats = models.PositiveSmallIntegerField(null=True, blank=True)
    extendable = models.BooleanField(default=False)


class Chair(Product):
    model = models.CharField(max_length=100)
    chair_type = models.CharField(max_length=40)
    material = models.CharField(max_length=50)
    adjustable = models.BooleanField(default=False)
    armrest = models.BooleanField(default=False)
    wheels = models.BooleanField(default=False)
    max_weight = models.CharField(max_length=30, null=True, blank=True)
    dimensions = models.CharField(max_length=50, null=True, blank=True)