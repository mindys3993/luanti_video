-- Simple node registration for 4 palette layers
for i = 0, 3 do
    minetest.register_node("colorfull:pixel_" .. i, {
        description = "Cinema Pixel Layer " .. i,
        tiles = {"white_block.png"},
        paramtype2 = "color",
        palette = "pal_" .. i .. ".png", 
        groups = {
            oddly_breakable_by_hand = 3, 
            snappy = 3, 
            dig_immediate = 3, -- Instant break
            not_in_creative_inventory = 1
        },
        sunlight_propagates = true,
        pointable = true,
        is_ground_content = false,
    })
end
