import enum


class FilterName(enum.IntEnum):
    DISCOVER = 0  # 探索滤镜
    PLAYER = 1  # 领土滤镜


class ResourceName(enum.StrEnum):
    ENERGY = "energy"
    MINERAL = "mineral"
    FOOD = "food"
    CUSTOMER = "customer"
    ALLOY = "alloy"
    PHYSICS = "physics"
    ENGINEER = "engineer"
    BEYOND = "beyond"


ResourceList = (
    ResourceName.ENGINEER,
    ResourceName.MINERAL,
    ResourceName.FOOD,
    ResourceName.CUSTOMER,
    ResourceName.ALLOY,
    ResourceName.PHYSICS,
    ResourceName.ENGINEER,
    ResourceName.BEYOND
)
