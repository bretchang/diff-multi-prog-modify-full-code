from module import Program
from entry import Authentication
app = "Diff Multi_Prog"
e = Authentication(app)

"""
===================================
 輸入 ECR, 撈資料時間, 訓練時間
===================================
"""

equipment = "DKPEWZ02"
chamber = "DKPEWZ02_DKPEPW02"
# MainRecipe/1_Product/D2Y0BSIGE_3_B  MainRecipe/1_Product/D2Y0BSIGE_3_C  MainRecipe/1_Product/D2Y1BSIGE_0M_B
# recipe = ["MainRecipe/1_Product/D2Y0BSIGE_3_%", "MainRecipe/1_Product/D2Y1BSIGE_0M_B"]
recipe = ["MainRecipe/1_Product/D2Y0WLPOL%"]

starttime = "2025-01-01"
endtime = "2025-06-01"

training_starttime = "2025-01-01 00:00:00"
training_endtime = "2025-03-01 00:00:00"


p = Program(equipment, chamber, recipe, starttime, endtime,
            training_starttime, training_endtime, e)


"""
===================================
 下載資料
===================================
"""

p.query()


"""
===================================
 過濾 recipe step
===================================
"""

# p.show_all_recipe_steps()

# recipe_step = ['A_PURGE2', 'OX_PRG1']
# p.use_filtered_recipe_steps(recipe_step)


"""
===================================
 使用 all recipe step
===================================
"""

p.use_all_recipe_steps()


"""
===================================
 輸出 raw data
===================================
"""

p.output_raw_data()


"""
===================================
 修改子系統分類
===================================
"""

p.output_category()
p.input_category()


"""
===================================
 進行子系統分析
===================================
"""

p.run(training_starttime, training_endtime)
