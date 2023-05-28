DX = 2

WIDTH = 1280
HEIGHT = 720

# 游戏主界面的四边
GAME_TOP = 0
GAME_BOTTOM = HEIGHT
GAME_LEFT = DX
GAME_RIGHT = WIDTH

# 游戏主界面的尺寸
GAME_WIDTH = WIDTH - DX
GAME_HEIGHT = HEIGHT - DX

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
WORLD_TOP = GAME_TOP + RESOURCE_HEIGHT + DX
WORLD_BOTTOM = WORLD_TOP + WORLD_HEIGHT

# 滤镜面板尺寸
FILTER_HEIGHT = 30
FILTER_WIDTH = GAME_WIDTH - WORLD_HEIGHT - DX * 2
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

# 消息面板的文字高度
MESSAGE_TEXT_HEIGHT = 16
# 消息面板展示的消息行数
MESSAGE_LINE_NUMBER = 5
# 消息面板的高度
MESSAGE_BOX_HEIGHT = MESSAGE_TEXT_HEIGHT * MESSAGE_LINE_NUMBER
