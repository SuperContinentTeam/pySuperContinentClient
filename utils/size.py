WIDTH = 1280
HEIGHT = 720

# 游戏主界面的四边
GAME_TOP = 0
GAME_LEFT = 0

# 游戏主界面的尺寸
GAME_WIDTH = WIDTH
GAME_HEIGHT = HEIGHT

# 资源面板的高度/宽度
RESOURCE_HEIGHT = 30

# 资源面板坐标
RESOURCE_LEFT = GAME_LEFT
RESOURCE_RIGHT = RESOURCE_LEFT + GAME_WIDTH
RESOURCE_TOP = GAME_TOP
RESOURCE_BOTTOM = RESOURCE_TOP + RESOURCE_HEIGHT

# 地图高度/宽度
WORLD_HEIGHT = GAME_HEIGHT - RESOURCE_HEIGHT

# 地图顶部坐标
WORLD_LEFT = GAME_LEFT
WORLD_RIGHT = WORLD_LEFT + WORLD_HEIGHT
WORLD_TOP = GAME_TOP + RESOURCE_HEIGHT
WORLD_BOTTOM = WORLD_TOP + WORLD_HEIGHT

# 滤镜面板尺寸
FILTER_HEIGHT = 30
FILTER_WIDTH = GAME_WIDTH - WORLD_HEIGHT

# 滤镜面板坐标
FILTER_LEFT = WORLD_HEIGHT
FILTER_RIGHT = FILTER_LEFT + FILTER_WIDTH
FILTER_TOP = WORLD_TOP
FILTER_BOTTOM = FILTER_TOP + FILTER_HEIGHT

# 区划尺寸
ZONING_HEIGHT = WORLD_HEIGHT // 2

# 区划坐标
ZONING_TOP = WORLD_TOP + FILTER_HEIGHT
ZONING_BOTTOM = ZONING_TOP + ZONING_HEIGHT
ZONING_LEFT = WORLD_HEIGHT
ZONING_RIGHT = ZONING_LEFT + ZONING_HEIGHT

# 进度区域尺寸
SCHEDULE_WIDTH = RESOURCE_RIGHT - ZONING_RIGHT
SCHEDULE_HEIGHT = ZONING_HEIGHT

# 进度区域坐标
SCHEDULE_LEFT = ZONING_RIGHT
SCHEDULE_TOP = ZONING_TOP

# 输入框尺寸
INPUT_WIDTH = ZONING_HEIGHT
INPUT_HEIGHT = 30

# 消息面板尺寸
MESSAGE_BOX_WIDTH = ZONING_HEIGHT
MESSAGE_BOX_HEIGHT = WORLD_BOTTOM - ZONING_BOTTOM - FILTER_HEIGHT

# 消息面板坐标
MESSAGE_BOX_LEFT = ZONING_LEFT
MESSAGE_BOX_TOP = ZONING_BOTTOM
MESSAGE_BOX_BOTTOM = MESSAGE_BOX_TOP + MESSAGE_BOX_HEIGHT

# 输入框坐标
INPUT_LEFT = ZONING_LEFT
INPUT_TOP = MESSAGE_BOX_BOTTOM

# 信息框尺寸
INFORMATION_WIDTH = SCHEDULE_WIDTH
INFORMATION_HEIGHT = MESSAGE_BOX_HEIGHT + INPUT_HEIGHT

# 信息框坐标
INFORMATION_LEFT = SCHEDULE_LEFT
INFORMATION_TOP = MESSAGE_BOX_TOP
