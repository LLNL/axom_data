-- The sphere scale has a default value of 1.0 that can be overridden
local sphere_scale = sphere_scale or 1.0

dimensions = 3

shapes = {
  {
    name = "sphere",
    material = "steel",
    geometry = {
      format = "stl",
      path = "../quest/sphere.stl",
      units = "cm",
      operators = {
        { scale = function() return {sphere_scale} end }
      }
    }
  }
}
