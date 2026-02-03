for i = 0, 3 do
    minetest.register_node("colorfull:pixel_" .. i, {
        description = "Cinema Pixel Layer " .. i,
        tiles = {"white_block.png"},
        paramtype2 = "color",
        palette = "pal_" .. i .. ".png", 
        -- Настройка групп: 
        -- oddly_breakable_by_hand = 3 (ломается рукой быстро)
        -- snappy = 3 (быстро ломается мечом/рукой)
        -- dig_immediate = 3 (моментальная поломка, как у факелов или цветов)
        groups = {
            oddly_breakable_by_hand = 3, 
            snappy = 3, 
            dig_immediate = 3,
            not_in_creative_inventory = 1
        },
        sunlight_propagates = true,
        pointable = true, -- Теперь на блок можно навестись и ударить
        is_ground_content = false,
    })
end